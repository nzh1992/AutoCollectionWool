# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2020/12/23
Last Modified: 2020/12/23
Description: 
"""


class TargetURL(object):
    def __init__(self, target_url_dict):
        """
        build url

        :param target_url_dict: dict. Init target url.
            format: {'baidu': 'http://www.baidu.com'}. url must contain protocol and domain name.
        """
        if not isinstance(target_url_dict, dict):
            raise TypeError("target_url_dict must be dict.")

        if not target_url_dict:
            raise ValueError("target_url_dict can't be empty.")

        self.url_list = []
        for k, url in target_url_dict.items():
            self.__setattr__(k, url)
            self.url_list.append(k)
