from selenium import webdriver
import time
import threading

phone='17428546713'
path = "F:\chromedrive\chromedriver.exe"
# driver=webdriver.Chrome(executable_path=path)


chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("--proxy-server=http://119.180.140.140:8060")
# 一定要注意，=两边不能有空格，不能是这样--proxy-server = http://202.20.16.82:10152
browser = webdriver.Chrome(executable_path=path,options = chromeOptions)

# 查看本机ip，查看代理是否起作用
browser.get("http://httpbin.org/ip")
print(browser.page_source)

# 退出，清除浏览器缓存
time.sleep(3)
browser.quit()

def zhihu():
    # phone = '18628246713'
    path = "F:\chromedrive\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=path)
    driver.get("https://www.zhihu.com/signup?next=%2F")
    tel = driver.find_element_by_xpath("//input[@placeholder='手机号']")
    tel.send_keys(phone)
    button = driver.find_element_by_xpath("//button[@class='Button CountingDownButton SignFlow-smsInputButton Button--plain']")
    button.click()
    driver.quit()
def guazi():
    # phone = '18628246713'
    path = "F:\chromedrive\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=path)
    driver.get("https://www.guazi.com/www/bj/buy")
    a_btn = driver.find_element_by_xpath("//a[@id='js-login-new']")
    a_btn.click()
    tel = driver.find_element_by_xpath("//input[@placeholder='请输入您的手机号码']")
    tel.send_keys(phone)
    button = driver.find_element_by_xpath("//button[@class='get-code']")
    button.click()
    driver.quit()
def wph():
    # phone = '18628246713'
    path = "F:\chromedrive\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=path)
    driver.get("https://passport.vip.com/register?src=https%3A%2F%2Fwww.vip.com%2F")
    tel = driver.find_element_by_xpath("//input[@placeholder='请输入手机号码']")
    tel.send_keys(phone)
    driver.find_element_by_xpath("//input[@placeholder='请再次输入上面的密码']").click()
    button = driver.find_element_by_xpath( "//a[@id='J_mobile_verifycode_btn']")
    button.click()
    driver.quit()

def wantong():
    phone = '17628887713'
    path = "F:\chromedrive\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=path)

    driver.get("http://wap.scwtqx.com/mfdh.html")
    tel = driver.find_element_by_xpath("//input[@placeholder='请输入您的手机号码']")
    tel.send_keys(phone)
    button=driver.find_element_by_xpath("//button[@id='cbBtnkst']").click()
    driver.quit()

def omik_cd():
    phone = '17441887713'
    path = "F:\chromedrive\chromedriver.exe"
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_argument("--proxy-server=http://119.180.140.140:8060")
    # 一定要注意，=两边不能有空格，不能是这样--proxy-server = http://202.20.16.82:10152
    driver = webdriver.Chrome(executable_path=path, options=chromeOptions)
    # driver = webdriver.Chrome(executable_path=path)
    driver.get("http://m.cdomick.com/zy/xidian/1.html")
    name = driver.find_element_by_xpath("//input[@placeholder='您的姓名']")
    name.send_keys('王远')
    name = driver.find_element_by_xpath("//input[@placeholder='您的手机号']")
    name.send_keys(phone)
    time.sleep(1)
    button = driver.find_element_by_xpath("//div[@class='zhuanye btn-omick1']").click()
    driver.quit()


if __name__ == '__main__':
    # t1=threading.Thread(target=zhihu)
    # t2=threading.Thread(target=guazi)
    # t3 = threading.Thread(target=wph)
    # t1.start()
    # t2.start()
    # t3.start()
    # wantong()
    omik_cd()


