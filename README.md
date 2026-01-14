# AI Data Analysis Agent

Conversational AI agent for statistical analysis of CSV datasets using natural language queries powered by Azure OpenAI and LangChain pandas agents.

## Features

- **Natural Language Queries**: Ask questions about data in plain English
- **Statistical Analysis**: Pandas-powered data operations and calculations
- **Interactive CLI**: Simple command-line chat interface
- **Flexible Datasets**: Works with any CSV file (can be extendede to other files)

## Prerequisites

- Python 3.8+
- Azure OpenAI API access key (or adapt the llm laoding function to model you have API key for.)
- CSV dataset

## Installation

```bash
# Clone repository
git clone https://github.com/tslime/ai-data-analysis-agent.git
cd ai-data-analysis-agent

# Install dependencies
pip install langchain langchain-openai langchain-experimental pandas python-dotenv

# Create . env file
echo "API_KEY=your_azure_openai_api_key" > .env

# Add your CSV dataset
# Place CSV file in data/ directory
```

## Project Structure

```
.
├── analysis-agent.py              # Main application
├── utilities/
│   └── AnalysisAgentUtilities.py  # Helper functions
├── data/
│   └── your_dataset.csv           # CSV dataset (not committed)
├── .env                           # API key (not committed)
└── README.md
```

## Usage

```bash
python analysis-agent.py
```

**Example questions:**
```
Prompt>> What is the average price? 
Prompt>> Show me the highest value and when it occurred
Prompt>> Calculate the correlation between volume and price
Prompt>> Find outliers in the dataset
```

Press `Ctrl+C` to quit.

## Architecture

### Main Application (`analysis-agent.py`)
- Loads configuration and environment variables
- Initializes LLM and dataframe agent
- Runs interactive chat loop

### Utilities Module (`utilities/AnalysisAgentUtilities. py`)

**Four core functions:**

| Function | Purpose |
|----------|---------|
| `extract_csv_data(csv_file_path)` | Loads CSV into pandas DataFrame |
| `load_llm(api_key, api_v, end_point, model, temp)` | Initializes Azure OpenAI model |
| `create_dataframe_agent(llm, df, agent_type)` | Creates pandas analysis agent |
| `run_agent(agent)` | Runs interactive query loop |

## Configuration

Update in `analysis-agent.py`:

```python
# Model settings
model_id = "gpt-4o-mini"
temperature = 0

# Azure endpoint
end_p = "https://your-resource.cognitiveservices.azure.com/"

# Dataset path
df = extract_csv_data("data/your_dataset.csv")
```

## Example Dataset

**Bitcoin USD 1-minute historical data** included as example:
- Download from [Kaggle](https://www.kaggle.com/datasets/mczielinski/bitcoin-historical-data)
- Place in `data/btcusd_1-min_data.csv`

**Works with any CSV containing numerical data.**

## Security Notes

Uses `allow_dangerous_code=True` for pandas operations
- Only use with trusted datasets
- Never commit `.env` file
- Review agent output in verbose mode

## Technologies

- **LangChain**: Agent framework
- **Azure OpenAI**: GPT-4o-mini
- **Pandas**: Data analysis
- **Python-dotenv**: Environment management

## Troubleshooting

| Issue | Solution |
|-------|----------|
| `FileNotFoundError` | Check CSV file path in `data/` directory |
| `AuthenticationError` | Verify `API_KEY` in `.env` file |
| `ModuleNotFoundError` | Run from project root directory |

