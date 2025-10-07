# Natural Language Search Interface

This project is a simple natural language search interface for querying a MySQL database using **LangChain**, **FAISS**, and **Streamlit**.  

Users can type questions in plain English, and the system retrieves results from both structured database tables and unstructured text (like product names) using **hybrid search**.

---

## Features

- Natural language queries converted to SQL using **ChatOpenAI**.
- Vector search on product names using **FAISS embeddings**.
- Streamlit interface for easy user interaction.

---

## Setup

1. Clone the repository:
```bash
https://github.com/Harmangillcs/nl-database-search.git

```

2. Install all dependencies
```bash
pip install -r requirements.txt
```

3.Add your OpenAI API key in a .env file:
```bash
OPENAI_API_KEY=your_api_key_here
```

4.Save the vectorstores and run the query as testing
```bash
python process.py
```

6. Save and run SQL query using LLM Model
```bash
python sql_integration.py
```

7.Run streamlit app
```bash
streamlit run app.py
```
