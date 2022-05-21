import os
import pymongo

mongo_client = pymongo.MongoClient(
    os.environ.get('MONGODB_HOST'),
    username=os.environ.get('MONGODB_USER'),
    password=os.environ.get('MONGODB_PASSWORD'),
    authSource=os.environ.get('MONGODB_AUTHSOURCE', 'rms')
)
