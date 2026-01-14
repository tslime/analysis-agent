from langchain_openai import AzureChatOpenAI
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent 

def load_llm(api_key,api_v,end_point,model,temp):
    
    #Load llm with langchain tools
    loaded_llm = AzureChatOpenAI(
    api_key=api_key,
    azure_endpoint=end_point,
    deployment_name=model,
    temperature=temp,
    streaming=False,
    api_version=api_v
    )

    return loaded_llm

def create_dataframe_agent(language_model,data_frame,agent_t):

    report_agent = create_pandas_dataframe_agent(
        language_model,
        data_frame,
        verbose=True,
        return_intermediate_steps=True,
        allow_dangerous_code=True,
        agent_type=agent_t
    )

    return report_agent

def run_agent(agent):

    while True:
        print("Prompt>> ",end="")
        q = input()
        answers = agent.invoke(q,handle_parsing_errors=True)
        print("Answer: ",answers["output"])
        print("\n")