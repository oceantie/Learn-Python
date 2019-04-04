from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
driver_path=r"F:\chromedrive\chromedriver.exe"
driver=webdriver.Chrome(executable_path=driver_path)
# driver.get('https://www.baidu.com/')
#获取元素的方法
# inputTag=driver.find_element_by_id('kw')
# inputTag=driver.find_element_by_xpath('//input[@id="kw"]')
# inputTag.send_keys('python')

#获取select标签：
# from selenium.webdriver.support.ui import Select
# driver.get('http://www.scxdf.com/bsl/dz/')
# selectBtn=Select(driver.find_element_by_name('dz_zymc'))
#通过可见文本抓取
# selectBtn.select_by_visible_text('经典西点专业')
#通过value抓取
# selectBtn.select_by_value('时尚西点专业')
#通过index抓取
# selectBtn.select_by_index(3)
# print(driver.page_source)

# 行为链
# driver.get('https://www.baidu.com/')
# inputTag=driver.find_element_by_id('kw')
# submitTag=driver.find_element_by_id('su')
#
# action=ActionChains(driver)
# action.move_to_element(inputTag)
# action.send_keys_to_element(inputTag,'python')
# action.move_to_element(submitTag)
# action.click(submitTag)
# action.perform()

#cookie操作
#get_cookies()获取所有的cookies
driver.get('https://www.baidu.com/')
for cookie in driver.get_cookies():
    print(cookie)
print('='*30)
#根据value找cookie
print(driver.get_cookie('PSTM'))
#删除所有的cookies
driver.delete_all_cookies()