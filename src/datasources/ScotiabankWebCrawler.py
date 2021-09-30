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
        try:
            # Open the page
            self.driver.get(self.login_url)

            self.login()

            consultas_href = self.wait_presence_xpath(
                "/html/body/div[11]/div[2]/div[2]/ul/li[1]/a"
            )
            ActionChains(self.driver).move_to_element(consultas_href).perform()

            self.wait_clickable_xpath(
                "/html/body/div[11]/div[2]/div[2]/ul/li[1]/ul/li[3]/a"
            ).click()

            attempts = 0
            while attempts < 10:
                try:
                    attempts += 1
                    self.wait_clickable_xpath(
                        '//*[@id="CuentaOrigenIdLista_chosen"]'
                    ).click()
                    break
                except:
                    if attempts == 10:
                        raise Exception("Too many attempts!")

            self.wait_clickable_xpath(
                "/html/body/div[11]/div[2]/div[2]/div[1]/form/fieldset/div/table[2]/tbody/tr[1]/td[2]/div/div/ul/li[4]"
            ).click()

        except FileNotFoundError as e:
            print(e)
            pass

        # finally:
        #     try:
        #         self.wait_clickable_xpath('//*[@id="exit"]').click()
        #     except:
        #         pass

        #     self.driver.close()

    def login(self):
        self.driver.find_element_by_xpath('//*[@id="UserName"]').send_keys(
            self.username
        )
        self.driver.find_element_by_xpath('//*[@id="_Password"]').send_keys(
            self.password
        )
        self.driver.find_element_by_xpath('//*[@id="btnIngresar"]').click()

    def extract(self) -> DataFrame:
        return super().extract()

    def wait_presence_xpath(self, xpath, timeout=30):
        return WebDriverWait(self.driver, timeout=timeout).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )

    def wait_clickable_xpath(self, xpath, timeout=30):
        return WebDriverWait(self.driver, timeout=timeout).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )
