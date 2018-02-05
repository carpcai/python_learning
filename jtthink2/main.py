

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.PhantomJS()

driver.get("https://www.baidu.com")

searchText = driver.find_element_by_id("kw")
searchText.send_keys("jtthink.com")

# searchBtn = driver.find_element_by_id("su")
searchBtn = driver.find_element_by_xpath("//input[@value='百度一下']")
print(searchBtn);
# searchBtn.click()

# WebDriverWait(driver, 20).until(expected_conditions.title_contains("jtthink.com"))


# print(driver.page_source)

