import csv
import os
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

mentors = collection.find({"mentor": True, "isAssigned": { "$ne": True}})
mentees = collection.find({"mentor": False, "isAssigned": { "$ne": True}})

filtered_mentees = [mentee for mentee in mentees if not mentee.get("isAssigned", False)]

headers = ["first name", "last name", "email", "role", "organisation", "grade", "profession"]

with open("./mentoring-data/mentors.csv", "w", newline="") as mentors_file:
    writer = csv.writer(mentors_file)
    writer.writerow(headers)
    for mentor in mentors:
        name = mentor.get("name","")
        first_name, last_name = name.split(" ", 1) if name else ("", "")
        writer.writerow([first_name, last_name, mentor.get("email"),
                         mentor.get("industry"), mentor.get("organisation"), mentor.get("proficiency"), mentor.get("role")])

with open("./mentoring-data/mentees.csv", "w", newline="") as mentees_file:
        writer = csv.writer(mentees_file)
        writer.writerow(headers)
        for mentee in filtered_mentees:
            name = mentee.get("name","")
            first_name, last_name = name.split(" ", 1) if name else ("", "")
            writer.writerow([first_name, last_name, mentee.get("email"),
                            mentee.get("industry"), mentee.get("organisation"), mentee.get("proficiency"), mentee.get("role")])
