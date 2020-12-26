# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2020/12/23
Last Modified: 2020/12/23
Description: 
"""


class Account(object):
    def __init__(self, username, pwd, **kwargs):
        if not username or not pwd:
            raise ValueError("username and pwd can't be empty.")

        # Required Parameters
        self.user_name = username
        self.pwd = pwd

        # Optional Parameters
        self.optional_attrs = []
        for k, v in kwargs.items():
            self.__setattr__(k, v)
            self.optional_attrs.append(k)