from selenium import webdriver
from kafka import KafkaConsumer, KafkaProducer
import json
import os
from os import path
import time

class Driver():

  def __init__(self, path_to_driver, download_path):
    chrome_options = webdriver.ChromeOptions()
    prefs = {"download.default_directory" : download_path}
    chrome_options.add_experimental_option("prefs",prefs)
    self.chrome_options = chrome_options
    self.path_to_driver = path_to_driver
    self.instruction_channel = 'instruction'
    self.data_channel = 'data'
    self.instructions = []
    self.running = True
    self.retry_count = 5

  def _create_driver(self):
    self.driver = webdriver.Chrome(executable_path=self.path_to_driver, chrome_options=self.chrome_options)

  def read_instructions(self):
    self.consumer = KafkaConsumer(bootstrap_servers="localhost:9092", consumer_timeout_ms=2000)
    self.consumer.subscribe(self.instruction_channel)
    for msg in self.consumer:
      instructions = json.loads(msg.value.decode())
      self.instructions.append(instructions)
      print(instructions)

  def goto_page(self, page_link):
    self._create_driver()
    self.driver.get(page_link)

  def fill_field(self, field, value):
    # use the selenium method to fill a value to a field
    pass

  def _extract_value_by_xpath(self, xpath):
    cont = True
    count = 0
    while cont and count < self.retry_count:
      try:
        value = self.driver.find_elements_by_xpath(xpath)[0].text
        cont = False
      except:
        print('Not found' + xpath)
        time.sleep(1)
        count += 1
        pass
    return value
    

  def extract_values_to_json(self, fields, collection_name):
    collection = {
      "name": collection_name,
      "value": {}
    }
    for field in fields:
      value = self._extract_value_by_xpath(field['link'])
      collection["value"][field['key']] = value
    return collection

  def click_link(self, xpath):
    cont = True
    count = 0
    while cont and count < self.retry_count:
      try:
        self.driver.find_elements_by_xpath(xpath)[0]
        cont = False
      except:
        print('Not found' + xpath)
        time.sleep(1)
        count += 1 
        pass

  def exit(self):
    self.driver.quit()

  def write_collection_to_db(self, data):
    self.producer = KafkaProducer(bootstrap_servers="localhost:9092")
    encoded_data = bytes(json.dumps(data), encoding="utf-8")
    self.producer.send(self.data_channel, encoded_data)

  def execute_instructions(self):
    for procedures in self.instructions:
      for instruction in procedures['procedure']:
        cmd = instruction['cmd']
        if cmd == 'GOTO':
          link = instruction['link']
          self.goto_page(link)
        elif cmd == 'FILL':
          field = instruction['field']
          value = instruction['value']
          self.fill_field(field, value)
        elif cmd == 'EXTRACT':
          fields = instruction['fields']
          collection = instruction['collection']
          data = self.extract_values_to_json(fields, collection)
          self.write_collection_to_db(data)
        elif cmd == 'CLICK':
          link = instruction['link']
          self.click_link(link)
        elif cmd == 'EXIT':
          self.exit()
        print(cmd)
        time.sleep(5)
    self.instructions = []

  def continue_running(self):
    return self.running

chrome_path = path.join(os.getcwd(), 'project2.0', 'chromedriver.exe')
download_path = path.join(os.getcwd(), 'project2.0', 'download')
driver = Driver(chrome_path, download_path)
while driver.continue_running() == True:
  driver.read_instructions()
  driver.execute_instructions()
