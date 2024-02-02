
# Natural Language Database Queries Using Google Gemini


This project utilizes Google's Gemini natural language processing to convert user-provided natural language questions into SQL queries. The system then executes these queries on an SQLite database, returning relevant results to the user. The goal is to streamline the process of retrieving information from databases by eliminating the need for users to manually construct SQL queries, making data retrieval more user-friendly and accessible.


## Usage

1 . Create virtual environment in your directory.

2 . Clone the repo.

2 . Install requirements using : 

    pip install -r requirements.txt

3 . Create .env file and add your Gemini api key to it.

4 . Run sqllm.py using :

    streamlit run .\sqllm.py