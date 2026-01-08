# Statistical Analysis Agent

A Python-based conversational agent that performs statistical analysis on data sets. Bitcoin historical price data set (1-minute intervals) from kaggle is used here for querying. But other data sets can also be used.

## Overview

This application allows users to ask natural language questions about Bitcoin USD pricing data and receive intelligent statistical analysis powered by GPT-4o-mini and pandas dataframe agents. 

## Features

- **Statistical Analysis**: Query Bitcoin 1-minute interval data using natural language
- **AI-Powered**: Uses Azure OpenAI GPT-4o-mini for intelligent responses
- **Pandas Integration**: LangChain pandas dataframe agent for data operations
- **Interactive Chat**: Simple command-line interface for questions
- **Real-time Analysis**: Analyze high-frequency Bitcoin price data

## Prerequisites

- Python 3.8+
- Azure OpenAI API access
- Bitcoin 1-minute historical data from Kaggle

## Installation

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd <your-repo-name>
```

2. **Install dependencies**
```bash
pip install langchain langchain-openai langchain-experimental pandas python-dotenv
```

3. **Set up environment variables**

Create a `.env` file in the root directory: 
```env
API_KEY=your_azure_openai_api_key_here
```

4. **Download the dataset**

Download the Bitcoin USD 1-minute data from [Kaggle](https://www.kaggle.com/datasets/mczielinski/bitcoin-historical-data) and place it in the `data/` directory:
```
data/btcusd_1-min_data.csv
```

## Usage

Run the program:
```bash
python main.py
```

Ask questions about the Bitcoin data: 
```
Prompt>> What is the average Bitcoin price? 
Prompt>> Show me the highest price in the dataset
Prompt>> What's the trading volume trend?
Prompt>> Calculate the price volatility
```

Press Ctrl+C to quit.

## Example Questions

- "What is the average Bitcoin price in the dataset?"
- "What was the maximum price and when did it occur?"
- "Calculate the standard deviation of prices"
- "Show me statistics for the last 1000 entries"
- "What's the correlation between volume and price?"
- "Find the largest price spike in a single minute"

## Project Structure

```
. 
├── main.py                      # Main application file
├── . env                         # Environment variables (not committed)
├── data/
│   └── btcusd_1-min_data.csv   # Bitcoin 1-min dataset (not committed)
├── .gitignore                  # Git ignore file
└── README.md                   # This file
```

## Technologies Used

- **LangChain**:  Agent framework and orchestration
- **LangChain Experimental**:  Pandas dataframe agent
- **Azure OpenAI**: GPT-4o-mini language model
- **Pandas**: Data manipulation and analysis
- **Python-dotenv**: Environment variable management

## Configuration

The agent is configured with:
- **Model**: GPT-4o-mini
- **Temperature**: 0 (deterministic responses)
- **Streaming**: Disabled
- **API Version**: 2025-01-01-preview
- **Verbose Mode**: Enabled (shows agent reasoning)

## Security Notes

This agent uses `allow_dangerous_code=True` to execute Python code for data analysis. Only use with trusted data sources. 

- Never commit your `.env` file with API keys
- Keep your Azure OpenAI API credentials secure
- Review generated code in verbose output
- Only use with trusted datasets

## Dataset Information

This project uses Bitcoin USD historical data with 1-minute interval pricing.  The dataset typically includes:
- Timestamp
- Open, High, Low, Close prices
- Volume (BTC)
- Volume (USD)
- Weighted Price

**Source**: [Kaggle - Bitcoin Historical Data](https://www.kaggle.com/datasets/mczielinski/bitcoin-historical-data)

## Troubleshooting

**Issue**: `FileNotFoundError: data/btcusd_1-min_data.csv`
- **Solution**: Download the dataset from Kaggle and place it in the `data/` directory

**Issue**: `AuthenticationError`
- **Solution**: Check your `.env` file and ensure `API_KEY` is set correctly

**Issue**: Agent not responding
- **Solution**: Check your Azure OpenAI endpoint and deployment name match your Azure configuration

## License

MIT License

## Acknowledgments

- Bitcoin dataset from Kaggle
- Powered by Azure OpenAI and LangChain
- Built with LangChain Experimental Agents