# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2020/12/23
Last Modified: 2020/12/23
Description: 
"""
import time

from config import config
from core.data_structure.url import TargetURL
from framework.web_driver import ChromeDriver
from selenium.webdriver.common.keys import Keys


class BaiduProcess(object):
    """
    Define operations of Baidu website
    """
    def __init__(self):
        self.chrome_driver = ChromeDriver()
        self.home_page_url = TargetURL(config.TARGET_URL).baidu

    def open_home_page(self):
        self.chrome_driver.jump(self.home_page_url)

    def login(self):
        self.chrome_driver.driver.find_element_by_link_text("登录").click()

    def custom_process(self):
        self.open_home_page()

        self.login()


class TaobaoProcess(object):
    def __init__(self):
        self.name = "taobao"
        self.chrome_driver = ChromeDriver()
        self.home_page_url = TargetURL(config.TARGET_URL).taobao

    def open_home_page(self):
        self.chrome_driver.jump(self.home_page_url)

    def login(self):
        self.chrome_driver.driver.find_element_by_link_text("登录").click()

        time.sleep(2)

        # change tab to login page.
        # self.chrome_driver.next_tab()
        window_tabs = self.chrome_driver.driver.window_handles
        self.chrome_driver.driver.switch_to.window(window_tabs[1])

        user_name, pwd = config.USER_ACCOUNT.get(self.name)[1]
        self.chrome_driver.driver.find_element_by_id("fm-login-id").send_keys(user_name)
        self.chrome_driver.driver.find_element_by_id("fm-login-password").send_keys(pwd)
        self.chrome_driver.driver.find_element_by_class_name("password-login").click()

        time.sleep(1)
        if "login_agreement" in self.chrome_driver.driver.current_url:
            self.chrome_driver.driver.find_element_by_id("J_AgreementBtn").click()

    def quit(self):
        self.chrome_driver.driver.close()

    def custom_process(self):
        self.open_home_page()

        self.login()


t = TaobaoProcess()
t.custom_process()


