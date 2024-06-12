from fastapi import FastAPI
from app.mongodb import MongoDBConnection

app = FastAPI()

def get_mongo_conection():
    connection = MongoDBConnection()
    try:
        yield connection
    finally:
        connection.close()

@app.get("/")
def read_root():
    return {"Hello": "World"}