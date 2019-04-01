from selenium import webdriver
import time
import threading

# phone='18628246713'
# path = "F:\chromedrive\chromedriver.exe"
# driver=webdriver.Chrome(executable_path=path)
def zhihu():
    phone = '18628246713'
    path = "F:\chromedrive\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=path)
    driver.get("https://www.zhihu.com/signup?next=%2F")
    tel = driver.find_element_by_xpath("//input[@placeholder='手机号']")
    tel.send_keys(phone)
    button = driver.find_element_by_xpath("//button[@class='Button CountingDownButton SignFlow-smsInputButton Button--plain']")
    button.click()
    driver.quit()
def guazi():
    phone = '18628246713'
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
    phone = '18628246713'
    path = "F:\chromedrive\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=path)
    driver.get("https://passport.vip.com/register?src=https%3A%2F%2Fwww.vip.com%2F")
    tel = driver.find_element_by_xpath("//input[@placeholder='请输入手机号码']")
    tel.send_keys(phone)
    driver.find_element_by_xpath("//input[@placeholder='请再次输入上面的密码']").click()
    button = driver.find_element_by_xpath( "//a[@id='J_mobile_verifycode_btn']")
    button.click()
    driver.quit()

def xdfxx():
    phone = '18599854178'
    path = "F:\chromedrive\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=path)
    driver.get("http://m.scxdfxx.com/")
    time.sleep(5)
    iframe = driver.find_element_by_id("ks_dir_ifra")
    driver.switch_to.frame(iframe)
    driver.find_element_by_id('minimize').click()
    driver.switch_to.default_content()

    # nam=driver.find_element_by_xpath("//input[@placeholder='请输入您的尊称']").send_keys("测试")
    # tel=driver.find_element_by_xpath("//input[@placeholder='请输入您的电话号码']")
    # tel.send_keys(phone)
    # button = driver.find_element_by_xpath("//input[@name='submit']")
    # button.click()
    driver.quit()


if __name__ == '__main__':
    # zhihu()
    # guazi()
    # wph()
    xdfxx()


    # t1=threading.Thread(target=zhihu)
    # t2=threading.Thread(target=guazi)
    # t3 = threading.Thread(target=wph)
    # t4 = threading.Thread(target=yhf)
    # t1.start()
    # t2.start()
    # t3.start()
    # t4.start()


