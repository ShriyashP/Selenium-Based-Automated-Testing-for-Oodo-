from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

def login(url):
    driver.get(url)
    driver.find_element_by_name("login").send_keys("admin")
    driver.find_element("name", "password").send_keys("admin", Keys.RETURN)
    time.sleep(10)


def create_vendor():
    driver.get("http://localhost:8069/web#cids=1&menu_id=313&action=442&model=lunch.product&view_type=kanban")
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/header/nav/div[2]/div[3]/button").click()
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/header/nav/div[2]/div[3]/div/a[2]").click()
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[2]/div[1]/div/div/button").click()
    time.sleep(2)
    driver.find_element_by_xpath(
        "/html/body/div[1]/div/div[2]/div/div[1]/div/div[3]/table[1]/tbody/tr[1]/td[2]/div/div[1]/div/input").send_keys(
        "Shriyash")
    driver.find_element_by_xpath(
        "/html/body/div[1]/div/div[2]/div/div[1]/div/div[3]/table[1]/tbody/tr[1]/td[2]/div/div[1]/div/input").send_keys(
        Keys.RETURN)
    time.sleep(2)
    driver.find_element_by_xpath(
        ("/html/body/div[1]/div/div[2]/div/div[1]/div/div[3]/table[2]/tbody/tr[3]/td[2]/input")).send_keys("99898")
    driver.find_element_by_xpath(
        ("/html/body/div[1]/div/div[2]/div/div[1]/div/div[3]/table[2]/tbody/tr[3]/td[2]/input")).send_keys(Keys.RETURN)
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[2]/div[1]/div/div/div[2]/button[1]").click()
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div[1]/ol/li[1]/a").click()



login("http://localhost:8069/web/login")
create_vendor()
print("\nTest is Pass")
time.sleep(5)
driver.quit()