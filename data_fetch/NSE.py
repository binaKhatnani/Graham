class NSE():

  # initialize class with driver
  def __init__(self, webdriver):
    self.driver = webdriver

  # get the title of the page
  def load_download_page(self):
    link = "https://www1.nseindia.com/products/content/all_daily_reports.htm"
    # page_load_delay = 3
    date_xpath = '/html/body/div[2]/div[3]/div[2]/div/div[2]/div[1]/div[1]/div[1]/ul/li[4]/font[1]/b'
    
    self.driver.get(link)
    today_date = self.driver.find_elements_by_xpath(date_xpath)[0].text
    print(today_date)

  # common method to download any link by passing only xpath
  def _download_file_by_xpath(self, xpath):
    link = self.driver.find_elements_by_xpath(xpath)[0]
    link.click()

  # download bhavcopy file
  def download_bhavcopy(self):
    bhavcopy_xpath = '/html/body/div[2]/div[3]/div[2]/div/div[2]/div[1]/div[1]/div[1]/div[1]/div/table/tbody/tr[3]/td[1]/a'
    self._download_file_by_xpath(bhavcopy_xpath)

  # download short selling file
  def download_short_selling(self):
    short_selling_xpath = '/html/body/div[2]/div[3]/div[2]/div/div[2]/div[1]/div[1]/div[1]/div[1]/div/table/tbody/tr[19]/td[1]/a'
    self._download_file_by_xpath(short_selling_xpath)

  # download block deals file
  def download_block_deals(self):
    block_deals_xpath = '/html/body/div[2]/div[3]/div[2]/div/div[2]/div[1]/div[1]/div[1]/div[1]/div/table/tbody/tr[18]/td[1]/a'
    self._download_file_by_xpath(block_deals_xpath)

  def download_bulk_deals(self):
    bulk_deals_xpath = '/html/body/div[2]/div[3]/div[2]/div/div[2]/div[1]/div[1]/div[1]/div[1]/div/table/tbody/tr[17]/td[1]/a'
    self._download_file_by_xpath(bulk_deals_xpath)
  
  # def download_market_activity_report(self):
  #   market_activity_report = '/html/body/div[2]/div[3]/div[2]/div/div[2]/div[1]/div[1]/div[1]/div[1]/div/table/tbody/tr[6]/td[1]/a'
  #   self._download_file_by_xpath(market_activity_report)

  # close the driver
  def close_page(self):
    self.driver.close()