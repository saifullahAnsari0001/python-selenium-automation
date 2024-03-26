import requests
import  time
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pynput.keyboard import Key, Controller
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logging.basicConfig(filename= "C:/Users/ammar/PycharmProjects/pythonProject/log_script/test_log.txt",
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

s = Service("C:/Users/ammar/OneDrive/Desktop/chromedriver.exe")
driver = webdriver.Chrome(service=s)

url = "https://atg.party/"
driver.get("https://atg.party/")


start_time = time.time()
driver.get(url)
end_time = time.time()
response_time = end_time - start_time
logger.info(f"Page load time: {response_time:.2f} seconds")

http_response_code = driver.execute_script("return window.performance.timing.responseStart !== 0 ? 200 : 400")
logger.info(f"HTTP response code: {http_response_code}")


if http_response_code == 200:

    driver.find_element(By.XPATH,"""/html/body/div[5]/header/div[1]/div/div/div[2]/div/div/div/div/div/div/div/div/div[1]/div/div/p/span""").click()

    email_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "email_landing")))
    email_input.send_keys("wiz_saurabh@rediffmail.com")
    password_input = driver.find_element(By.ID, "password_landing")
    password_input.send_keys("Pass@123")

    login_button = driver.find_element(By.XPATH,"""/html/body/div[5]/header/div[1]/div/div/div[2]/div/div/div/div/div/div/div/div/div[2]/div/form/div[3]/button""")
    login_button.click()
    time.sleep(2)

    driver.get("https://atg.party/article")

    title_input = driver.find_element(By.ID, "title")
    title_input.send_keys("python selenium and basic linux awareness test")
    description_input = driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div/div[2]/form/div/div/div[2]/div/div/div/div[1]/div/div/div")
    description_input.send_keys("i have successfully done this test")

    driver.find_element(By.ID, "add-cover-image").click()
    time.sleep(2)
    keyboard = Controller()
    keyboard.type("C:\\Users\\ammar\\OneDrive\\Desktop\\images.jpg")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(2)

    post_button = driver.find_element(By.ID, "hpost_btn")
    post_button.click()

    new_page_url = driver.current_url
    logger.info(f"New page URL: {new_page_url}")
    time.sleep(2)

else:
    logger.error(f"HTTP response code: {http_response_code}")

driver.quit()

