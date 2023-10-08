from selenium.webdriver.common.by import By
from constants import *
import allure
from base_page import BasePage

class FillFormSecond(BasePage):
    date = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    date_def = (By.XPATH, "//div[@aria-label='Choose суббота, 28-е октября 2023 г.']")
    time = (By.CLASS_NAME, "Dropdown-placeholder")
    time_def = (By.XPATH, "//div[@class='Dropdown-option'][text()='двое суток']")
    color = (By.XPATH, "//input[@id='black']")
    comment = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")

    @allure.step('Находим поле даты доставки и выбираем дату')
    def fill_date(self):
        self.click_element(self.date)
        self.click_element(self.date_def)

    @allure.step('Находим поле срока аренды и выбираем срок')
    def fill_time(self):
        self.click_element(self.time)
        self.click_element(self.time_def)

    @allure.step('Находим поле выбора цвета и выбираем цвет')
    def fill_color(self):
        self.click_element(self.color)

    @allure.step('Находим поле комментария и вводим комментарий')
    def fill_comment(self, comment_text):
        self.send_keys(self.comment, comment_text)

    @allure.step("Заполняем форму заказа")
    def fill_form_order(self):
        self.fill_date()
        self.fill_time()
        self.fill_color()
        self.fill_comment(comment_form)
