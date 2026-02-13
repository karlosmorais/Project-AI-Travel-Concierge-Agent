import os
import sys
import json
import asyncio
from semantic_kernel import Kernel
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
from dotenv import load_dotenv

# Add parent directory to path to import app module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

load_dotenv()

async def evaluate_agent():
    """
    Run LLM judge to evaluate agent performance.
    """
    # 1. Setup Judge Kernel
    kernel = Kernel()
    chat_service = AzureChatCompletion(
        service_id="judge",
        deployment_name=os.environ.get("AZURE_OPENAI_CHAT_DEPLOYMENT"),
        endpoint=os.environ.get("AZURE_OPENAI_ENDPOINT"),
        api_key=os.environ.get("AZURE_OPENAI_KEY"),
    )
    kernel.add_service(chat_service)
    
    # 2. Define Evaluation Criteria
    rubric = """
    Evaluate the Travel Agent response based on the following criteria:
    1. Accuracy (0-10): Are facts (weather, currency) correct?
    2. Completeness (0-10): Does it cover all user requirements?
    3. Relevance (0-10): Is the info relevant to the query?
    4. Tool Use (0-10): Did it appear to use tools effectively?
    5. Formatting (0-10): Is the output valid JSON?
    
    Return a valid JSON object with scores and a total score (0-50).
    """
    
    # 3. specific test case
    test_input = "I want to go to Paris from 2026-06-01 to 2026-06-08 with my BankGold card"
    # We need to run the agent to get the output
    from app.main import run_request_async
    agent_output = await run_request_async(test_input)
    
    prompt = f"""
    {rubric}
    
    User Query: {test_input}
    Agent Response: {agent_output}
    
    Evaluation:
    """
    
    # 4. Run Evaluation
    result = await kernel.invoke_prompt(prompt)
    
    print("Agent Response:")
    print(agent_output)
    print("\nJudge Evaluation:")
    print(result)
    
    return str(result)

if __name__ == "__main__":
    asyncio.run(evaluate_agent())