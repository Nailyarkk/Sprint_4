from selenium.webdriver.common.by import By
from constants import *
import allure

class FillFormSecond():
    date = (By.XPATH, "//input[@class='Input_Input__1iN_Z Input_Responsible__1jDKN' and @placeholder='* Когда привезти самокат' and @value='']")
    date_def = (By.XPATH, "//div[contains(@class, 'react-datepicker__day') and contains(@class, 'react-datepicker__day--028') and contains(@class, 'react-datepicker__day--weekend') and starts-with(@aria-label, 'Choose суббота, 28-е октября 2023 г.')]")
    time = (By.XPATH, "//div[@class='Dropdown-control' and @aria-haspopup='listbox']//div[@class='Dropdown-placeholder'][text()='* Срок аренды']")
    time_def = (By.XPATH, "//div[@class='Dropdown-option' and @role='option' and @aria-selected='false' and text()='двое суток']")
    color = (By.XPATH, "//input[@id='black' and @class='Checkbox_Input__14A2w' and @type='checkbox']")
    comment = (By.XPATH, "//input[@class='Input_Input__1iN_Z Input_Responsible__1jDKN' and @placeholder='Комментарий для курьера' and @type='text']")
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Находим поле даты доставки и выбираем дату')
    def fill_date(self):
        self.driver.find_element(*self.date).click()
        self.driver.find_element(*self.date_def).click()
    @allure.step('Находим поле срока аренды и выбираем срок')
    def fill_time(self):
        self.driver.find_element(*self.time).click()
        self.driver.find_element(*self.time_def).click()
    @allure.step('Находим поле выбора цвета и выбираем цвет')
    def fill_color(self):
        self.driver.find_element(*self.color).click()
    @allure.step('Находим поле комментария и вводим комментарий')
    def fill_comment(self):
        self.driver.find_element(*self.comment).send_keys(comment_form)

    def fill_form_order(self):
        self.fill_date()
        self.fill_time()
        self.fill_color()
        self.fill_comment()

