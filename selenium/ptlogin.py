from selenium import webdriver

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


def click_pt():
    driver_path = r"F:\chromedrive\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=driver_path)
    driver.get('https://report.ptengine.cn/login.html')
    username=driver.find_element_by_xpath('//input[@class="pt-form-control js-input-email"]')
    password=driver.find_element_by_xpath('//input[@class="pt-form-control js-input-pwd"]')
    login_btn=driver.find_element_by_xpath('//button[@class="pt-btn btn-login js-login qa-user-login"]')
    username.send_keys('li.jingjing01@xhgroup.cn')
    password.send_keys('52510100743636691A')
    login_btn.click()

    # time.sleep(5)
    # driver.implicitly_wait(10)
    # wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'.js-table-td-a-name')))
    try:
        element=WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,'.js-table-td-a-name'))
        )
        xdf_page=driver.find_element_by_xpath('//*[@id="profile"]/div/div[1]/div[2]/div[1]/div/div[2]/div/div/table/tbody/tr[1]/td[3]/div/a[1]')
        xdf_page.click()
    except:
        pass
    time.sleep(5)
    driver.quit()

def main():
    run_count=int(input("请输入需要执行次数:"))
    count=1
    while run_count:
        run_count=run_count-1
        # time.sleep(1)
        # print(run_count)
        print('当前执行次数%d'%(count))
        count = count + 1
        click_pt()
        time.sleep(3)

if __name__ == '__main__':
    main()