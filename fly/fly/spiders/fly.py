# -*- coding: utf-8 -*-
import sys
import os
import inspect


currentdir = os.path.dirname(os.path.realpath(inspect.getfile(lambda: None)))
parentdir = os.path.dirname(os.path.dirname(os.path.dirname(currentdir)))
sys.path.append(parentdir)

import scrapy
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers.step import StepHelper


class FlySpider(scrapy.Spider):
    name = 'fly'
    DEPARTURE_FIELD = "//input[@placeholder='Departure']"
    ARRIVED_FIELD = "//input[@placeholder='Arrival']"
    step = StepHelper()


    def start_requests(self):
        yield SeleniumRequest(
            url="https://www.flyuia.com/ua/en/home",
            wait_time=5,
            screenshot=True,
            callback=self.parse,
        )

    def input_text(self, how, locator, text, webdriver):
        wd = webdriver
        element = WebDriverWait(wd, 10).until(
            EC.visibility_of_element_located((how, locator)))
        element.clear()
        element.send_keys(text)


    def parse(self, response):
        driver = response.meta['driver']
        book_flights_button = driver.find_element_by_xpath("//span[text()='Book flights']")
        book_flights_button.click()
        one_way_button = driver.find_element_by_xpath("//button[text()=' One way ']")
        one_way_button.click()
        self.step.input_text(self.DEPARTURE_FIELD, "AAAA", driver)
        driver.save_screenshot('asd.png')
        # time.sleep(1)
        # self.step.wait_for_element(self.DEPARTURE_FIELD).send_keys(Keys.ARROW_DOWN)
        # self.step.wait_for_element(self.DEPARTURE_FIELD).send_keys(Keys.ENTER)
        # self.step.input_text(self.ARRIVED_FIELD, to)
        # time.sleep(1)
        # self.step.wait_for_element(self.ARRIVED_FIELD).send_keys(Keys.ARROW_DOWN)
        # self.step.wait_for_element(self.ARRIVED_FIELD).send_keys(Keys.ENTER)