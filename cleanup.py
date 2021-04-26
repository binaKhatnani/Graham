import shutil

def cleanup(download_path, delete_files):
  if delete_files:
    shutil.rmtree(download_path)