import os
import pandas as pd

class MainData():

  def __init__(self, download_folder, file_name, db):
    self.file = os.path.join(download_folder, file_name)
    self.db = db
    pass

  def parse_data(self):
    data = pd.read_csv(self.file)
    del data[data.keys()[13]]
    data = data[data['SERIES'] == 'EQ']
    data = self._add_average_trade_val(data)
    data = self._add_percentage_change(data)
    save_data = data.to_dict(orient='records')
    self.db.write_many_to_collection('equity', save_data)

  def _add_percentage_change(self, data):
    data['PERC'] = round((data['CLOSE'] - data['OPEN']) / data['OPEN'] * 100, 2)
    return data

  def _add_average_trade_val(self, data):
    data['AVGTRDVAL'] = round((data['TOTTRDVAL'] / data['TOTTRDQTY']), 2)
    return data