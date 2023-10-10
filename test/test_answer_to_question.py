import pytest
from constants import *
from pages.answer_to_question_page import AnswerToQuestion
import allure


class TestAnswerToQuestion:

    @pytest.mark.parametrize("question_index", range(8))
    @allure.description(
        'На странице ищем выпадающие вопросы, нажимаем на стрелочку, открывается соответствующий текст и проверяем')
    def test_answer_to_questions(self, question_index):
        answer_to_question_page = AnswerToQuestion(self)
        question_loc = answer_to_question_page.question_loc[question_index]
        answer_to_question_loc = answer_to_question_page.answer_to_question_loc[question_index]

        answer_to_question_text = answer_to_questions[question_index]

        answer_to_question_page.check_answer(question_loc, answer_to_question_loc, answer_to_question_text)
