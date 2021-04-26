import os
from data_fetch.NSE import NSE
from data_fetch.Driver import Driver

# from Cleanup import cleanup

class DataDownload():

  def __init__(self, root_path):
    self.root_path = root_path
    self.driver_path = os.path.join(root_path, 'chromedriver.exe')
    self.download_path = os.path.join(root_path, 'downloads')
    
  def fetch_data(self):
    driver = Driver(self.driver_path, self.download_path)
    nse_app = NSE(driver.get_driver())
    nse_app.load_download_page()
    nse_app.download_bhavcopy()
    nse_app.download_short_selling()
    nse_app.download_block_deals()
    nse_app.download_bulk_deals()
    # nse_app.download_market_activity_report()
    driver.wait_until_downloads_complete()
    driver.quit()
