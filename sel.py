# -*- coding: utf-8 -*-
"""
Created on Wed May 17 14:24:02 2018

@author: Ruslan
"""

import time
from selenium import webdriver
import urllib.request
from PIL import Image

url = "https://www.instagram.com/"
username = "test617621535176"
userpass = "jdsoi2139ur38r38ru3893r2j9"
query = "#sea"
imagelist = []
driver = webdriver.Chrome()


def login():
    driver.implicitly_wait(10)
    buttonLogin = driver.find_element_by_xpath(
        '//article/div/div/p/a[text()="Вход"]')

    buttonLogin.click()
    driver.implicitly_wait(10)

    driver.find_element_by_name("username").send_keys(username)
    driver.find_element_by_name("password").send_keys(userpass)
    buttonEnter = driver.find_element_by_xpath(
        '//form/span/button[text()="Войти"]')
    buttonEnter.click()
    search()
    


def search():
    driver.implicitly_wait(10)
    driver.find_element_by_css_selector("._avvq0._o716c").send_keys(query)
    driver.find_element_by_css_selector("._ndl3t").click()
    elementh1 = driver.find_element_by_class_name("_8zv80")
    if elementh1.text == query:
       safe()
    
        
    
def safe():
    driver.implicitly_wait(10)
    for image in driver.find_elements_by_tag_name('img'):
        imagelist.append(image.get_attribute('src'))
        
    urllib.request.urlretrieve(imagelist[1], "image.png")
    convertToBinary()

       
    
def convertToBinary():
    col = Image.open("image.png")
    gray = col.convert('L')  
    bw = gray.point(lambda x: 0 if x<128 else 255, '1')  
    bw.save("Test_Worked..png")



def main():
    driver.get(url)
    login()
    time.sleep(60)
    driver.quit()

if __name__ == '__main__':
    main()
