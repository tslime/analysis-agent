import os
import sys
import pandas as pd

from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent 


load_dotenv()



#Model config
credentials = os.getenv("API_KEY")
model_id = "gpt-4o-mini"
parameters = {
    "temperature": 0
}



#Load llm with langchain tools
llm = AzureChatOpenAI(
    api_key=credentials,
    azure_endpoint="https://gj491-mk2w3yrm-eastus2.cognitiveservices.azure.com/",
    deployment_name=model_id,
    temperature=parameters["temperature"],
    streaming=False,
    api_version="2025-01-01-preview"
    )

df = pd.read_csv("data/btcusd_1-min_data.csv")


report_agent = create_pandas_dataframe_agent(
    llm,
    df,
    verbose=True,
    return_intermediate_steps=True,
    allow_dangerous_code=True,
    agent_type="openai-tools"
    )

"""
response = report_agent.invoke("Create a line plot showing the closing price over time")
print(response["output"])
"""

while True:
    print("Prompt>> ",end="")
    q = input()
    answers = report_agent.invoke(q,handle_parsing_errors=True)
    print("Answer: ",answers["output"])
    print("\n")