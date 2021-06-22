# installed and imported selenium
# downloaded chrome web driver from chromium.org

from selenium import webdriver
PATH = "C:\Program Files (x86)\webdev\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://time4t.io")
print(driver.title)
