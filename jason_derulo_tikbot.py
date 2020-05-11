from selenium import webdriver
import time

url = 'https://www.tiktok.com/trending?lang=en'

driver = webdriver.Chrome('/Users/eganansorge/Downloads/chromedriver')

driver.get(url)

time.sleep(5)

jason = driver.find_element_by_xpath('//a[contains(@href, "jason")]')

jason.click()

time.sleep(2)


report = driver.find_element_by_xpath("//div[@class='jsx-177938563 report-text']")

report.click()

time.sleep(1.5)

spam = driver.find_element_by_class_name('jsx-572710943')

spam.click()

time.sleep(1)

next_button = driver.find_element_by_xpath("//*[text()='Next']")
next_button.click()

time.sleep(1)

dropdown = driver.find_element_by_xpath("//div[@class='jsx-3862494444 select']")
dropdown.click()

time.sleep(0.5)

covid = driver.find_element_by_xpath("//*[text()='COVID-19 misinformation']")
covid.click()

time.sleep(1)


submit = driver.find_element_by_xpath("//*[text()='Submit']")
submit.click()

