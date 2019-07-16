from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from src.pages.main_page import ReqresPage
from src.api.test_api import TestApi


class TestId:

    def setup_method(self):
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        self.mainPage = ReqresPage(self.driver)

    def test_compare_data(self):
        self.mainPage.open()
        assert self.mainPage.at_page()

        self.mainPage.clickOnListResource()
        webItem = self.mainPage.get_json_by_id()
        apiItem = TestApi.json_by_id2(self)
        assert webItem == apiItem

    def teardown_method(self):
        self.driver.close()