from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


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

    def enter_element(self):
        self.driver.send_keys(Keys.ENTER)

    def down_element(self):
        self.driver.send_keys(Keys.ARROW_DOWN)

    def go_to_url(self, name_url):
        self.driver.get(name_url)

    def send_keys(self, *locator, value):
        element = self.find_element(*locator)
        element.clear()
        element.send_keys(value)

    def get_element_text(self, locator):
        element = self.driver.find_element(*locator)
        return element.text

    def switch_to_new_window(self):
        main_window = self.driver.current_window_handle
        for window_handle in self.driver.window_handles:
            if window_handle != main_window:
                self.driver.switch_to.window(window_handle)
