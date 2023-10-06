from selenium.webdriver.common.by import By
from constants import *
import allure

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def click_element(self, *locator):
        self.find_element(*locator).click()

    def send_keys(self, *locator, value):
        element = self.find_element(*locator)
        element.clear()
        element.send_keys(value)

class FillFormFirst(BasePage):
    name = (By.XPATH, "//input[@placeholder='* Имя']")
    lastname = (By.XPATH, "//input[@placeholder='* Фамилия']")
    address = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    stmetro = (By.XPATH, "//input[@placeholder='* Станция метро']")
    number = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    button_dalee = (By.XPATH, "//button[text()='Далее']")



    @allure.step('Находим поле для ввода имени и вводим имя')
    def fill_name(self):
        self.send_keys(self.name, value=name_form)

    @allure.step('Находим поле для ввода фамилии и вводим фамилию')
    def fill_lastname(self):
        self.send_keys(self.lastname, value=lastname_form)

    @allure.step('Находим поле для ввода адреса и вводим адрес')
    def fill_address(self):
        self.send_keys(self.address, value=address_form)

    @allure.step('Находим поле для выбора метро и вводим название')
    def fill_stmetro(self):
        self.send_keys(self.stmetro, value=stmetro_form)

    @allure.step('Находим поле для ввода номера телефона и вводим номер телефона')
    def fill_number(self):
        self.send_keys(self.number, value=number_form)



    @allure.step('Находим кнопку "далее" и нажимаем на нее')
    def click_button(self):
        self.click_element(self.button_dalee)


    def fill_form_and_click_button(self):
        self.fill_name()
        self.fill_lastname()
        self.fill_address()
        self.fill_stmetro()
        self.fill_number()
        self.click_button()
