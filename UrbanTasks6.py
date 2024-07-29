my_dict = {"Исмоил": 2001,
           "Баха": 2000,
           "Насим": 1994}
print(f'Словарь: {my_dict}')

print(f'Существующее значение: {my_dict.get("Исмоил")}')
print(f'Несуществующее значение: {my_dict.get("Акбар")}')

my_dict.update({"Фарзин": 2003,
                "Иско": 2004})
a = my_dict.pop("Насим")

print(f'Удалённое значение: {a}')
print(f'Изменённый словарь: {my_dict}')

my_set = {1, 2, 2.5, 8, 5, 'hello', True, 2, 1, 2.5 }
print(f'set: {my_set}')
my_set.add(9)
my_set.add(11)
my_set.remove('hello')
print(f'Изменённый set: {my_set}')