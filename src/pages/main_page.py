import allure
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ReqresPage:

    listResource = (By.XPATH, "//*[@data-id='unknown']")

    driver = None

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://reqres.in")
        return self

    def clickOnListResource(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(ReqresPage.listResource)).click()

    def at_page(self):
        return "Reqres - A hosted REST-API ready to respond to your AJAX requests" in self.driver.title

    def get_json_by_id(self):
        respond = self.driver.find_element_by_xpath("//*[@data-key='output-response']").text
        resp = json.loads(respond)
        for i in resp['data']:
            if i['id'] == 2:
                return i
        return None




