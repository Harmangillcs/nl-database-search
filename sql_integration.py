from langchain_community.chat_models import ChatOpenAI
from langchain_experimental.sql import SQLDatabaseChain
from langchain.sql_database import SQLDatabase
from dotenv import load_dotenv

load_dotenv()  

db = SQLDatabase.from_uri("mysql+pymysql://root:root@localhost/company_database")

llm = ChatOpenAI(temperature=0, model_name="gpt-4")

db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)

user_query = "List all products with price less than 1000"
result = db_chain.run(user_query)

print(result)
