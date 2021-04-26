from pymongo import MongoClient
import pymongo
import matplotlib.pyplot as plt
from datetime import datetime
import time


class Visualization():

  def __init__(self):
    conn = MongoClient("localhost", 27017)
    self.db = conn['prod']
    self.data = []

  def read_data_from_db(self):
    collection = self.db['fundamentals']
    read_data = collection.find()
    data = []
    for d in read_data:
      del d['_id']
      dateval  = d['datetime'][0:9]
      if d['datetime']:
        d['datetime'] = datetime.strptime(dateval, "%d-%b-%y")
      data.append(d)
    del data[-1]
    self.data = data

  def draw_graph_for_field_against_datetime(self, title, y_field, y_label, x_field, x_label):
    op = [float(d[y_field]) for d in self.data]
    dt = [d[x_field].strftime('%m/%d/%Y') for d in self.data]
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    ticks = []
    for index, v in enumerate(dt):
      if index % 20 == 0:
        ticks.append(index)
    plt.xticks(ticks)
    plt.plot(dt, op)
    fileName = y_field + '.png'
    plt.savefig(fileName)
    plt.close()


v = Visualization()
v.read_data_from_db()
v.draw_graph_for_field_against_datetime('Open prices for Asian Paints', 'open', 'Open', 'datetime', 'Date')
v.draw_graph_for_field_against_datetime('Closing prices for Asian Paints', 'close', 'Close', 'datetime', 'Date')
v.draw_graph_for_field_against_datetime('Daily High price for Asian Paints', 'high', 'High', 'datetime', 'Date')
v.draw_graph_for_field_against_datetime('Daily Low price for Asian Paints', 'low', 'Low', 'datetime', 'Date')
v.draw_graph_for_field_against_datetime('Daily Del to Trade ratio for Asian Paints', 'delToTrade', 'Del to Trade', 'datetime', 'Date')