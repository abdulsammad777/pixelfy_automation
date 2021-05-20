from operator import contains
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import time
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

options = webdriver.ChromeOptions()
# options = Options()
# options.add_argument(user_profile_path)
# options.add_argument("--user-data-dir=chrome-data")
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option('useAutomationExtension', False)

# options.add_argument("user-data-dir=C:\\Users\\Abdul samad\\AppData\\Local\\Google\\Chrome\\Default")

# driver = webdriver.Chrome(executable_path='C:/Program Files (x86)/chromedriver.exe')
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(0.5)
# driver.maximize_window()
# driver.get('https://pixelfy.me/')
driver.get('https://app.pixelfy.me/sign-in')

def Login(email, password):
    email_id = driver.find_element_by_id("email")
    password_id = driver.find_element_by_id("password")
    email_id.clear()
    password_id.clear()
    email_id.send_keys(email)
    password_id.send_keys(password)
    # email.send_keys(Keys.RETURN)
    signin = driver.find_element_by_id('sign-in-form-button')
    signin.click()

def Modify_Tracking_links(link_name, sheetUrl):
    link_url = driver.find_element_by_link_text('My Tracking Links').get_attribute("href")
    driver.get(link_url)
    link_name_url = driver.find_element(By.XPATH, '//a[text()="'+link_name+'"]').get_attribute("href")
    name_id = link_name_url.split('trlinkID=')
    url = "/edit-tracking-links?trlinkID="+name_id[1]
    edit_icon = driver.find_element(By.XPATH, '//a[@href="'+url+'"]')
    edit_icon.click()
    Add_url = driver.find_element(By.XPATH, '//a[text()="Add destination Url "]')
    Add_url.click()

    # containers = driver.find_elements_by_xpath('//div[@class="row fields-add px-4 rotator-link"]')
    containers = driver.find_elements_by_xpath('//div[@class="col-md-12 addinput position-relative"]')

    containers.text().split()

    # element = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
    #     (By.XPATH, '//a[text()="Test 3"]')))
        # (By.XPATH, "//span[contains(@class, 'md_countryName_fdxiah8') and text()='Colombia']")))
    for items in containers:
        name = items.find_element_by_xpath('//div[@class="name"]')
        print(name.text)
    a = 0




if __name__ == "__main__":
    Login('lap318181@gmail.com', 'ZEV4JY901n7')
    Modify_Tracking_links("Test 3", "sdfsdfsdfsd")




