from operator import contains
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import time
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options


chromeOptions = Options()
# chromeOptions.add_argument("--kiosk")
chromeOptions.add_argument("--start-maximized")

# options.add_argument("--user-data-dir=chrome-data")
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option('useAutomationExtension', False)

# driver = webdriver.Chrome(executable_path='C:/Program Files (x86)/chromedriver.exe')
driver = webdriver.Chrome(options=chromeOptions)
driver.implicitly_wait(0.5)


def Login(email, password):
    driver.get('https://app.pixelfy.me/sign-in')
    email_id = driver.find_element_by_id("email")
    password_id = driver.find_element_by_id("password")
    email_id.clear()
    password_id.clear()
    email_id.send_keys(email)
    password_id.send_keys(password)
    # email.send_keys(Keys.RETURN)
    signin = driver.find_element_by_id('sign-in-form-button')
    signin.click()

def Modify_Tracking_links(link_name, sheetUrls):
    link_url = driver.find_element_by_link_text('My Tracking Links').get_attribute("href")
    driver.get(link_url)
    link_name_url = driver.find_element(By.XPATH, '//a[text()="'+link_name+'"]').get_attribute("href")
    name_id = link_name_url.split('trlinkID=')
    url = "/edit-tracking-links?trlinkID="+name_id[1]
    edit_icon = driver.find_element(By.XPATH, '//a[@href="'+url+'"]')
    edit_icon.click()
    url = 31
    # input_tag = driver.find_element_by_xpath('/label[@label="Destination URL 31"]')
    url = "Destination URL " + str(url)
    input_tag = driver.find_element_by_xpath('//label[contains(text(),"'+url+'"]')
    # input_tag = driver.find_element_by_xpath('//div[@label="Destination URL "+' +str(url)+ '"]')


    containers = driver.find_elements_by_xpath('//div[@class="col-md-12 addinput position-relative"]')
    total_urls_to_update = len(sheetUrls)
    total_avalilable_urls = len(containers)

    if total_urls_to_update <= total_avalilable_urls:
        for index in range(0, total_urls_to_update):
            input_tag = containers[index].find_element_by_xpath(".//fieldset//input[@type='text']")
            get_url = input_tag.get_attribute("value")
            if get_url != sheetUrls[index]:
                input_tag.clear()
                input_tag.send_keys(sheetUrls[index])
        save_button = driver.find_element_by_id("form-submit")
        save_button.click()
    elif total_urls_to_update > total_avalilable_urls:
        for index in range(0, total_avalilable_urls):
            input_tag = containers[index].find_element_by_xpath(".//fieldset//input[@type='text']")
            get_url = input_tag.get_attribute("value")
            if get_url != sheetUrls[index]:
                input_tag.clear()
                input_tag.send_keys(sheetUrls[index])
        for index in range(total_avalilable_urls, total_urls_to_update):
            url = index + 1
            add_field = driver.find_element_by_id("addFieldBtn")
            add_field.click()
            input_tag = driver.find_element_by_xpath("//label[contains(text(),'Destination URL 31')]")

        save_button = driver.find_element_by_id("form-submit")
        save_button.click()










    # element = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
    #     (By.XPATH, '//a[text()="Test 3"]')))
        # (By.XPATH, "//span[contains(@class, 'md_countryName_fdxiah8') and text()='Colombia']")))





if __name__ == "__main__":
    Login('lap318181@gmail.com', 'ZEV4JY901n7')
    urls =  ['https://www.facebook.com/101', 'https://www.facebook.com/102', 'https://www.facebook.com/103',
                 'https://www.facebook.com/104', 'https://www.facebook.com/105', 'https://www.facebook.com/106',
                 'https://www.facebook.com/107', 'https://www.facebook.com/108', 'https://www.facebook.com/109',
                 'https://www.facebook.com/110', 'https://www.facebook.com/111', 'https://www.facebook.com/112',
                 'https://www.facebook.com/113', 'https://www.facebook.com/114', 'https://www.facebook.com/115',
                 'https://www.facebook.com/116', 'https://www.facebook.com/117', 'https://www.facebook.com/118',
                 'https://www.facebook.com/119', 'https://www.facebook.com/120', 'https://www.facebook.com/121',
                 'https://www.facebook.com/122', 'https://www.facebook.com/123', 'https://www.facebook.com/124',
                 'https://www.facebook.com/125', 'https://www.facebook.com/126', 'https://www.facebook.com/127',
                 'https://www.facebook.com/128', 'https://www.facebook.com/129', 'https://www.facebook.com/130']

    Modify_Tracking_links("Test 3", urls)




