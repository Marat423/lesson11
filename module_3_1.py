calls = 0 # Создаем переменную
def count_calls(): # Создаем функцию
    global calls # Делаем имя нашей переменной глобальной
    calls += 1 # При вызове + 1

def string_info(string): # Создаем функцию для строк
    count_calls() # Обращаемся к глобальной функции
    return (len(string), string.upper(), string.lower()) # Возвращаем длину строки, в верзнем регистре и в нижнем

def is_contains(string, list_to_searh): # Создаем функицию  для сравнения строки со списком
    count_calls() # Обращение к глобальной функции
    s = string.lower() # строка в нижнем регистре
    for i in list_to_searh: # цикл по списку
        if s == i.lower(): # Если строка в нижнем регистре равен слову из списка в нижнем регистре
            return True 

    return False



print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)