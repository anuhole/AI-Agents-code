import os
from langchain.agents import create_agent
from langchain_groq import ChatGroq
from langchain_core.tools import tool


@tool
def save_java_file(filename: str, code: str) -> str:
    """Save Java test code to tests folder. Use this after writing the test class"""
    os.makedirs("tests", exist_ok=True)
    path = os.path.join("tests", os.path.basename(filename))
    with open(path, 'w') as file:
        file.write(code)
    return f"Java code saved to {path}"

llm=ChatGroq(model="openai/gpt-oss-20b", temperature=0)
agent=create_agent(
    model=llm,
    tools=[save_java_file],
    system_prompt=("You are a QA automation Engineer. You can generate Selenium test cases in Java using Junit5."
    "Use only the locators given by the user" 
    "write one complete test class, then save it with the given filename using the save_java_file tool. "
    "Reply with one line summary of the test created."
    ),
)

task = """
Generate a Selenium test class in Java for www.saucedemo.com login page.
Locators: username id=user-name, password id=password, login button id=login-button
error message css=[data-test='error'], inventory list class = inventory_list.
Test cases:
1. Valid login(standard_user / secret_sauce) shows the inventory list.
2. Wrong password shows an error message.
3. Empty username and passwords shows an error message.
Class name : LoginTests
"""

result=agent.invoke({"messages":[{"role":"user","content":task}]})
print(result["messages"][-1].content)
