import json
import os
import sys
from configparser import ConfigParser

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys


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
    A simple selenium application that goes to http://quotes.toscrape.com/ to perform a login action with dummy credentials
    '''

    def check_if_element_exist(xpath: str) -> bool:
        try:
            driver.find_element_by_xpath(xpath)

        except NoSuchElementException:
            return False

        return True

    # Reads data from `example.ini`.
    config = ConfigParser()

    # NOTE: We do not use `resource_path` here because we want the generated `exe` to always read from this file based on users' configuration
    config.read('example.ini')

    text = config.get('example', 'text')
    print(f'Reading text={text} from config.ini')

    # Reads data from 'example.json
    # NOTE: We do not use `resource_path` here because we want the generated `exe` to always read from this file based on users' configuration
    with open('example.json', 'r') as f:
        credentials = json.load(f)
        username = credentials['username']
        print(f'Getting username={username} from json')

        password = credentials['password']
        print(f'Getting password={password} from json')

    # Launch selenium webdriver
    driver = webdriver.Chrome(resource_path('driver\chromedriver.exe'))
    driver.get('http://quotes.toscrape.com/')

    # Clicks the 'login' button
    driver.find_element_by_xpath('//a[@href="/login"]').click()

    # Enters dummy username
    username_form_input = driver.find_element_by_id('username')
    username_form_input.send_keys(username)

    # Enter dummy password
    password_form_input = driver.find_element_by_id('password')
    password_form_input.send_keys(password)
    password_form_input.send_keys(Keys.ENTER)

    # Quick way to make sure you're 'logged in'
    assert check_if_element_exist('//a[@href="/logout"]') == True
    driver.close()
    # End


if __name__ == '__main__':
    print("Hello!")
    main()
    print("Bye!")
