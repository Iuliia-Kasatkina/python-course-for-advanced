# 6.2 Основы работы с кортежами. Часть 1
"""

Вам доступен кортеж countries. Напишите программу, которая выводит индекс строки 'Slovenia' в кортеже countries.

Примечание. Считайте, что кортеж countries уже объявлен в вашей программе, и вы имеете к нему доступ.

Тестовые данные 🟢
Номер теста	                                       Входные данные	                                                                                                                        Выходные данные
1	             countries = ('Russia', 'Argentina', 'Spain', 'Slovakia', 'Canada', 'Slovenia', 'Italy')                                                     5

2	             countries = ('China', 'Slovenia', 'Cuba', 'Brazil')                                                                                         1

3                countries = ('Russia', 'Argentina', 'Spain', 'Slovakia', 'Canada', 'Spain', 'Cameroon', 'Slovenia', 'Italy', 'Spain', 'Ukraine', 'Chile')   7

"""

print(countries.index('Slovenia'))