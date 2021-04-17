from pymongo import MongoClient
import pymongo

client = MongoClient('mongodb+srv://SKARANJA:FinalGroupAssignment@assignments.cttns.mongodb.net/assignment2?retryWrites=true&w=majority')
db = client.assignment
newscol = db.news
frequentcol = db.frequentwords

