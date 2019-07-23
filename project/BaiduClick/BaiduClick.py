from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from lxml import etree
import time
BASE_URL='//*[@id="results"]/div[1]/div/div/div{}/div/div/div/a[1]/span'

def sign_baidu():
    driver_path = r"F:\chromedrive\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=driver_path)
    driver.get('https://m.baidu.com/')
    input_=driver.find_element_by_xpath('//div[@class="con-wrap"]/input')
    submit_button=driver.find_element_by_xpath('//*[@id="index-bn"]')
    input_.send_keys('学厨师')
    driver.implicitly_wait(10)
    submit_button.click()
    BASE_URL='//*[@id="results"]/div[1]/div/div/div{}/div/div/div/a[1]/span'
    driver.implicitly_wait(10)
    source=driver.page_source
    html=etree.HTML(source)
    divs_html=html.xpath('//*[@id="results"]/div[1]/div/div/div')

    for index, x in enumerate(divs_html):
        url = x.xpath('./div/div/div/a[1]/span/text()')[0]
        # print(x.xpath('./div/div/div/a[1]/span/text()')[0])
        if url == 'm.scxdf.com':
            click_url = BASE_URL.format([index + 1])
            print('点击成功')
            test_url = driver.find_element_by_xpath(click_url)
            test_url.click()
            time.sleep(5)

            # print(test_url)
        else:
            print('目标URL无展现')
    driver.close()

def run():
    count = 0
    while count<3:
        count = count + 1
        print('正在点击第',count,'次')
        sign_baidu()
        time.sleep(2)

# divs=driver.find_element_by_xpath('//*[@id="results"]/div[1]/div/div/div')
# url1=driver.find_element_by_xpath('//*[@id="results"]/div[1]/div/div/div[1]/div/div/div/a[1]/span')
# url2=driver.find_element_by_xpath('//*[@id="results"]/div[1]/div/div/div[2]/div/div/div/a[1]/span')

# for index,x in enumerate(divs_html):
#     url=x.xpath('./div/div/div/a[1]/span/text()')[0]
#     # print(x.xpath('./div/div/div/a[1]/span/text()')[0])
#     if url=='m.scxdf.com':
#         click_url=BASE_URL.format([index+1])
#         print(click_url)
#         test_url = driver.find_element_by_xpath(click_url)
#         test_url.click()
#         # print(test_url)
#     else:
#         print('目标URL无展现')