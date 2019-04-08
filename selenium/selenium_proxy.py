from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
driver_path=r"F:\chromedrive\chromedriver.exe"
options=webdriver.ChromeOptions()
options.add_argument("--proxy-server=http://116.209.52.107:9999")

driver=webdriver.Chrome(executable_path=driver_path,options=options)
driver.get('http://httpbin.org/ip')
