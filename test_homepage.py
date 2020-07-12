from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://fresh.efishery.com")
sleep(5)
driver.quit()

