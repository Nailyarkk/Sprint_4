from selenium.webdriver.common.by import By
from constants import *
import allure

class FillFormFirst():
    name = (By.XPATH, "//input[@class='Input_Input__1iN_Z Input_Error__1Tx5d Input_Responsible__1jDKN' and @placeholder='* Имя' and @type='text']")
    lastname = (By.XPATH, "//input[@class='Input_Input__1iN_Z Input_Error__1Tx5d Input_Responsible__1jDKN' and @placeholder='* Фамилия' and @type='text']")
    address = (By.XPATH, "//input[@class='Input_Input__1iN_Z Input_Responsible__1jDKN' and @placeholder='* Адрес: куда привезти заказ' and @type='text']")
    stmetro = (By.XPATH, "//input[@class='select-search__input' and @tabindex='0' and @placeholder='* Станция метро' and @autocomplete='on']")
    number = (By.XPATH, "//input[@class='Input_Input__1iN_Z Input_Responsible__1jDKN' and @placeholder='* Телефон: на него позвонит курьер' and @type='text']")
    button_dalee = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Далее']")

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Находим поле для ввода имени и вводим имя')
    def fill_name(self):
        self.driver.find_element(*self.name).send_keys(name_form)

    @allure.step('Находим поле для ввода фамиии и вводим фамилию')
    def fill_lastname(self):
        self.driver.find_element(*self.lastname).send_keys(lastname_form)

    @allure.step('Находим поле для ввода адреса и вводим адрес')
    def fill_address(self):
        self.driver.find_element(*self.address).send_keys(address_form)

    @allure.step('Находим поле для выбора метра и вводим название')
    def fill_stmetro(self):
        self.driver.find_element(*self.stmetro).send_keys(stmetro_form)

    @allure.step('Находим поле для ввода номера телефона и вводим номер телефона')
    def fill_number(self):
        self.driver.find_element(*self.number).send_keys(number_form)

    @allure.step('Находим кнопку "далее" и нажимаем на нее')
    def click_button(self):
        self.driver.find_element(*self.button_dalee).click()

    def fill_form_and_click_button(self):
        self.fill_name()
        self.fill_lastname()
        self.fill_address()
        self.fill_stmetro()
        self.fill_number()
        self.click_button()

