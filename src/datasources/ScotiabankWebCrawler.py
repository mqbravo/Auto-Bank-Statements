from pandas.core.frame import DataFrame
from selenium.webdriver import Firefox
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from datasources.Datasource import Datasource


class ScotiabankWebCrawler(Datasource):
    def __init__(self) -> None:
        self.driver = Firefox()
        self.login_url = "https://scotiaenlinea.scotiabank.fi.cr/IB/Account/LogOn"
        self.username = ""
        self.password = ""

    def crawl(self):
        # Open the page
        self.driver.get(self.login_url)

        self.login()

        consultas_href = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[11]/div[2]/div[2]/ul/li[1]/a")
            )
        )
        ActionChains(self.driver).move_to_element(consultas_href).perform()

        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[11]/div[2]/div[2]/ul/li[1]/ul/li[3]/a")
            )
        ).click()

    def login(self):
        self.driver.find_element_by_xpath('//*[@id="UserName"]').send_keys(
            self.username
        )
        self.driver.find_element_by_xpath('//*[@id="_Password"]').send_keys(
            self.password
        )
        self.driver.find_element_by_xpath('//*[@id="btnIngresar"]').login_button.click()

    def extract(self) -> DataFrame:
        return super().extract()
