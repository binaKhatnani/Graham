from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import json
import shutil
import os

class Driver():

  # load the driver and start
  def __init__(self, path_to_driver, download_path):
    if not os.path.exists(download_path):
      os.mkdir(download_path)
    self.download_path = download_path

    chrome_options = webdriver.ChromeOptions()
    prefs = {"download.default_directory" : download_path}
    chrome_options.add_experimental_option("prefs",prefs)
    self.driver = webdriver.Chrome(executable_path=path_to_driver, chrome_options=chrome_options)


  def get_driver(self):
    return self.driver


  def wait_until_downloads_complete(self):
    download_url = "chrome://downloads"
    if not self.driver.current_url.startswith(download_url):
      self.driver.get(download_url)

    def _all_files_downloaded_script(driver):
      script_output = driver.execute_script("""
                  var items = document.querySelector('downloads-manager')
                      .shadowRoot.getElementById('downloadsList').items;
                  return items
                  """)
      return script_output

    status = False
    while status == False:
      output_list = WebDriverWait(self.driver, 10, 1).until(_all_files_downloaded_script)
      status = True
      for item in output_list:
        if item['state'] != 'COMPLETE':
          status = False
    return status


  # quit the application
  def quit(self):
    self.driver.quit()
    