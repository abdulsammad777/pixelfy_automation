from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
chromeOptions = Options()
chromeOptions.add_argument("--start-maximized")
chromeOptions.add_experimental_option("detach", True)
chromeOptions.add_experimental_option('useAutomationExtension', False)


# driver = webdriver.Chrome(executable_path='C:/Program Files (x86)/chromedriver.exe')
driver = webdriver.Chrome(options=chromeOptions)
# executor_url = driver.command_executor._url
# session_id = driver.session_id
driver.implicitly_wait(0.5)
# driver = webdriver.Remote(command_executor=executor_url, desired_capabilities={})
# driver.close()   # this prevents the dummy browser
# driver.session_id = session_id

def check_login(get_current_url):
    # driver.refresh()
    if get_current_url == 'https://app.pixelfy.me/dashboard':
        return True
    else:
        return False
def Login(email, password):
    driver.get('https://app.pixelfy.me/sign-in')
    get_current_url = driver.current_url
    if check_login(get_current_url) is False:
        try:
            email_id = driver.find_element_by_id("email")
            password_id = driver.find_element_by_id("password")
            email_id.clear()
            password_id.clear()
            email_id.send_keys(email)
            password_id.send_keys(password)
            # email.send_keys(Keys.RETURN)
            signin = driver.find_element_by_id('sign-in-form-button')
            signin.click()
        except Exception as e:
            print(e, 'Found This Error')
def Modify_Tracking_links(sheetUrls, link_name):
    link_url = driver.find_element_by_link_text('My Tracking Links').get_attribute("href")
    driver.get(link_url)
    link_name_url = driver.find_element(By.XPATH, '//a[text()="'+link_name+'"]').get_attribute("href")
    name_id = link_name_url.split('trlinkID=')
    url = "/edit-tracking-links?trlinkID="+name_id[1]
    edit_icon = driver.find_element(By.XPATH, '//a[@href="'+url+'"]')
    edit_icon.click()

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
    elif total_urls_to_update > total_avalilable_urls and containers != []:
        for index in range(0, total_avalilable_urls):
            input_tag = containers[index].find_element_by_xpath(".//fieldset//input[@type='text']")
            get_url = input_tag.get_attribute("value")
            if get_url != sheetUrls[index]:
                input_tag.clear()
                input_tag.send_keys(sheetUrls[index])
        for index in range(total_avalilable_urls, total_urls_to_update):
            # url_no = index + 1
            add_field = driver.find_element_by_id("addFieldBtn")
            add_field.click()
            # url = "Destination URL " + str(url_no)
            # input_tag = driver.find_element_by_xpath("//label[contains(text(),'"+url+"')]")
            containers = driver.find_elements_by_xpath('//div[@class="col-md-12 addinput position-relative"]')
            containers[-1].find_element_by_xpath(
                ".//div//select[@class='form-control selectron']/option[@value='0']").click()
            input_tag = containers[-1].find_element_by_xpath(".//div//input[@type='text']")
            input_tag.clear()
            input_tag.send_keys(sheetUrls[index])
        save_button = driver.find_element_by_id("form-submit")
        save_button.click()
    elif containers == []:
        for index in range(total_urls_to_update):
            add_field = driver.find_element_by_id("addFieldBtn")
            add_field.click()
            containers = driver.find_elements_by_xpath('//div[@class="col-md-12 addinput position-relative"]')
            containers[-1].find_element_by_xpath(
                ".//div//select[@class='form-control selectron']/option[@value='0']").click()
            input_tag = containers[-1].find_element_by_xpath(".//div//input[@type='text']")
            input_tag.clear()
            input_tag.send_keys(sheetUrls[index])
        save_button = driver.find_element_by_id("form-submit")
        save_button.click()



    # element = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
    #     (By.XPATH, '//a[text()="Test 3"]')))
        # (By.XPATH, "//span[contains(@class, 'md_countryName_fdxiah8') and text()='Colombia']")))





if __name__ == "__main__":
    Login('lap318181@gmail.com', 'ZEV4JY901n7')
    urls = ['https://www.facebook.com/101', 'https://www.facebook.com/102', 'https://www.facebook.com/103',
                 'https://www.facebook.com/104', 'https://www.facebook.com/105', 'https://www.facebook.com/106',
                 'https://www.facebook.com/107', 'https://www.facebook.com/108', 'https://www.facebook.com/109',
                 'https://www.facebook.com/110', 'https://www.facebook.com/111', 'https://www.facebook.com/112',
                 'https://www.facebook.com/113', 'https://www.facebook.com/114', 'https://www.facebook.com/115',
                 'https://www.facebook.com/116', 'https://www.facebook.com/117', 'https://www.facebook.com/118',
                 'https://www.facebook.com/119', 'https://www.facebook.com/120', 'https://www.facebook.com/121',
                 'https://www.facebook.com/122', 'https://www.facebook.com/123', 'https://www.facebook.com/124',
                 'https://www.facebook.com/125', 'https://www.facebook.com/126', 'https://www.facebook.com/127',
                 'https://www.facebook.com/128', 'https://www.facebook.com/129', 'https://www.facebook.com/130',
                'https://www.facebook.com/113', 'https://www.facebook.com/114', 'https://www.facebook.com/115',
                'https://www.facebook.com/116', 'https://www.facebook.com/117', 'https://www.facebook.com/118',
                'https://www.facebook.com/119', 'https://www.facebook.com/120', 'https://www.facebook.com/121',
                'https://www.facebook.com/122', 'https://www.facebook.com/123', 'https://www.facebook.com/124',
                'https://www.facebook.com/125', 'https://www.facebook.com/126', 'https://www.facebook.com/127',
                'https://www.facebook.com/128', 'https://www.facebook.com/129', 'https://www.facebook.com/130']

    Modify_Tracking_links(urls, "Test 3")




