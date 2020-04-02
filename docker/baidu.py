#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-03-29 20:13
# @Author  : yang

from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains

browser = webdriver.Chrome()
browser.get("https://www.baidu.com/")
sleep(3)
browser.maximize_window()
sleep(3)
setting = browser.find_element_by_link_text("设置")
ActionChains(browser).move_to_element(setting).perform()
sleep(2)
browser.find_element_by_link_text("搜索设置").click()
sleep(2)
browser.find_element_by_xpath('//*[@id="wrapper"]/div[6]/div/div/ul/li[2]').click()
sleep(2)
browser.quit()

