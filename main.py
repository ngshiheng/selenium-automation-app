import json
import os
import sys
from configparser import ConfigParser

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)


def main():
    def check_if_element_exist(xpath: str) -> bool:
        try:
            driver.find_element_by_xpath(xpath)

        except NoSuchElementException:
            return False

        return True

    # Reads data from `example.ini`
    config = ConfigParser()
    config.read(resource_path('example.ini'))
    text = config.get('example', 'text')
    print(f'Reading text={text} from config.ini')

    # Reads data from 'example.json
    with open(resource_path('example.json'), 'r') as f:
        credentials = json.load(f)
        username = credentials['username']
        print(f'Getting username={username} from json')

        password = credentials['password']
        print(f'Getting password={password} from json')

    # Launch selenium webdriver
    driver = webdriver.Chrome(resource_path('driver\chromedriver.exe'))
    driver.get('http://quotes.toscrape.com/')

    driver.find_element_by_xpath('//a[@href="/login"]').click()

    username_form_input = driver.find_element_by_id('username')
    username_form_input.send_keys(username)

    password_form_input = driver.find_element_by_id('password')
    password_form_input.send_keys(password)
    password_form_input.send_keys(Keys.ENTER)

    assert check_if_element_exist('//a[@href="/logout"]') == True
    driver.close()
    print('Yay!')


if __name__ == '__main__':
    print("Hello!")
    main()
    print("Bye!")
