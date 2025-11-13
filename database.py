import os
from sqlalchemy import create_engine, text, URL
from dotenv import load_dotenv

load_dotenv()

url_object = URL.create(
    "mysql+pymysql",
    username=os.getenv("USERNAME"),
    password=os.getenv("PASSWORD"),
    host=os.getenv("HOST"),
    port=os.getenv("PORT"),
    database=os.getenv("DATABASE"),
    query={"charset": "utf8mb4"},
)

connect_args = {
    "ssl": {"ca": os.getenv("CA_CERT_PATH")}
}

engine = create_engine(url_object, connect_args=connect_args)

# Test query
with engine.connect() as connection:
    result = connection.execute(text("SELECT * FROM jobs LIMIT 5"))
    result_dicts = []
    for row in result.all():
        result_dicts.append(dict(row._mapping))
        
    print(result_dicts)

def load_job_from_db(id):
     with engine.connect() as connection:
         result = connection.execute(
             text("SELECT * FROM jobs WHERE id = :val"),
             {"val": id}
         )
         rows = result.all()
         if len(rows) == 0:
              return None
         else:
              return dict(rows[0]._mapping)
    
