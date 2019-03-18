#!/usr/bin/python
# _*_ coding: UTF-8 _*_

import configparser
from selenium import webdriver
import os



class Driver(object):
    def __init__(self):
        config=configparser.ConfigParser()
      #  config = ConfigParser.ConfigParser()
      #   print(os.getcwd() + "/../lib/conf.ini")
        config.read(filenames=os.getcwd() + "/../lib/conf.ini")
        config.options("baseconf")
        self.ip_address=config.get("baseconf","ip")
        print("ip",self.ip_address)

        self.port=config.get("baseconf","port")
        #print 'port:',port

        self.user=config.get("baseconf","user")
        #print 'user:',user

        self.password=config.get("baseconf","password")
        #print 'password:',password


        # driver.find_element_by_class_name("fa-sign-out").click()

    def close(self):
        self.driver.quit()

    def open(self):
        #self.driver = webdriver.Firefox()
        self.driver = webdriver.Chrome()
        self.url = "http://" + self.ip_address + ":" + self.port
        self.driver.get(self.url)

        self.driver.find_element_by_xpath("//input[@type='text']").send_keys(self.user)
        self.driver.find_element_by_xpath("//input[@type='password']").send_keys(self.password)

        self.driver.find_element_by_id("loginBtn").click()
