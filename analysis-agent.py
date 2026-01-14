import os
import sys


from dotenv import load_dotenv
from utilities.AnalysisAgentUtilities import extract_csv_data, load_llm, create_dataframe_agent, run_agent 

load_dotenv()


#Model configs
credentials = os.getenv("API_KEY")
model_id = "gpt-4o-mini"
api_version = "2025-01-01-preview"
end_p = "https://gj491-mk2w3yrm-eastus2.cognitiveservices.azure.com/"
temperature = 0

#Prepare and run agent with data frame
df = extract_csv_data("data/btcusd_1-min_data.csv")
llm = load_llm(credentials,api_version,end_p,model_id,temperature)
analysis_agent = create_dataframe_agent(llm,df,"openai-tools")
run_agent(analysis_agent)
