import os
import pandas as pd

class ShortData():

  def __init__(self, download_folder, file_name, db):
    self.file = os.path.join(download_folder, file_name)
    self.db = db
    pass

  def parse_data(self):
    data = pd.read_csv(self.file)
    if not data.empty:
      save_data = data.to_dict(orient='records')
      self.db.write_many_to_collection('shorts', save_data)
    