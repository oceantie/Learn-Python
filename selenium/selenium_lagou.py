from selenium import webdriver
from lxml import etree
import re
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
class LagouSpider(object):
    driver_path=r"F:\chromedrive\chromedriver.exe"
    def __init__(self):
        self.driver=webdriver.Chrome(executable_path=LagouSpider.driver_path)
        self.url='https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='
        self.positions=[]

    def run(self):
        self.driver.get(self.url)
        while True:
            source=self.driver.page_source
            WebDriverWait(driver=self.driver,timeout=10).until(
                EC.presence_of_element_located((By.XPATH,"//div[@class='pager_container']/span[last()]"))
           )
            self.parse_list_page(source)
            try:
            #找下一页的按钮
                next_btn=self.driver.find_element_by_xpath("//div[@class='pager_container']/span[last()]")
                if "pager_next pager_next_disabled" in next_btn.get_attribute('class') :
                    break
                else:
                    next_btn.click()
            except:
                print(source)
            time.sleep(2)

    def parse_list_page(self,source):
        html=etree.HTML(source)
        links=html.xpath("//a[@class='position_link']/@href")
        for link in links:
            self.request_detail_page(link)
            time.sleep(1)
            # print(link)
    def request_detail_page(self,url):
        # self.driver.get(url)
        self.driver.execute_script("window,open('%s')"%url)
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver,timeout=10).until(
            EC.presence_of_element_located((By.XPATH,"//span[@class='name']"))
        )
        source=self.driver.page_source
        self.parse_detail_page(source)
        #关闭详情页
        self.driver.close()
        #继续切换回列表页
        self.driver.switch_to.window(self.driver.window_handles[0])
    def parse_detail_page(self,source):
        html=etree.HTML(source)
        position_name=html.xpath("//span[@class='name']/text()")[0]
        job_request_spans=html.xpath("//dd[@class='job_request']//span")
        salary=job_request_spans[0].xpath(".//text()")[0].strip()
        city=job_request_spans[1].xpath(".//text()")[0].strip()
        city=re.sub(r"[\s/]","",city)
        work_year=job_request_spans[2].xpath(".//text()")[0].strip()
        education=job_request_spans[3].xpath(".//text()")[0].strip()
        position={
            'name':position_name,
            'slary':salary,
            'city':city,
            'work_year':work_year,
            'education':education
        }
        self.positions.append(position)
        print(position)
        print("="*40)
if __name__ == '__main__':
    spider=LagouSpider()
    spider.run()