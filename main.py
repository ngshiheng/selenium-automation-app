import json
import os
import sys
import time
from configparser import ConfigParser

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.webdriver import WebDriver


def check_if_element_exist(driver: WebDriver, xpath: str) -> bool:
    try:
        driver.find_element_by_xpath(xpath)

    except NoSuchElementException:
        return False

    return True


def resource_path(relative_path: str) -> str:
    '''
    Get absolute path to resource, works for dev and for PyInstaller
    '''
    try:
        base_path = sys._MEIPASS

    except Exception:
        base_path = os.path.dirname(__file__)

    return os.path.join(base_path, relative_path)


def main() -> None:
    '''
    A simple selenium application that performs login action with dummy credentials at http://quotes.toscrape.com/
    '''

    # Reads data from 'example.json
    # NOTE: We do not use `resource_path` here while reading 'example.json' because we want the generated `exe` to always read from this file based on users' configuration
    with open('example.json', 'r') as f:
        credentials = json.load(f)
        username = credentials['username']
        password = credentials['password']

    # Reads data from 'example.ini'
    config = ConfigParser()
    config.read('example.ini')

    # Launch selenium webdriver
    CHROME_DRIVER_PATH = config.get('chromedriver', 'path')
    DURATION = config.getint('delay', 'seconds')

    # NOTE: We are using `resource_path` here because we want the generated `exe` to look for chromedriver from an absolute path
    driver = webdriver.Chrome(resource_path(CHROME_DRIVER_PATH))

    URL = config.get('website', 'url')
    driver.get(URL)

    # Clicks the 'login' button
    driver.find_element_by_xpath('//a[@href="/login"]').click()

    # Enters dummy username
    time.sleep(DURATION)
    username_form_input = driver.find_element_by_id('username')
    time.sleep(DURATION)
    username_form_input.send_keys(username)

    # Enter dummy password
    time.sleep(DURATION)
    password_form_input = driver.find_element_by_id('password')
    password_form_input.send_keys(password)
    password_form_input.send_keys(Keys.ENTER)

    # Quick way to make sure you're 'logged in'
    time.sleep(DURATION)
    assert check_if_element_exist(driver, '//a[@href="/logout"]') == True
    driver.close()
    # End


if __name__ == '__main__':
    print("Hello!")
    main()
    print("Bye!")
