# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2020/12/23
Last Modified: 2020/12/23
Description: 
"""
import os

from config import config
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from framework.selector import Selector


class ChromeDriver(object):
    def __init__(self):
        self.browser_name = "chrome"
        self.driver_path = None
        self.driver = None
        self.current_url = None
        self.history = []
        self.current_tab = None
        self.previous_tab = None

        self._load_driver()

    def jump(self, url):
        """
        jump to page. it will save url to self.current_url when load successful, otherwise raise error.

        :param url: str. target url to jump.
        :return:
        """
        try:
            self.driver.get(url)
        except Exception as e:
            raise e

    def jump_wait(self, url, selector):
        """
        jump to page until page loaded completely it will save url to self.current_url when load successful,
        otherwise raise error.

        :param url: str. target url to jump.
        :param selector: framework.selector.Selector object. Used for get selector type and selector value.
        :return:
        """
        self.driver.get(url)
        try:
            if isinstance(selector, Selector):
                element = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((selector.type, selector.value))
                )
            else:
                raise TypeError(f"selector type must be framework.selector.Selector")
        except Exception as e:
            raise e

    def next_tab(self):
        """
        change current tab to next tab.
        :return:
        """
        self.driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)
        self.previous_tab = self.driver.current_window_handle

    def _load_driver(self):
        driver_path = config.BROWSER_DRIVER_PATH.get(self.browser_name)
        if not driver_path:
            raise ValueError(f"can't find {self.browser_name} driver in config file.")

        if not os.path.exists(driver_path):
            raise ValueError(f"{driver_path} not exist.")

        self.driver_path = driver_path

        try:
            self.driver = webdriver.Chrome(self.driver_path)
            print("Chrome Browser Driver start, ok.")
        except Exception as e:
            raise e

