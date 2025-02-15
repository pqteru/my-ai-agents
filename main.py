import tools
import dotenv
import os
from smolagents import (
    CodeAgent,
    ToolCallingAgent,
    DuckDuckGoSearchTool,
    LiteLLMModel,
    GradioUI,
)

dotenv.load_dotenv()
    
model = LiteLLMModel(
    model_id="ollama/deepseek-r1:7b",
    api_base="http://localhost:11434",
    api_key="ollama", # 使用 local model 的話隨意填寫
    num_ctx=4096,  # 確保這個數值被支援
    max_tokens=512,
)

web_agent = ToolCallingAgent(
    tools=[DuckDuckGoSearchTool(), tools.visit_webpage],  # 修正 tools 調用
    model=model,
    name="search",
    description="Runs web searches for you. Give it your query as an argument.",
)

manager_agent = CodeAgent(
    tools=[],  # 這裡可以加上數據分析相關工具
    model=model,
    managed_agents=[web_agent],
    additional_authorized_imports=[
        "random", "re", "request", "bs4", "crawl4ai", "time", "unicodedata", "queue", "numpy",
        "datetime", "math", "pandas", "collections", "stat", "itertools", "statistics"
    ],
)

# using GradioUI to launch the agent
# GradioUI(manager_agent).launch()

# using bash command
answer = manager_agent.run("Randomly pick 5 stocks from S&P500, separated by commas, no code provided, text answer only.")

print(answer)
