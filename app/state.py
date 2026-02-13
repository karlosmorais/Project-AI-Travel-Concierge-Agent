# app/state.py
from enum import Enum
from typing import List, Optional, Dict, Any
import logging

logger = logging.getLogger(__name__)

class Phase(Enum):
    """Agent execution phases."""
    Init = "Init"
    ClarifyRequirements = "ClarifyRequirements"
    PlanTools = "PlanTools"
    ExecuteTools = "ExecuteTools"
    AnalyzeResults = "AnalyzeResults"
    ResolveIssues = "ResolveIssues"
    Synthesize = "Synthesize"
    Done = "Done"

class AgentState:
    """
    Manages agent execution state through the workflow phases.
    """
    
    def __init__(self):
        self.phase = Phase.Init
        self.requirements: Dict[str, Any] = {}
        self.history: List[str] = []
        self.tools_called: List[str] = []
        self.tool_outputs: Dict[str, Any] = {}
        self.iteration: int = 0
        self.max_iterations: int = 15
    
    def set_requirements(self, requirements: Dict[str, Any]):
        """Set requirements."""
        self.requirements = requirements

    def add_tool_call(self, tool_name: str, input_data: Any, output_data: Any):
        """Record a tool call."""
        self.tools_called.append(tool_name)
        self.tool_outputs[tool_name] = output_data

    def advance(self):
        """
        Advance to the next phase in the workflow based on current state.
        This is a simple linear progression for now, but can be more dynamic.
        """
        previous_phase = self.phase
        
        if self.phase == Phase.Init:
            self.phase = Phase.ClarifyRequirements
            
        elif self.phase == Phase.ClarifyRequirements:
            # If we have basic requirements, move to planning
            if self._has_basic_requirements():
                self.phase = Phase.PlanTools
            else:
                # Stay here if we need more info (in a real loop would ask user)
                # For this automated flow, we assume we extract what we can
                self.phase = Phase.PlanTools 
                
        elif self.phase == Phase.PlanTools:
            self.phase = Phase.ExecuteTools
            
        elif self.phase == Phase.ExecuteTools:
            self.phase = Phase.AnalyzeResults
            
        elif self.phase == Phase.AnalyzeResults:
            # If analysis shows missing data, could go back to PlanTools
            # For now, proceed to Synthesis
            self.phase = Phase.Synthesize
            
        elif self.phase == Phase.Synthesize:
            self.phase = Phase.Done
            
        elif self.phase == Phase.Done:
            pass # Stay in Done
            
        logger.info(f"State transition: {previous_phase.value} -> {self.phase.value}")
    
    def _has_basic_requirements(self) -> bool:
        """Check if we have minimum requirements."""
        return "destination" in self.requirements and "dates" in self.requirements

    def reset(self):
        """
        Reset the state to initial values.
        """
        self.phase = Phase.Init
        self.requirements = {}
        self.history = []
        self.tools_called = []
        self.tool_outputs = []
        self.iteration = 0