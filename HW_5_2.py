import re
'''Друге завдання'''

def generator_numbers(text: str):
    # вибрав всі числа за допомогою Regex (\d+ -вибрав перше входженні числа) (\.? - можливо буде крапка) (\d* - будь яка кількість чисел після крапки)
    # створив генератор і проітерував через цикл for 
    for number in re.findall(r'\d+\.?\d*', text):
        yield number


def sum_profit(text: str, func):
    # сума ЗП 
    total = 0
    # проітерував генератор і додав кожен елемент як тип флот до суми ЗП
    for i in func(text):
        total += float(i)
    return total






