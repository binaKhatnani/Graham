from pymongo import MongoClient

class Database():

  def __init__(self, db):
    self.client = MongoClient('localhost', 27017)
    self.db = self.client[db]
    pass

  def write_one_to_collection(self, name, val):
    collection = self.db[name]
    collection.insert_one(val)

  def write_many_to_collection(self, name, values):
    collection = self.db[name]
    collection.insert_many(values)
