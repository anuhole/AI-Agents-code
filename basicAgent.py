from langchain.agents import create_agent
from langchain_groq import ChatGroq
from langchain_core.tools import tool 

@tool 
def get_weather(city: str) -> str:
    """Get the current weather for a city."""
    return f"IT is 28 C and sunny in {city}."

@tool
def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b

llm =ChatGroq(model="openai/gpt-oss-20b", temperature=0)

agent = create_agent(model=llm, tools=[get_weather,multiply],
                      system_prompt="You are a helpful assistant. use tools when needed.",)

result = agent.invoke(
    {"messages": [{"role": "user", "content": "my name is "}]}
)

print(result["messages"][-1].content)