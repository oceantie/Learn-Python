from selenium import webdriver
driver_path=r"F:\chromedrive\chromedriver.exe"
driver=webdriver.Chrome(executable_path=driver_path)
driver.get('https://www.douban.com/')
#driver.get('https://www.baidu.com/')
driver.execute_script("window.open('https://www.baidu.com/')")
print(driver.window_handles[1])
#在代码中切换窗口使用switch_to.window
#driver.window_handles是个列表装的都是窗口句柄，会按照打开页面的顺序来存储页面窗口句柄
driver.switch_to.window(driver.window_handles[1])
print(driver.current_url)