import json

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys


def check_if_element_exist(xpath: str) -> bool:
    try:
        webdriver.find_element_by_xpath(xpath)

    except NoSuchElementException:
        return False

    return True


with open('credentials.json', 'r') as f:
    credentials = json.load(f)


webdriver = webdriver.Chrome('/usr/bin/chromedriver')
webdriver.get('http://quotes.toscrape.com/')

webdriver.find_element_by_xpath('//a[@href="/login"]').click()

username_form_input = webdriver.find_element_by_id('username')
username_form_input.send_keys(credentials['username'])

password_form_input = webdriver.find_element_by_id('password')
password_form_input.send_keys(credentials['password'])
password_form_input.send_keys(Keys.ENTER)

assert check_if_element_exist('//a[@href="/logout"]') == True
