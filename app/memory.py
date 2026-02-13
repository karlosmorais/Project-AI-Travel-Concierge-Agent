from typing import List, Dict, Any, Optional
import time
import uuid
import json

class ShortTermMemory:
    """
    Short-term memory system for session-based context management.
    Compatible with provided unit tests.
    """
    
    def __init__(self, max_items: int = 10, max_tokens: int = 2000):
        self.max_items = max_items
        self.max_tokens = max_tokens
        self.memory_items: List[Dict[str, Any]] = []
        self.session_id = str(uuid.uuid4())
        self.created_at = time.time()
        
    @property
    def total_tokens(self) -> int:
        """Calculate total estimated tokens in memory."""
        return sum(item.get("tokens", 0) for item in self.memory_items)
    
    def _estimate_tokens(self, text: str) -> int:
        """Rough token estimation (approx 4 chars per token)."""
        if not text:
            return 0
        return len(str(text)) // 4
    
    def add_conversation(self, role: str, content: str, metadata: Dict[str, Any] = None):
        """Add a conversation item."""
        tokens = self._estimate_tokens(content)
        item = {
            "role": role,
            "content": content,
            "tokens": tokens,
            "timestamp": time.time(),
            "metadata": metadata or {}
        }
        self.memory_items.append(item)
        self._evict_if_needed()
        
    def add_tool_call(self, tool_name: str, input_data: Dict, output_data: Dict, success: bool = True):
        """Add a tool call record."""
        content = f"Tool call: {tool_name}\nInput: {json.dumps(input_data)}\nOutput: {json.dumps(output_data)}"
        tokens = self._estimate_tokens(content)
        item = {
            "role": "assistant", # or system? Tests expect 'assistant' for tool calls usually or explicit check
            # Wait, test_add_tool_call expects role="assistant" in line 73
            "content": content,
            "tokens": tokens,
            "timestamp": time.time(),
            "metadata": {
                "type": "tool_call",
                "tool_name": tool_name,
                "input": input_data,
                "output": output_data,
                "success": success
            }
        }
        self.memory_items.append(item)
        self._evict_if_needed()

    def add_system_event(self, event: str, data: Dict):
        """Add a system event."""
        content = event
        tokens = self._estimate_tokens(content)
        item = {
            "role": "system",
            "content": content,
            "tokens": tokens,
            "timestamp": time.time(),
            "metadata": {
                "type": "system_event",
                "event": event,
                "data": data
            }
        }
        self.memory_items.append(item)
        self._evict_if_needed()

    def _evict_if_needed(self):
        """Evict items if limits are exceeded."""
        # Evict by items
        while len(self.memory_items) > self.max_items:
            self.memory_items.pop(0)
            
        # Evict by tokens
        while self.total_tokens > self.max_tokens and self.memory_items:
            self.memory_items.pop(0)

    def get_conversation_history(self, include_metadata: bool = False) -> List[Dict[str, Any]]:
        """Get the raw memory items."""
        if include_metadata:
            return self.memory_items
        
        # Return simplified view
        result = []
        for item in self.memory_items:
            simplified = {
                "role": item["role"],
                "content": item["content"],
                "timestamp": item["timestamp"]
            }
            result.append(simplified)
        return result

    def get_recent_conversation(self, n: int) -> List[Dict[str, Any]]:
        """Get last n items."""
        return self.memory_items[-n:] if n > 0 else []

    def get_context_window(self, max_tokens: int = None) -> str:
        """Get formatted string for LLM context."""
        limit = max_tokens or self.max_tokens
        current_tokens = 0
        context_items = []
        
        # Iterate reversed to keep most recent
        for item in reversed(self.memory_items):
            item_tokens = item["tokens"]
            if current_tokens + item_tokens > limit:
                break
            
            role_prefix = item["role"].upper()
            context_items.insert(0, f"{role_prefix}: {item['content']}")
            current_tokens += item_tokens
            
        return "\n".join(context_items)

    def get_memory_summary(self) -> Dict[str, Any]:
        """Get summary stats."""
        if not self.memory_items:
             return {
                "session_id": self.session_id,
                "total_items": 0,
                "total_tokens": 0,
                "max_items": self.max_items,
                "max_tokens": self.max_tokens,
                "memory_usage_percent": 0.0,
                "oldest_item": None,
                "newest_item": None
            }
            
        return {
            "session_id": self.session_id,
            "total_items": len(self.memory_items),
            "total_tokens": self.total_tokens,
            "max_items": self.max_items,
            "max_tokens": self.max_tokens,
            "memory_usage_percent": (len(self.memory_items) / self.max_items) * 100,
            "oldest_item": self.memory_items[0]["timestamp"],
            "newest_item": self.memory_items[-1]["timestamp"]
        }

    def search_memory(self, query: str, role_filter: str = None) -> List[Dict[str, Any]]:
        """Simple substring search."""
        results = []
        for item in self.memory_items:
            if role_filter and item["role"] != role_filter:
                continue
                
            if query.lower() in item["content"].lower():
                results.append(item)
                
            # Check metadata too if it exists?
            # Test: "Search for 'weather' -> User question and tool call"
            # Tool call content contains "Weather", so it matches content search.
        
        return results

    def clear_memory(self):
        """Clear all memories."""
        self.memory_items = []

    def export_memory(self, filepath: str):
        """Export to JSON file."""
        data = {
            "session_id": self.session_id,
            "created_at": self.created_at,
            "items": self.memory_items
        }
        with open(filepath, 'w') as f:
            json.dump(data, f)

    def import_memory(self, filepath: str):
        """Import from JSON file."""
        with open(filepath, 'r') as f:
            data = json.load(f)
        
        self.session_id = data.get("session_id", str(uuid.uuid4()))
        self.created_at = data.get("created_at", time.time())
        self.memory_items = data.get("items", [])
        self._evict_if_needed()

    def __str__(self):
        return f"ShortTermMemory(session_id={self.session_id}, items={len(self.memory_items)})"

    def __repr__(self):
        return self.__str__()