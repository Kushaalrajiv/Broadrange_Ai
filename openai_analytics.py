# Install the necessary libraries for OpenAI
#!pip install pandasai llm openai

# Import the required classes and libraries
import pandas as pd
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI

# Instantiate the OpenAI LLM
OPENAI_API_KEY = "YOUR OPENAI API KEY"      #Caution: Should be kept "Secret" from public (github)
llm = OpenAI(api_token=OPENAI_API_KEY)

# Custom PandasAI class for interacting with OpenAI
class MyPandasAI(PandasAI):
    def chat(self, df, prompt):
        # Get the answer from the OpenAI API
        answer = self.llm.chat(prompt)
        # Return the answer
        return answer

# Create a DataFrame using Pandas - Sample Data
data_dict = {
    "company_name": ["ABC Corp", "XYZ Inc", "123 Enterprises"],
    "company_id": [1, 2, 3],
    "compliant_status": [True, False, True],
    "created_datetime": ["2023-01-01 10:00:00", "2023-02-15 08:30:00", "2023-03-20 14:45:00"],
    "updated_datetime": ["2023-05-10 12:00:00", "2023-06-18 09:20:00", "2023-07-25 16:30:00"]
}
df = pd.DataFrame(data_dict)

# Instantiate the custom PandasAI class
pandas_ai = MyPandasAI(llm)

# Utilize PandasAI with OpenAI for AI analytics
pandas_ai.chat(df, "What is the total number of companies in the ledger?")
pandas_ai.chat(df, "How many companies are compliant?")
# Ask other relevant questions for analytics
# pandas_ai.chat(df, "What is the major reason for incompliance?")

"""
PANDAS-AI CODE

# Install the PandasAI library
#!pip install pandasai

# Import the PandasAI library
from pandasai import PandasAI

# Instantiate PandasAI
pandasai = PandasAI()

# Utilize PandasAI for AI analytics
# Interact with the Pandas DataFrame 'ledger_df' to obtain AI-generated insights
pandasai.chat(ledger_df, "What is the total number of companies in the ledger?")
pandasai.chat(ledger_df, "How many companies are compliant?")
# Ask other relevant questions for analytics

"""
