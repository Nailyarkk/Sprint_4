import pytest
from constants import *
from pages.answer_to_question_page import AnswerToQuestion
import allure

class TestAnswerToQuestion:
    @pytest.mark.parametrize("question_loc, answer_to_question_loc, answer_to_question_text", [
        (AnswerToQuestion.question0_loc, AnswerToQuestion.answer0_loc, answer_to_question0),
        (AnswerToQuestion.question1_loc, AnswerToQuestion.answer1_loc, answer_to_question1),
        (AnswerToQuestion.question2_loc, AnswerToQuestion.answer2_loc, answer_to_question2),
        (AnswerToQuestion.question3_loc, AnswerToQuestion.answer3_loc, answer_to_question3),
        (AnswerToQuestion.question4_loc, AnswerToQuestion.answer4_loc, answer_to_question4),
        (AnswerToQuestion.question5_loc, AnswerToQuestion.answer5_loc, answer_to_question5),
        (AnswerToQuestion.question6_loc, AnswerToQuestion.answer6_loc, answer_to_question6),
        (AnswerToQuestion.question7_loc, AnswerToQuestion.answer7_loc, answer_to_question7)
     ])
    @allure.description(
        'На странице ищем выпадающие вопросы, нажимаем на стрелочку, открывается соответствующий текст проверяем')
    def test_answer_to_questions(self, driver, question_loc, answer_to_question_loc, answer_to_question_text):
        answer_to_question_page = AnswerToQuestion(driver)
        driver.get(url)

        answer_to_question_page.find_element(*answer_to_question_page.cook).click()

        dropdown = answer_to_question_page.find_question_element(question_loc)
        answer_to_question_page.scroll_into_view(dropdown)
        dropdown.click()

        answer_text = answer_to_question_page.get_element_text(answer_to_question_loc)
        assert answer_text == answer_to_question_text
