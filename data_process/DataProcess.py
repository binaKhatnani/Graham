import os
import re
import pymongo
from data_process.DataExtraction import PreProcess
from data_process.MainData import MainData
from data_process.ShortData import ShortData
from data_process.BlockData import BlockData
from data_process.BulkData import BulkData

class DataProcess():

    def __init__(self, root_path, db):
        self.download_path = os.path.join(root_path, 'downloads')
        self.prefix = ''
        self.rename_dict = {
            'block.csv': 'Block.csv',
            'ShortSelling.csv': 'Short.csv',
            'bulk.csv': 'Bulk.csv'
        }
        self.db = db

    def process_files(self):
        preProcess = PreProcess(self.download_path)
        preProcess.extract_zip_files()
        self.prefix = preProcess.get_prefix()
        files = os.listdir(self.download_path)
        for f in files:
            if re.search('^cm.*bhav[.]csv$', f):
                preProcess.rename_file(f, 'Main.csv')
            else:
                preProcess.rename_file(f, self.rename_dict[f])

    def process_data(self):
        main_file_data = MainData(self.download_path, self.prefix+'Main.csv', self.db)
        main_file_data.parse_data()
        short_file_data = ShortData(self.download_path, self.prefix+'Short.csv', self.db)
        short_file_data.parse_data()
        block_file_data = BlockData(self.download_path, self.prefix+'Block.csv', self.db)
        block_file_data.parse_data()
        bulk_file_data = BulkData(self.download_path, self.prefix+'Bulk.csv', self.db)
        bulk_file_data.parse_data()
    
    def process_backup_data(self):
        pass
        # run a loop on backup folder to process each file and store in db
        # try using process_data function if possible