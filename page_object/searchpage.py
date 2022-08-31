#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from page.webpage import WebPage, sleep
from common.readelement import Element

search = Element('search')


class SearchPage(WebPage):
    """
    继承webpage.py中WebPage
    页面对象类，把webpage中的selenium方法和page_element中的页面元素进行整合
    """

    def input_search(self, content):
        """输入搜索"""
        self.input_text(search['搜索框'], txt=content)
        sleep()

    @property
    def imagine(self):
        """搜索联想"""
        return [x.text for x in self.find_elements(search['候选'])]

    def click_search(self):
        """点击搜索"""
        self.is_click(search['搜索按钮'])


if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    search_page = SearchPage(driver)
    search_page.get_url("http://www.baidu.com")
    search_page.input_search("测试搜索")
    print(search_page.imagine)
    driver.quit()

