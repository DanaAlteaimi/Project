from chromadb import Client
from chromadb.config import Settings  
from chromadb import PersistentClient

client = PersistentClient(path="./")

collections = client.list_collections()
print([c.name for c in collections])

