# Project: AI Travel Concierge Agent

AI Travel Concierge Agent
=========================

Introduction
------------

Welcome! Imagine yourself as a trusted consultant specializing in building smart, efficient, and powerful agent-based workflows for the enterprise. Your latest client, the global financial services leader **‘Banking International’**, urgently requires your expertise to revolutionize their premium client services. Your mission is to develop a sophisticated AI agent that provides an exclusive travel planning service, reinforcing the value of their premium credit cards and enhancing customer loyalty.
The Challenge

-------------

Banking International wants to offer a "Travel Credit Card Concierge" service to its premium members, but lacks the automated, intelligent system to power it. They need an agent that can handle complex travel queries with precision and personalization.

Your challenge is to build a sophisticated AI travel agent that helps customers plan their trips from start to finish. The agent must be able to:

* **Handle specific trip planning**, such as planning a trip from NYC to Paris from June 1st to June 8th next year.
* **Provide general travel information**, including real-time weather, top-rated restaurants, and popular attractions.
* **Recommend the best credit card** for the trip by analyzing the destination and highlighting specific card perks and benefits.
* **Operate with enterprise-grade capabilities**, including using tools (web search, APIs), maintaining short- and long-term memory, retrieving policy knowledge via Retrieval-Augmented Generation (RAG), and managing state across a complex workflow.

To execute this project, you'll utilize your knowledge of agentic AI systems along with your skills in **Python**, **Semantic Kernel**, and **Azure services**.
Core Components & Deliverables

------------------------------

Your completed solution must be a robust Python agent featuring the following components and capabilities.

* **Advanced Tool Integration:** The agent must effectively use tools for function calling to access external data, including web search (Bing) and live APIs (weather, currency exchange rates).
* **Stateful Orchestration:** Implement an explicit state machine to manage the conversation's flow, guiding the user through stages like clarification, planning, execution, and synthesis.
* **Structured & Validated Outputs:** Ensure the agent produces reliable, Pydantic-validated JSON objects for itineraries and recommendations, complete with source citations.
* **Dual Memory System:**
* Short-Term Memory: Maintain a conversation buffer to keep track of the immediate context.
* Long-Term Memory: Integrate with a database like Cosmos DB to remember user preferences and past interactions for a personalized experience.
* **Knowledge Retrieval via RAG:** Build a RAG pipeline over a curated knowledge base (e.g., card perks, lounge rules) to answer specific policy questions accurately using vector similarity search.

Ready to revolutionize travel planning for Banking International's premium clients? Let's get started! 🚀

Sign in to Azure and Monitor Costs
==================================

Launch the Azure Portal in your Udacity Classroom
-------------------------------------------------

You are given a _federated user account_, a temporary Azure user account with limited permissions, that you can use in this course.

To log in to the Azure Portal, click the **Cloud Resources** tab in your Udacity Classroom, then click on **Start Cloud Resource** and **Open Cloud Console** when the button is available. This will open the Azure Portal in a new browser tab, and may take a few moments to load the first time. Use the username, password, and Temporary Access Pass in the popup window to log into the Azure Portal.

If you have a pop-up blocker installed, it may prevent the new tab from launching. Please be sure to allow pop-ups from Udacity.
Important Points to Remember

----------------------------

#### **1. Session limit**

Note that there is a **session time limit**. If reached, you will automatically be timed out. As long as you have not used your entire budget, your work will be saved. You can re-launch using the same "Open Cloud Gateway" button in the left navigation menu to return to your session.

**2. Default Azure Resource Group**

A Resource Group will already be created for you. _You will not be able to create new Resource Groups._ When you are creating resources, choose the default Resource Group from the dropdown or identify the name of it through the portal first for use in PowerShell commands.

#### 3. Choosing Azure regions when creating resources

When creating a resource, choose the Azure region closest to you.

#### 4. Budget allocated for you

All Azure services are a pay-as-you-go service. Udacity has set a budget for each student to complete their course work. Please understand that these credits are limited and available for you to use judiciously. **The budget for this course is $25 for you.** Although, we find about $20 sufficient for most to complete this course.

#### **5. Shut down your resources | No extra credits**

We recommend you **shut down/delete every Azure resource** (e.g. virtual machines, storage, databases, machine learning workspaces, app services, bots, SQL Servers, etc.) immediately after the usage or if you are stepping away for a few hours. Otherwise, you will run out of your allocated budget. **Udacity will not provide additional credits.** In case you exhaust your credits:

* **You will lose your progress on the Azure Portal.**
* **You will have to use your personal Azure account to finish the remaining coursework.** Even if you are in the middle of the project/exercise and need to step away, you must shut down your resources. You can re-instantiate them later. To better understand pricing, see the [Azure Pricing(opens in a new tab)](https://azure.microsoft.com/en-us/pricing/calculator/) for all available services.

> For reference, any service available to you @$0.1/hour or higher should be monitored closely and shut down immediately after use or if you are stepping away.

![Check the pricing at https://azure.microsoft.com/en-us/pricing/calculator/ explained above](https://video.udacity-data.com/topher/2022/March/622916a8_screen-shot-2022-03-09-at-2.54.23-pm/screen-shot-2022-03-09-at-2.54.23-pm.png)

Check the pricing with the [Azure Price Calculator(opens in a new tab)](https://azure.microsoft.com/en-us/pricing/calculator/)

#### 6. Tracking your usage

The Cloud Resources tab provides you a convenient interface to track your budget. The budget that you have remaining in your account will be provided there.

> **Note** -  
> As you are given a temporary Azure user account with **limited** permissions, you might not be able to avail **all** Azure services. We have allowed the necessary ones only. If you see a few warning messages related to insufficient permissions, you can ignore them and proceed with your practice.

### Question 1 of 2

Select all of the true statements about Azure usage.

* [ ] Any service at $0.1/hour or higher should be monitored closely and shut down immediately after use to avoid exhausting your budget

* [ ] All progress on the Azure Portal will be saved even if you exhaust your budget

* [ ] Most students have completed the course using about $20 from their budget

* [ ] You will have to work with your personal Azure account to finish the program if you exhaust your budget

* [ ] You can track your monthly usage of credits within the Azure Cost and Billing Blade in the Azure Portal
  
  

### Question 2 of 2

Will you be able to create Resource Groups in your temporary Azure Account?

- [ ] Yes

- [ ] No
  
  

Environment Setup
Technical Requirements
=================

Before you begin, ensure you have access to the following technologies.

### Core Python Libraries

* `semantic-kernel`: Core framework for AI orchestration.
* `pydantic`: For data validation and creating structured outputs.
* `azure-identity`: Handles secure authentication to Azure.
* `azure-cosmos`: Client library for the Cosmos DB vector store.
* `requests`: For any direct web requests made by tools.
* `python-dotenv`: Manages local environment variables from a `.env` file.
* `azure-ai-projects`: Required for interacting with Azure AI Agent features like Bing grounding.

### Azure Services

* Azure OpenAI: Requires an endpoint with a chat model (e.g., `gpt-4o-mini`) and an embedding model (e.g., `text-embedding-3-small`).
* Azure Cosmos DB: Used as the vector database for memory and RAG.
* Azure AI Project: Required for the Bing Search grounding feature.

Local Machine Instructions
--------------------------

Follow these steps to configure the project locally. You'll need **Python 3.10+** installed.

### Step 1: Set Up Your Project

Create a new project directory, set up and activate a virtual environment, and download the starter project files into it.

### Step 2: Install Dependencies

Create a `requirements.txt` file in your project directory with the contents below, then run `pip install -r requirements.txt`.

`# Core dependencies python-dotenv requests pydantic tiktoken  # Azure services azure-identity azure-cosmos azure-ai-projects # Semantic Kernel semantic-kernel # Testing pytest`

### Step 3: Configure Credentials

Create a `.env` file in your project root to securely store your Azure credentials.

`# Azure OpenAI AZURE_OPENAI_ENDPOINT="YOUR_AZURE_OPENAI_ENDPOINT" AZURE_OPENAI_KEY="YOUR_AZURE_OPENAI_KEY" AZURE_OPENAI_API_VERSION="2024-02-15-preview" AZURE_OPENAI_CHAT_DEPLOYMENT="gpt-4o-mini" AZURE_OPENAI_EMBED_DEPLOYMENT="text-embedding-3-small" # Azure Cosmos DB COSMOS_ENDPOINT="YOUR_COSMOS_DB_ENDPOINT" COSMOS_KEY="YOUR_COSMOS_DB_KEY" COSMOS_DB="ragdb" COSMOS_CONTAINER="snippets" COSMOS_PARTITION_KEY="/pk" # Azure AI Project (for Bing Search) PROJECT_ENDPOINT="YOUR_AZURE_AI_PROJECT_ENDPOINT" AGENT_ID="YOUR_AGENT_ID" BING_CONNECTION_ID="YOUR_BING_CONNECTION_ID" BING_KEY="YOUR_BING_SEARCH_API_KEY"`




## Recommended Reading (Optional)

* [What Does a Travel Planner Do | Trip Planning Guide(opens in a new tab)](https://www.google.com/search?q=https://www.tripit.com/web/blog/trip-planning/what-does-a-travel-planner-do.html)
* [10 Things to Consider When Booking a Hotel(opens in a new tab)](https://www.google.com/search?q=https://www.smartertravel.com/10-things-to-consider-when-booking-a-hotel/)
* [10 Things to Consider When Booking a Flight](https://www.google.com/search?q=https://www.smartertravel.com/10-things-consider-when-booking-flight/)
  
  

Instructions
============

Project Instructions
--------------------

### Step 1: Understand the System Architecture

Begin by understanding the architecture of the AI Travel Concierge. Unlike a simple chatbot, this agent operates using a structured workflow to handle complex tasks. The core of this system is an **explicit state machine** that guides the conversation through distinct phases: Clarifying user needs, Planning which tools to use, Executing those tools, Analyzing the results, Resolving any issues, and Producing a final, structured output.

Your agent will be supported by several key components:

* **Orchestrator:** A state machine you will build in Python to control the agent's logic and workflow.
* **Tools (SK Plugins):** Functions that allow the agent to interact with external data sources like web search, weather APIs, and currency converters.
* **Memory:** A dual system comprising short-term `ShortTermMemory` for conversation context and long-term memory in **Cosmos DB** to store user preferences.
* **Knowledge Base (RAG):** A vector database containing specific information (e.g., credit card perks, lounge rules) that the agent can query to answer specific questions.

### Step 2: Set Up Your Environment & Review Starter Code

Carefully examine the provided starter code in your workspace. This scaffolding includes essential initializations for the Semantic Kernel, Pydantic models for structured outputs (`TripPlan`, `Weather`, etc.), state management (`AgentState`), and stubs for the required Python classes.

First, ensure your environment is correctly configured by running the health check:

`cd project/starter python -m app.scripts.system_check`

You should see all green checkmarks (✅) indicating the system is healthy.

Spend time reviewing the starter files. Understand how the `Kernel` is configured and how logging filters are added. Familiarize yourself with the Pydantic models, as you will use them to ensure your agent produces reliable, validated JSON outputs.

### Step 3: Implement the Core Agent Components

With your environment ready, begin implementing the agent's core capabilities.

* **Set Up the Semantic Kernel:** In `app/main.py`, implement the `create_kernel()` function to:
  * Create a `Kernel` instance
  * Add `AzureChatCompletion` and `AzureTextEmbedding` services using environment variables
  * Register all tool plugins (`WeatherTools`, `FxTools`, `SearchTools`, `CardTools`, `KnowledgeTools`)
* **Write the System Prompt:** In `app/main.py`, complete the `system_message` prompt to instruct the agent on:
  * Its role as a travel concierge
  * Available tools and when to use them
  * Output format matching the `TripPlan` Pydantic model
  * Anti-hallucination rules (use null/N/A for missing data)
* **Implement Tools (SK Plugins):** Flesh out the provided Python classes to create functional tools. Use the `@kernel_function` decorator for each method. You will need to implement: Register these plugins with the Semantic Kernel so the orchestrator can call them.
  * `WeatherTools` to get weather data for a given location.
  * `FxTools` to convert currencies.
  * `SearchTools` to perform web searches via Azure AI Agent with Bing grounding.
  * `CardTools` to recommend credit cards based on internal rules.
  * `KnowledgeTools` to retrieve information from the RAG knowledge base.
* **Implement Memory Systems:**
  * **Short-Term Memory:** In `app/memory.py`, implement the `ShortTermMemory` class methods: * `add_conversation()` - Add user/assistant messages to memory * `_evict_if_needed()` - Implement sliding window eviction when limits are exceeded * `get_conversation_history()` - Retrieve conversation history for context
    * **Long-Term Memory:** In `app/long_term_memory/core.py`, implement:
      * `add_memory()` - Create MemoryItem and insert into Cosmos DB
      * `get_memory()` - Read memory and update access stats

### Step 4: Build the Orchestration and RAG Logic

Now, bring the agent to life by implementing its main control flow and reasoning capabilities.

* **Build the State Machine:** In `app/state.py`, implement the `AgentState` class methods:
  * `advance()` - Progress through the 8 phases (Init → ClarifyRequirements → PlanTools → ExecuteTools → AnalyzeResults → ResolveIssues → ProduceStructuredOutput → Done)
  * `reset()` - Reset state to initial values for a new session
* **Implement the RAG Pipeline:**
  1. **Ingestion:** In `app/rag/ingest.py`, implement:
     * `embed_texts()` - Generate embeddings using Semantic Kernel's `AzureTextEmbedding`
     * `upsert_snippet()` - Store documents with embeddings in Cosmos DB
  2. **Retrieval:** In `app/rag/retriever.py`, implement:
     * Generate query embedding using `embed_texts()`
     * Execute `VectorDistance` query against Cosmos DB for similarity search
  3. **Agentic Loop:** The LLM automatically decides which tools to call using `FunctionChoiceBehavior.Auto()`. It can call multiple tools in sequence and combine their results into a coherent response.

### Step 5: Test and Evaluate Your Implementation

Thoroughly test your AI agent to ensure all components work together correctly and produce high-quality responses. Use the provided testing suite and interactive demo.

* **Run Unit Tests:** Execute the full suite of unit tests to verify the functionality of individual components.

`python -m pytest tests/ -v`

Ensure all tests are passing.

* **Interactive Chat Demo:** Launch the interactive chat interface to test the end-to-end workflow with your own queries.

`python chat.py`

Try queries like:

  `* I want to go to Paris from 2026-06-01 to 2026-06-08 with my BankGold card  * I want to visit Tokyo from July 10-17 with my BankPlatinum card  * Plan a trip to Barcelona next month. I have a BankRewards card - what perks can I use?`

* **Run the Evaluation Harness:** Use the provided harness to systematically measure your agent's performance. This tool uses an "LLM-as-judge" pattern to score the agent against a rubric, aggregating metrics like answer quality, JSON validity, tool usage, and latency.

`python -m app.eval.judge`

### Step 6: Prepare Your Submission

After implementing and testing your system, prepare your final submission. Ensure you have completed all the required components and that your code is clean and well-documented.

Your final submission must include:

* **Your completed Python agent implementation**, including all tools, the state machine, memory integrations, and the RAG pipeline.
* **Your LLM judge evaluation script** (`app/eval/judge.py`) with numerical scoring output.
* **Required screenshots:**
  * Azure OpenAI Deployments page showing chat and embedding deployments
  * Cosmos DB Data Explorer showing database, container, and stored items
  * Azure AI Studio showing Bing search connection
  * Console output showing state transitions during agent execution
  * Console output showing RAG retrieval with VectorDistance scores
  * LLM judge numerical score output

Ensure that you check the project rubric to understand the requirements for the different parts of the project before submitting it. Your submission will be reviewed against the project rubric
Expected Outcome: Example Interaction

-------------------------------------

This walkthrough demonstrates the agent's ideal execution flow from user query to final output. It serves as a reference for what your agent should be able to do.

### Sample Chat Session

`🚀 Travel Agent Chat Interface ================================================== Welcome! I'm your AI travel concierge. Tell me about your travel plans and I'll help you plan your trip! Commands:   help    - Show this help message  status  - Show system status  clear   - Clear the screen  quit    - Exit the chat 💬 You: I'm planning a trip to Paris from Sept 1st to Sept 8th. I have a BankGold card and want to know which restaurants to visit. Also, what's the weather like and should I use my card there? 🤖 Agent: Let me help you plan your trip... ============================================================ 🎯 TRAVEL PLAN ============================================================ 📍 Destination: Paris 📅 Travel Dates: Sept 1st to Sept 8th ✅ Response validated with Pydantic 🌤️  WEATHER ------------------------------ Temperature: 15°C Conditions: partly cloudy Recommendation: Good for outdoor dining 🔍 SEARCH RESULTS ------------------------------ 1. 🍽️ Le Comptoir du Relais    Classic French bistro in Saint-Germain    🔗 https://example.com/le-comptoir    ⭐ Rating: 4.8/5    💰 Price: $$$ 2. 🍽️ Frenchie    Modern French cuisine in the 2nd arrondissement   🔗 https://example.com/frenchie    ⭐ Rating: 4.9/5    💰 Price: $$$$ 💳 CARD RECOMMENDATION ------------------------------ Card: BankGold Benefit: 4x points on dining worldwide FX Fee: None 💰 CURRENCY INFO ------------------------------ Sample Meal (USD): $100 Sample Meal (EUR): €92 Exchange Rate: 1 USD = 0.92 EUR Points Earned: 400 📋 NEXT STEPS ------------------------------ 1. Book restaurant reservations 2. Notify bank of travel dates 3. Pack for 15°C weather 📚 SOURCES ------------------------------ 1. https://example.com/le-comptoir 2. https://example.com/frenchie ============================================================ 💬 You: quit 👋 Goodbye! Safe travels!`

### How It Works Behind the Scenes

1. **User Input**: You type your travel query
2. **Tool Execution**: The LLM automatically decides which tools to call:
   * `get_weather("Paris")` → Returns temperature and conditions
   * `web_search("restaurants in Paris")` → Returns restaurant results from Bing
   * `search_knowledge("BankGold dining benefits")` → Returns card perks from knowledge base
   * `convert_fx(100, "USD", "EUR")` → Returns currency conversion
3. **Synthesis**: LLM combines all tool results into a structured JSON response
4. **Validation**: Response is validated against the `TripPlan` Pydantic model
5. **Display**: The `chat.py` script formats and displays the results

### Step 6: Prepare Your Submission

After implementing and testing your system, prepare your final submission. Ensure you have completed all the required components and that your code is clean and well-documented.

Your final submission must include:

* **Your completed Python agent implementation**, including all tools, the state machine, memory integrations, and the RAG pipeline.
* **Your evaluation harness script** used to test the agent's performance.
* **(Optional)** Deployment to an Azure runtime with managed identity and observability.

Ensure that you check the project rubric to understand the requirements for the different parts of the project before submitting it. Your submission will be reviewed against the project rubric.

Rubric
======

Use this project rubric to understand and assess the project criteria.
Agent Architecture & External Service Integration

-------------------------------------------------

| Criteria                                           | Submission Requirements                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| -------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Configure cloud services for agent infrastructure  | The submission includes configuration of all necessary Azure services for the agent system.<br><br>* Three screenshots from Azure Portal:<br>* Azure OpenAI Deployments page showing chat deployment (gpt-4o-mini) and embedding deployment (text-embedding-3-small) with "Succeeded" status visible<br>* Cosmos DB Data Explorer showing database and container configured for agent memory storage with appropriate partition key, and at least one stored data item visible - Azure AI Studio showing semantic search connection with status as "Active" and credentials configured                                                                                              |
| Build agentic orchestration using Semantic Kernel  | The submission contains Python code that initializes the Semantic Kernel and connects it to Azure OpenAI service for agent orchestration.<br><br>* The Python code includes a function for setting up the Semantic Kernel (typically in `app/main.py`).<br>* The code creates an instance of the Kernel object.<br>* The kernel is configured by adding both `AzureChatCompletion` and `AzureTextEmbedding services`.<br>* The service configuration uses Azure OpenAI endpoints and API keys from environment variables.                                                                                                                                                           |
| Implement agent tools with Semantic Kernel plugins | The submission defines at least two Semantic Kernel plugins as agent tools, where each plugin integrates with a different external API.<br><br>* At least two separate plugin classes are implemented with `@kernel_function` decorators.<br>* Each decorated method makes HTTP requests to external APIs (weather service, currency exchange, web search, etc.).<br>* Methods demonstrate error handling or graceful failure responses (e.g., try-except blocks or error return values).<br>* Plugins are registered in the kernel using `kernel.add_plugin()`.<br>* Console output or test evidence demonstrates plugin invocation and data retrieval.                            |
| Structure agent responses using Pydantic models    | The submission contains Pydantic models that structure and validate agent outputs.<br><br>* Five models are defined: `Weather`, `SearchResult`, `CardRecommendation`, `CurrencyInfo`, and `TripPlan`.<br>* All models inherit from Pydantic's BaseModel with type hints and field definitions (required vs optional).<br>* Key recommendation models have required fields for card name, benefit description, fee information, and data source.<br>* Main response model has required fields for destination, travel dates, recommendations, and currency information.<br>* Pytest test suite passes with all tests validating model fields, types, and required field constraints. |

Agent Memory & State Management
-------------------------------

| Criteria                                                   | Submission Requirements                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Implement agent short-term memory for conversation context | The submission implements a short-term memory structure using a custom ShortTermMemory class for agent conversation tracking and context management.<br><br>* A `memory.py` file is included in the project.<br>* The file contains a `ShortTermMemory` class that manages conversation history using custom memory management<br>* The `ShortTermMemory` class is configured to track a history of at least three items via constructor parameters.<br>* The class includes methods for adding conversations, managing memory limits, and retrieving context windows.<br>* The implementation passes all 20 tests in the provided `pytest test_memory.py` test suite. |
| Integrate agent long-term memory with Cosmos DB            | The submission demonstrates Cosmos DB integration for agent long-term memory persistence using CosmosClient.<br><br>* Two screenshots: (1) Cosmos DB instance in Azure Portal, (2) upserted test item in the container.<br>* Methods in memory modules call `CosmosClient` from `azure.cosmos`.<br>* Credentials are passed via environment variables (not hardcoded).                                                                                                                                                                                                                                                                                                 |

Agent Core: Search State and RAG
--------------------------------

| Criteria                                           | Submission Requirements                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| -------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Implement agent state machine for query processing | The submission defines agent states and uses state management for tracking query processing data and metadata.<br><br>* A `state.py` file is included, defining the agent's possible states using an Enum (minimum: `Init`, `PlanTools`, `ExecuteTools`, `Done`).<br>* An `AgentState` class is implemented that initializes to `Init` and includes comprehensive data tracking capabilities.<br>* The `AgentState` class includes a fully implemented `advance()` method that progresses through the defined phases.<br>* The main application demonstrates usage of the `AgentState` class for tracking tools, sessions, and results.<br>* Screenshot demonstrates the agent moving through states during a query execution, showing console output or application logs with state transitions visible (e.g., initial state, progression through phases, final state) with timestamps or sequence indicators.                                                                                                                              |
| Build agent knowledge retrieval with RAG           | The submission uses an Azure embedding model to create and store vector embeddings in Cosmos DB for agent knowledge retrieval.<br><br>* The project code calls the Azure OpenAI embedding model configured in Azure to generate vectors from the knowledge base using Semantic Kernel's `AzureTextEmbedding` service.<br>* The RAG scripts (`ingest.py`, `retriever.py`) demonstrate embedding generation with `embedding_service.generate_embeddings()` calls.<br>* The retrieval functionality demonstrates vector similarity search using `VectorDistance` queries in Cosmos DB with cosine similarity scoring.<br>* A screenshot from the Azure Data Explorer is submitted, showing items in the vector store with visible embedding vectors (appearing as arrays or JSON arrays with numerical values).<br>* A screenshot of the Python console output is provided, showing retrieval results with: query embedding generated, `VectorDistance` query executed, results returned with similarity scores and retrieved document content. |
| Enable agent web search with Bing integration      | The submission integrates Bing Search as a Semantic Kernel plugin to extend agent search capabilities.<br><br>* A `search.py` file is included that defines a web search tool as a Semantic Kernel plugin.<br>* The tool is defined as a `@kernel_function` that integrates with Bing search.<br>* It uses the Azure AI Agent with Bing grounding via AIProjectClient and connection ID configuration.<br>* Environment variables are used for authentication (`PROJECT_ENDPOINT`, `AGENT_ID`, `BING_CONNECTION_ID`).<br>* Evidence of functional web search results: screenshot of console output or test results showing search query execution with returned results (title, URL, snippet).                                                                                                                                                                                                                                                                                                                                               |

Agent Evaluation
----------------

| Criteria                                              | Submission Requirements                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ----------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Implement agent performance evaluation with LLM judge | The submission includes an LLM judge to evaluate the agent's performance and provide a numerical score.<br><br>* A Python file (e.g., `judge.py` or `llm_judge.py`) is included that defines an LLM judge for agent evaluation.<br>* The judge uses evaluation criteria based on accuracy, completeness, relevance, and tool use to generate a quantitative output score.<br>* The judge produces a numerical score output (e.g., 0-5 scale or weighted overall score with individual criterion scores).<br>* Screenshot is submitted showing the numerical score output from the LLM judge evaluation. |
