from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import re
import shutil
from pathlib import Path


ser = Service("chromedriver.exe")

options = Options()
options.add_argument("--window-size=1920,1200")
DRIVER_PATH = 'chromedriver.exe'
driver = webdriver.Chrome(options=options, service=ser)
driver.get("ytlink")

user_Data = driver.find_elements(By.XPATH, '//*[@id="header"]/ytmusic-detail-header-renderer/div/div[2]/yt-formatted-string[1]/span[1]')
links = []

for i in user_Data:
    sayi = re.findall("\d+", i.text)[0]

a = 1
basliklar = []
while(a<=int(sayi)):
    print("girdi buraya" + sayi)
    the_xpath = ('//*[@id="contents"]/ytmusic-responsive-list-item-renderer[%s]/div[2]/div[1]/yt-formatted-string/a'%(a))
    user_Data = driver.find_elements(By.XPATH, the_xpath)
    for i in user_Data:
        basliklar.append(i.text)
    a+=1
print(basliklar)

for i in basliklar:
    myfile = Path(i+".mp3")
    if myfile.exists():
        shutil.move(i+".mp3", "klasorismi")
    
driver.quit()
