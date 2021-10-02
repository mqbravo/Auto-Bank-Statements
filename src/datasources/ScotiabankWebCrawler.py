from pandas.core.frame import DataFrame
from selenium.webdriver import Firefox
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from datasources.Datasource import Datasource
from selenium.webdriver.support.ui import Select
from time import sleep
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile


class ScotiabankWebCrawler(Datasource):
    def __init__(self) -> None:
        self.login_url = "https://scotiaenlinea.scotiabank.fi.cr/IB/Account/LogOn"
        self.username = ""
        self.password = ""

        self.output_path = ""

        profile = FirefoxProfile()
        profile.set_preference("browser.download.panel.shown", False)
        profile.set_preference(
            "browser.helperApps.neverAsk.openFile", "text/csv,application/vnd.ms-excel"
        )
        profile.set_preference(
            "browser.helperApps.neverAsk.saveToDisk",
            "text/csv,application/vnd.ms-excel",
        )
        profile.set_preference("browser.download.folderList", 2)

        self.driver = Firefox(firefox_profile=profile)

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

            self.attempt_clicks('//*[@id="CuentaOrigenIdLista_chosen"]')

            self.wait_clickable_xpath(
                "/html/body/div[11]/div[2]/div[2]/div[1]/form/fieldset/div/table[2]/tbody/tr[1]/td[2]/div/div/ul/li[4]"
            ).click()

            sleep(3)

            select = Select(self.wait_clickable_xpath('//*[@id="TipoConsultaId"]'))
            select.select_by_value("AM")

            self.wait_clickable_xpath(
                "/html/body/div[11]/div[2]/div[2]/div[1]/div/div/table[2]/tbody/tr/td[1]/div/p/a"
            ).click()

            # Wait for download
            sleep(6)

        except Exception as e:
            print(e)

        finally:
            try:
                logout_button = self.wait_clickable_xpath(
                    "/html/body/div[11]/div[1]/div[1]"
                )

                self.driver.execute_script("arguments[0].click();", logout_button)

                sleep(3)
            except Exception as e:
                print(e)
                pass

            self.driver.quit()

    def login(self):
        self.wait_presence_xpath('//*[@id="UserName"]').send_keys(self.username)
        self.wait_presence_xpath('//*[@id="_Password"]').send_keys(self.password)
        self.wait_presence_xpath('//*[@id="btnIngresar"]').click()

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

    def attempt_clicks(self, xpath, max_attempts=10):
        attempts = 0
        while attempts < max_attempts:
            try:
                attempts += 1
                self.wait_clickable_xpath(xpath).click()
                break
            except:
                if attempts == max_attempts:
                    raise Exception("Too many attempts!")
