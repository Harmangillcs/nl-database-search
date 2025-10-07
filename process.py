import pandas as pd
import pymysql
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    database='company_database'
)

depart_texts = ["Department: " + str(name) for name in pd.read_sql("SELECT name FROM departments", conn)["name"]]

emp_texts = [
    f"Employee: {row.name}, Dept: {row.department_name}, Email: {row.email}, Salary: {row.salary}"
    for row in pd.read_sql(
        "SELECT e.name, e.email, e.salary, d.name AS department_name FROM employees e LEFT JOIN departments d ON e.department_id = d.id", conn
    ).itertuples()
]

prod_texts = [
    f"Product: {row.name}, Price: {row.price}"
    for row in pd.read_sql("SELECT * FROM products", conn).itertuples()
]

order_texts = [
    f"Order: {row.id}, Customer: {row.customer_name}, Employee: {row.employee_name}, Total: {row.order_total}, Date: {row.order_date}"
    for row in pd.read_sql(
        "SELECT o.id, o.customer_name, o.order_total, o.order_date, e.name AS employee_name FROM orders o LEFT JOIN employees e ON o.employee_id = e.id", conn
    ).itertuples()
]

chunks = depart_texts + emp_texts + prod_texts + order_texts

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
faiss_store = FAISS.from_texts(chunks, embeddings)
faiss_store.save_local("Faissstore")
print("FAISS vector store saved!")

query = "Show me laptops under $1000"
for r in faiss_store.similarity_search(query, k=5):
    print(r.page_content)
