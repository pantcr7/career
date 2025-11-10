import sqlalchemy
from sqlalchemy import create_engine, URL
from dotenv import load_dotenv

import os


load_dotenv()

url_object = URL.create(
    "mysql+pymysql",
    username=os.getenv("USERNAME"),
    password=os.getenv("PASSWORD"),
    host=os.getenv("HOST"),
    database=os.getenv("DATABASE"),
    query={"charset": "utf8mb4"},
  )

engine = create_engine(url_object)


