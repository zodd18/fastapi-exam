from pymongo import MongoClient

client = MongoClient("mongodb+srv://uma:uma@uma.ixkiq.mongodb.net/geocaching?retryWrites=true&w=majority")

# Database name 
db = client.geocaching