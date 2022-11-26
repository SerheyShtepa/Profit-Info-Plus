"""
1.Необходимо реализовать функцию, которая на входе принимает список массивов и номер варианта.
На выходе получаем массив, состоящий из значений порядкового номера этого варианта.

Пояснение:
Допустим, мы хотим реальзовать генерацию трехзначного числа в десятичной системе вариантов.
На входе функции подаем:
[
  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
]

Номер варианта 1: На выходе получим [0,0,0]
Номер варианта 138: На выходе получим [1,3,7]
Номер варианта 1012: : На выходе получим [0,1,1] (один полный круг + 12-й вариант на втором круге)

Система счисления может быть любой, например такой:
[
  [false, true],
  0,
  ['first', 'second', 'third']
]
Если вариант = 4, то на выходе должно быть [true, 0, 'first']"""


def sorting_by_options(array_list: list, variant_number: list) -> list:
    # Для избежанние недоразумений, предлагаю передавать каждый вариант отдельным элементом списка,
    # поскольку 1012 это 10 и 12, или 10, 1 и 2.

    result = []

    try:
        if type(array_list) != list or type(variant_number) != list:
            raise TypeError(print("На входе должны быть масивы"))
        elif [num for num in variant_number if type(num) != int]:
            raise TypeError(print("Варианты должны быть только целочисленные"))
        elif [num for num in variant_number if num < 1]:
            raise TypeError(print("Варианты может быть только положительным числом больше '0'"))
        elif len(array_list) < len(variant_number):
            raise ValueError(print("Количество вариантов больше количества масивов"))

    except(ValueError, TypeError):
        print("Некорректный ввод, измените данные на входе.")

    option = 0
    for i in array_list:
        selected_option = i[variant_number[option] % len(i) - 1]
        result.append(selected_option)
        option += 1
        option = option % len(variant_number)

    # return result
    print(result)


array_list = [
  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
]

variant_number = [1, 10, 12]

sorting_by_options(array_list, variant_number)
