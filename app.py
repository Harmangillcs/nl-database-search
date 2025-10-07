import streamlit as st
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain_experimental.sql import SQLDatabaseChain
from langchain.sql_database import SQLDatabase
from dotenv import load_dotenv
load_dotenv()

#load vectorstores
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
faiss_store = FAISS.load_local("Faissstore", embeddings, allow_dangerous_deserialization=True)

#load sql
db = SQLDatabase.from_uri("mysql+pymysql://root:root@localhost/company_database")
llm = ChatOpenAI(temperature=0, model_name="gpt-4")
db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=False)

st.title("Natural Language Search for Company DB")

user_input = st.text_input("Ask a question:")

if st.button("Search"):
    
    vector_results = faiss_store.similarity_search(user_input, k=3)
    st.subheader("Vector Search Results:")
    for r in vector_results:
        st.write(r.page_content)
    
    
    sql_result = db_chain.run(user_input)
    st.subheader("SQL Search Results:")
    st.write(sql_result)
