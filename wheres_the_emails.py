
from selenium import webdriver
import time
import pyperclip

#twitter login
url = 'https://twitter.com/login'

# your path to webdriver
driver  = webdriver.Chrome('your/path/to/webdriver')
driver.get(url)  #opens url

time.sleep(3)

# finds login boxes. Put your own credentials
driver.find_element_by_name('session[username_or_email]').send_keys('your_email@email.com')
driver.find_element_by_name('session[password]').send_keys('your_password')

time.sleep(3)
# clicks login
driver.find_element_by_xpath("//*[text()='Log in']").click()

time.sleep(3)

#defines and opens compose tweet
url2 = 'https://twitter.com/compose/tweet'
driver.get(url2)

time.sleep(3)

#gets tweet textbox
sendtweet = driver.find_element_by_xpath("//div[@class='notranslate public-DraftEditor-content']")
sendtweet.send_keys('@HillaryClinton  WHERES THE EMAILS???')


time.sleep(3)

# clicks tweet
clicktweet = driver.find_element_by_xpath("//div[@class='css-18t94o4 css-1dbjc4n r-urgr8i r-42olwf r-sdzlij r-1phboty r-rs99b7 r-1w2pmg r-1n0xq6e r-1vuscfd r-1dhvaqw r-1fneopy r-o7ynqc r-6416eg r-lrvibr']")

clicktweet.click()
