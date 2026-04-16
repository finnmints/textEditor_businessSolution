from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()

#Go to website
driver.get("https://www.imdb.com/chart/top/?ref_=chttvtp_nv_menu")
time.sleep(1)


#Find the menu button
menu = driver.find_element(By.ID, "imdbHeader-navDrawerOpen")

#Set up the hover setting (move_to_element)
hover = ActionChains(driver).move_to_element(menu)

tv = driver.find_element(By.Class, "ipc-list-item__text")

#Set up the hover setting (move_to_element)
hover2 = ActionChains(driver).move_to_element(tv)


hover.perform()
time.sleep(2)
jokeButton.click()
time.sleep(3)


jokeButton.click()
time.sleep(3)
jokeButton.click()

time.sleep(3)
jokeButton.click()


time.sleep(4)



driver.quit()