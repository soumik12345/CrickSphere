import pymongo
import streamlit as st
from .secret import MONGO_SECRET


# @st.cache
def load_data(db, collection, query):
    client = pymongo.MongoClient(MONGO_SECRET)
    database = client[db]
    collection = database[collection]
    result = []
    for x in collection.find(query):
        result.append(x)
    return result
