import json
import os
import zipfile
import re

class PreProcess():
  
  def __init__(self, download_path):
    self.downlad_folder = download_path

  def extract_zip_files(self):
    for f in os.listdir(self.downlad_folder):
      extension = os.path.splitext(f)[1]
      if extension == '.zip':
        with zipfile.ZipFile(os.path.join(self.downlad_folder, f), 'r') as zip_ref:
          zip_ref.extractall(self.downlad_folder)
        os.remove(os.path.join(self.downlad_folder,f))

  def get_prefix(self):
    files = os.listdir(self.downlad_folder)
    new_filename = ''
    for f in files:
      if re.search('^cm.*bhav[.]csv$', f):
        new_filename = re.search('^cm(.*)bhav[.]csv$', f).group(1)
    self.prefix = new_filename
    return self.prefix

  def rename_file(self, old_filename = '', new_filename = ''):
    updated_new_filename = self.prefix + new_filename
    src = os.path.join(self.downlad_folder, old_filename)
    dst = os.path.join(self.downlad_folder, updated_new_filename)
    os.rename(src, dst)
  
  