from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains



class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def scroll_into_view(self, element):
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()



    def get_current_url(self):
        return self.driver.current_url

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def wait_for_url_change(self, current_url):
        WebDriverWait(self.driver, 10).until(EC.url_changes(current_url))

    def click_element(self, *locator):
        self.driver.find_element(*locator).click()

    def go_to_url(self, name_url):
        self.driver.get(name_url)



    def send_keys(self, *locator, value):
        element = self.find_element(*locator)
        element.clear()
        element.send_keys(value)

    def get_element_text(self, locator):
        element = self.driver.find_element(*locator)
        return element.text