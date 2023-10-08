from helpers import *

url = 'https://qa-scooter.praktikum-services.ru'
yandex_main = 'https://yandex.ru/'

answer_to_question0 = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
answer_to_question1 = 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'
answer_to_question2 = 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'
answer_to_question3 = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
answer_to_question4 = 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'
answer_to_question5 = 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'
answer_to_question6 = 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'
answer_to_question7 = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'

answer_to_questions = [
    answer_to_question0,
    answer_to_question1,
    answer_to_question2,
    answer_to_question3,
    answer_to_question4,
    answer_to_question5,
    answer_to_question6,
    answer_to_question7
]

name_form = generate_random_name()
lastname_form = generate_random_lastname()
stmetro_form  = 'Аэропорт'
address_form = generate_random_address()
number_form = generate_random_phone_number()


comment_form = 'test form'

success_text = 'Заказ оформлен'