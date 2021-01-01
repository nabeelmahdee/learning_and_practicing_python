from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import time

URL = "https://www.google.com/"
exec_path= r'C:\Users\nabee\Downloads\chromedriver_win32\chromedriver.exe'
# username = "admin"
# password = "admin"

# xpaths = { 'usernameTxtBox' : "//input[@name='username']",
#            'passwordTxtBox' : "//input[@name='password']",
#            'submitButton' :   "//input[@name='login']"
#          }

mydriver = webdriver.Chrome(executable_path=exec_path)
mydriver.get(URL)
mydriver.maximize_window()
mydriver.find_element_by_xpath(r'//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input').send_keys('Automation in python')
mydriver.find_element_by_name('btnK').click()
time.sleep(4)
# mydriver.quit()

# #Clear Username TextBox if already allowed "Remember Me" 
# mydriver.find_element_by_xpath(xpaths['usernameTxtBox']).clear()

# #Write Username in Username TextBox
# mydriver.find_element_by_xpath(xpaths['usernameTxtBox']).send_keys(username)

# #Clear Password TextBox if already allowed "Remember Me" 
# mydriver.find_element_by_xpath(xpaths['passwordTxtBox']).clear()

# #Write Password in password TextBox
# mydriver.find_element_by_xpath(xpaths['passwordTxtBox']).send_keys(password)

# #Click Login button
# mydriver.find_element_by_xpath(xpaths['submitButton']).click()




