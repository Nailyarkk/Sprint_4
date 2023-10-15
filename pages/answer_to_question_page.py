from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver
class AnswerToQuestion(BasePage):

    cook = (By.XPATH,"//button[text()='да все привыкли']")
    question0_loc = (By.XPATH, '//*[@id="accordion__heading-0"]')
    answer0_loc = (By.XPATH, '//*[@id="accordion__panel-0"]/p')
    question1_loc = (By.XPATH, '//*[@id="accordion__heading-1"]')
    answer1_loc = (By.XPATH, '//*[@id="accordion__panel-1"]/p')
    question2_loc = (By.XPATH, '//*[@id="accordion__heading-2"]')
    answer2_loc = (By.XPATH, '//*[@id="accordion__panel-2"]/p')
    question3_loc = (By.XPATH, '//*[@id="accordion__heading-3"]')
    answer3_loc = (By.XPATH, '//*[@id="accordion__panel-3"]/p')
    question4_loc = (By.XPATH, '//*[@id="accordion__heading-4"]')
    answer4_loc = (By.XPATH, '//*[@id="accordion__panel-4"]/p')
    question5_loc = (By.XPATH, '//*[@id="accordion__heading-5"]')
    answer5_loc =(By.XPATH, '//*[@id="accordion__panel-5"]/p')
    question6_loc = (By.XPATH, '//*[@id="accordion__heading-6"]')
    answer6_loc = (By.XPATH, '//*[@id="accordion__panel-6"]/p')
    question7_loc = (By.XPATH, '//*[@id="accordion__heading-7"]')
    answer7_loc = (By.XPATH, '//*[@id="accordion__panel-7"]/p')

    def find_element(self, by, value):
        return self.driver.find_element(by, value)

    def find_question_element(self, question_loc):
        return self.find_element(*question_loc)

    def get_element_text(self, element_loc):
        element = self.find_element(*element_loc)
        return element.text

    def scroll_into_view(self, element):
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()






