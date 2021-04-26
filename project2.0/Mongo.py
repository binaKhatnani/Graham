from pymongo import MongoClient
from kafka import KafkaConsumer
import json

class Mongo():

  def __init__(self):
    conn = MongoClient('localhost', 27017)
    self.db = conn['markets']
    self.data_channel = 'data'
    self.data = []
  
  def read_data_from_kafka(self):
    self.consumer = KafkaConsumer(bootstrap_servers="localhost:9092", consumer_timeout_ms=2000)
    self.consumer.subscribe(self.data_channel)
    for msg in self.consumer:
      self.data.append(json.loads(msg.value.decode('utf-8')))

  def write_to_db(self):
    for data in self.data:
      c_name = data['name']
      document = data['value']
      collection = self.db[c_name]
      collection.insert_one(document)
    self.data = []

# //create client

# //Create consumer

# //consumer subscribe
# //write to mongodb with topic name = collection name

db = Mongo()
while True:
  db.read_data_from_kafka()
  db.write_to_db()