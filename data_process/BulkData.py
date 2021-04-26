import os
import pandas as pd

class BulkData():

  def __init__(self, download_folder, file_name, db):
    self.file = os.path.join(download_folder, file_name)
    self.db = db
    pass

  def parse_data(self):
    data = pd.read_csv(self.file)
    data.rename(columns = {'Trade Price / Wght. Avg. Price': 'TPtoWAP'}, inplace=True)
    save_data = data.to_dict(orient='records')
    print(save_data)
    self.db.write_many_to_collection('bulk', save_data)
