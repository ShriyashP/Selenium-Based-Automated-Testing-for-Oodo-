from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support import expected_conditions as EC
import time

from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

def login(url):
    driver.get(url)
    driver.find_element_by_name("login").send_keys("admin")
    driver.find_element("name", "password").send_keys("admin", Keys.RETURN)
    time.sleep(10)


def create_vendor():
    driver.get("http://localhost:8069/web#cids=1&menu_id=313&action=442&model=lunch.product&view_type=kanban")
    time.sleep(5)
    driver.find_element_by_xpath("/html/body/header/nav/div[2]/div[3]/button").click()
    time.sleep(5)
    driver.find_element_by_xpath("/html/body/header/nav/div[2]/div[3]/div/a[2]").click()
    time.sleep(5)
    driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[2]/div[1]/div/div/button").click()
    time.sleep(5)
    driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[2]/div[1]/div/div/div[2]/button[1]").click()
    try:
        notification_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "o_notification_manager"))
        )
        # Handle the notification
        print("Warning is seen, Test Passed")
    except:
        print("Notification did not appear within the timeout period.")




login("http://localhost:8069/web/login")
create_vendor()
time.sleep(5)
driver.quit()