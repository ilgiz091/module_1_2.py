name_course = 'Python,'
number_of_hours_spent = 1.5
the_number_of_completed_DZ = 12
average_execution_time = number_of_hours_spent / the_number_of_completed_DZ
print('Курс:', name_course, 'всего задач:', the_number_of_completed_DZ, 'затрачено часов:', number_of_hours_spent, 'среднее время выполнения:', average_execution_time, 'часа')

# пример с переменными a,b,c,d

a = 'Python,'
b = 1.5
c = 12
d = b / c
print('Курс:', a, 'всего задач:', c, 'затрачено часов:', b, 'среднее время выполнения:', d, 'часа')

# пример с запятыми

name_course = 'Python,'
number_of_hours_spent = 1.5
the_number_of_completed_DZ = 12
average_execution_time = number_of_hours_spent / the_number_of_completed_DZ
print('Курс:', name_course, 'всего задач:', (str(the_number_of_completed_DZ)) + ',', 'затрачено часов:', (str(number_of_hours_spent)) + ',', 'среднее время выполнения:', average_execution_time, 'часа')

# пример с переменными a,b,c,d и запятыми

a = 'Python,'
b = 1.5
c = 12
d = b / c
print('Курс:', a, 'всего задач:', (str(c)) + ',', 'затрачено часов:', (str(b)) + ',', 'среднее время выполнения:', d, 'часа')