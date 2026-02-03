from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# Replace <db_password> with the actual password
uri = "mongodb+srv://1arpanchandra_db_user:Cosmos3D@cluster0.s2dx0c7.mongodb.net/?appName=Cluster0"


# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))


# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)