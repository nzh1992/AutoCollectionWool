# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2020/12/23
Last Modified: 2020/12/23
Description: 
"""
from selenium.webdriver.common.by import By


class Selector(object):
    # all types of selector
    support_types = ['id', 'name', 'class', 'tag']

    def __init__(self, selector_type, value = None):
        self._check_type(selector_type)

        self.type = self._transfer_type(selector_type)
        self.value = self.value

    @staticmethod
    def _check_type(selector_type):
        if selector_type not in Selector.support_types:
            raise ValueError(f"Selector type must in {Selector.support_types}")

    def _transfer_type(self, selector_type):
        mapping_dict = {
            'id': By.ID,
            'name': By.NAME,
            'class': By.CLASS_NAME,
            'tag': By.TAG_NAME
        }
        if mapping_dict.get(selector_type):
            return mapping_dict.get(selector_type)
        else:
            raise ValueError(f"Can't get transfer type for {selector_type}")