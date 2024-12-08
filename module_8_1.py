from decimal import Decimal

def add_everything_up(a, b):
    try:
        # Попытка сложить a и b
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            # Если оба аргумента - числа, используем Decimal для точного сложения
            return float(Decimal(str(a)) + Decimal(str(b)))
        else:
            return a + b
    except TypeError:
        # Если возникла ошибка TypeError, возвращаем строковое представление a и b
        return f"{a}{b}"

# Примеры использования функции
print(add_everything_up(123.456, 'строка'))  # Вывод: 123.456строка
print(add_everything_up('яблоко', 4215))     # Вывод: яблоко4215
print(add_everything_up(123.456, 7))         # Вывод: 130.456
