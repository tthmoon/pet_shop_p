# Pet shop
Решение тестового задания в Яндекс.Финтех

Реализация: Python 3.8. Pytest. Requests.

Инструкция по запуску тестов: 
Из директории с тестами выполнить команду в терминале "python3 -m pytest tests/pet.py --alluredir \allure-results"
Инструкция по просмотру результатов: 

Из директории с тестами выполнить команду в терминале "allure serve allure-results". Необходима установка allure (https://docs.qameta.io/allure/#_commandline).

Важная информация:

Данная реализация поддерживает работу только json-объектами.

Ключевые слова oneOf, anyOf, allOf, not будут храниться в объектах как коллекции, проверки их значений должны будут быть в тестах.

Фреймворк писался с целью показать минимальную функциональность. Реализация архитектуры, способа запуска тестов опущены.

Тесты не имеют подробного описания, а также отсутствует пачка аннотация для allure. Пропустил этот момент, так как не определенных правил, как отчет должен выглядеть.

В base_model.py реализован механизм преобразования json в объект, при этом при наличии неизвестных полей, или если будет иметь не тот тип, то произойдет ошибка. Данная реализация ранняя, обработка полей с учётом специфики openapi не реализована.
