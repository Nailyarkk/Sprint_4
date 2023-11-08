import pytest
from pages.fill_form_first_page import FillFormFirst
from pages.fill_form_second_page import FillFormSecond
from pages.order_scooter_button_main_page import OrderScooterButton
from pages.success_page import CheckSuccessOrder
from constants import *
import allure


class TestOrderScooter:
    @pytest.mark.parametrize("button_order", [
        OrderScooterButton.button_order1,
        OrderScooterButton.button_order2
    ])
    @allure.description(
        'Заказ самоката. Проверяем весь флоу позитивного сценария')
    def test_order_scooter(self, button_order):
        main_page = OrderScooterButton(self)
        main_page.go_to_url_main(url)
        main_page.click_button(button_order)

        form_page1 = FillFormFirst(self)
        form_page1.fill_form_and_click_button()

        form_page2 = FillFormSecond(self)
        form_page2.fill_form_order()

        check_page = CheckSuccessOrder(self)
        check_page.complete_order_process()
