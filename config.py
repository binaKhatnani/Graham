import json

config = {
  "root_path": '',
  "data_download": '',
  "data_process": '',
  "delete_files_after_processing": '',
  "db": ''
}

config_values = json.loads(open('./config.json').read())

try:
  root_path = config_values['root']
except:
  root_path = ''
  print("Please add root_path value in config.json folder")
config["root_path"] = root_path

try:
  delete_files = config_values['delete_files_after_processing']
except:
  delete_files = True
config["delete_files_after_processing"] = delete_files

try:
  data_download = config_values['data_download']
except:
  data_download = True
config["data_download"] = data_download

try:
  data_process = config_values['data_process']
except:
  data_process = True
config["data_process"] = data_process

try:
  db = config_values['database']
except:
  db = 'market'
config['db'] = db

