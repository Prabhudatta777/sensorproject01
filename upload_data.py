from pymongo.mongo_client import MongoClient
import pandas as pd
import json

uri = "mongodb+srv://Ruhan369:txlVQAjgrihn14DV@cluster0.twkxbad.mongodb.net/?appName=Cluster0"

client = MongoClient(uri)

DATABASE_NAME="pwskills"
COLLECTION_NAME='waferfault'

df = pd.read_csv(r"C:\Users\prabh\Downloads\sensorproject\notebooks\wafer_23012020_041211.csv")

df=df.drop("Unnamed: 0",axis=1)

json_record = list(json.loads(df.T.to_json()).values())

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)