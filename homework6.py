
#Работа со словарями
my_dict = {'Alisa': 1990, 'Boris': 1985, 'Chariton': 1995}
print("Словарь my_dict:")
print(my_dict)

print("\nЗначение по существующему ключу:")
print(my_dict.get('Alisa'))

print("\nЗначение по отсутствующему ключу:")
print(my_dict.get('Denis'))

my_dict['Eva'] = 2000
my_dict['Fedor'] = 1978

print("\nДобавлены две произвольные пары:")
print(my_dict)

removed_value = my_dict.pop('Boris')
print("\nУдалена пара с ключом 'Boris', значение было:", removed_value)

print("\nСловарь my_dict после удаления:")
print(my_dict)

#Работа с множествами
my_set = {1, 'груша', 3.14, 'груша'}
print("\nМножество my_set:")
print(my_set)

my_set.add('апельсин')
my_set.add(5)

my_set.remove('груша')

print("\nИзмененное множество my_set:")
print(my_set)