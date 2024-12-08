def personal_sum(numbers):
    result = 0
    incorrect_data = 0

    try:
        for number in numbers:
            if isinstance(number, (int, float)):
                result += number
            else:
                print(f'Некорректный тип данных для подсчёта суммы - {number}')
                incorrect_data += 1
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None

    return result, incorrect_data


def calculate_average(numbers):
    result = personal_sum(numbers)

    if result is None:
        return None

    total, incorrect_data = result

    try:
        average = total / (len(numbers) - incorrect_data)
    except ZeroDivisionError:
        return 0

    return average


# Примеры вызова функции
print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')
