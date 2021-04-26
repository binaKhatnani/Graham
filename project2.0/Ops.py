import os
from os import path
import json
import time
from kafka import KafkaProducer

class Ops():

  def __init__(self):
    self.operations = {}
    self.exec_plan = []
    self.ops_folder_path = path.join(os.getcwd(), "project2.0", "ops")

  def read_all_operations(self):
    for filename in os.listdir(self.ops_folder_path):
      ops_file = path.join(self.ops_folder_path, filename)
      with open(ops_file) as f:
        operation = json.loads(f.read())
        self.operations[str(operation['id'])] = operation   
        exec_plan = {
          'id': str(operation['id']), 
          'time': { 
            'nextexec': int(time.time()),
            'interval': operation['time']['interval']
          }
        }
        self.exec_plan.append(exec_plan)

  def write_operations_to_queue(self, python_selenium_instance, instruction):
    producer = KafkaProducer(bootstrap_servers="localhost:9092")
    producer.send(python_selenium_instance, instruction)
    producer.close()    

  def get_scheduled_operations(self):
    curr_time = int(time.time())
    exec_proc_list = []
    for plan in self.exec_plan:
      if plan['time']['nextexec'] < curr_time:
        exec_proc_list.append(self.operations[plan['id']])
        plan['time']['nextexec'] = curr_time + plan['time']['interval']
    return exec_proc_list

  def distribute_operations(self):
    for operation in self.get_scheduled_operations():
      enconded_operation = bytes(json.dumps(operation), encoding="utf-8")
      self.write_operations_to_queue("instruction", enconded_operation)


operations = Ops()
operations.read_all_operations()
while True:
  operations.distribute_operations()
  time.sleep(2)