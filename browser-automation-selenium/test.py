from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome('browser-automation-selenium/chromedriver')
browser.get('https://www.americanas.com.br/')

elem = browser.find_element_by_link_text('notebook')
elem.get_attribute('href')
elem.click()

elem = browser.find_element_by_link_text('celulares')
elem.get_attribute('href')
elem.click()

searchBar = browser.find_element_by_id('h_search-input')
searchBar.send_keys('fone razer')
searchBar.send_keys(Keys.ENTER)
