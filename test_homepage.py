from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os

remote_driver = os.environ['REM_DRIVER']

capabilities = {}
capabilities = DesiredCapabilities.CHROME.copy()
driver = webdriver.Remote(command_executor=remote_driver, desired_capabilities=capabilities)
driver.get("https://fresh.efishery.com")

# verify able to select city
print("verify select city")
bandung_options = driver.find_element_by_xpath("//*[text()='bandung']")
bandung_options.click()
lokasi_button = driver.find_element_by_xpath("//span[text()='Lokasi']")
bandung_options.click()

#assert banner (carousel)
print("verify banner")
driver.find_element_by_xpath("//*[@class='carousel-inner']")
driver.find_element_by_xpath("//*[@class='slider-item carousel-item']")
driver.find_element_by_xpath("//*[@class='carousel-control-prev']")
driver.find_element_by_xpath("//*[@class='carousel-control-next']")
driver.find_element_by_xpath("//img[@element='banner']")

#verify catalog appear
print("verify catalogue")
driver.find_element_by_xpath("//*[text()='BELI SEKARANG']")
driver.find_element_by_xpath("//*[text()='Bukalapak']")
driver.find_element_by_xpath("//*[text()='Tokopedia']")
driver.find_element_by_xpath("//*[text()='Blibli']")

driver.quit()

