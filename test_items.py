from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import pytest
from selenium.webdriver.support.ui import WebDriverWait

def test_page_contains_add_to_cart_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)
    
    # select=browser.find_element_by_css_selector("[value="'en-gb'"]").click()
    # browser.find_element_by_class_name("page_inner").click()

    # browser.find_element(By.CSS_SELECTOR, "#language_selector button").click()


    button= browser.find_elements(By.CSS_SELECTOR, "#add_to_basket_form button")
    assert 'page does not contains add to cart button'

