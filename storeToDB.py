import csv
import os
import sys
import certifi
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

mongo_uri = os.getenv('MONGO_URI')
dbName = os.getenv('DB_NAME')
collectionName = os.getenv('COLLECTION_NAME')
client = MongoClient(mongo_uri, tlsCAFile=certifi.where())
db = client[dbName]
collection = db[collectionName]

if not os.path.exists('./mentoring-data/output/mentors-list.csv') or not os.path.exists('./mentoring-data/output/mentees-list.csv'):
    print('Files not found, so exiting')
    sys.exit(0)
# Read data from mentors-list.csv
with open("./mentoring-data/output/mentors-list.csv", "r") as mentors_file:
    reader = csv.DictReader(mentors_file)
    for row in reader:
        email = row.get("email")
        match_1_email = row.get("match 1 email")

        # Check if all fields of match 1 exist
        if match_1_email:
            # Update MongoDB data and set isAssigned flag to True
            query = {
                "email": email
            }
            update = {
                "$set": {
                    "isAssigned": True,
                    "mentee": {
                        "email": match_1_email
                    }
                }
            }
            collection.update_one(query, update)

with open("./mentoring-data/output/mentees-list.csv", "r") as mentees_file:
    reader = csv.DictReader(mentees_file)
    for row in reader:
        email = row.get("email")
        match_1_email = row.get("match 1 email")

        # Check if all fields of match 1 exist
        if match_1_email:
            # Update MongoDB data and set isAssigned flag to True
            query = {
                "email": email
            }
            update = {
                "$set": {
                    "isAssigned": True,
                    "mentor": {
                        "email": match_1_email
                    }
                }
            }
            collection.update_one(query, update)

client.close()
