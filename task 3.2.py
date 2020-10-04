# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия,
# год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

# def info_user(name, surname, year_of_birth, city_of_residence, email, telephone):
#    print(name, surname, year_of_birth, city_of_residence, email, telephone)


# name = input('Введите имя: ')
# surname = input('Введите фамилию: ')
# year_of_birth = input('Введите год рождения: ')
# city_of_residence = input('Введите город проживания: ')
# email = input('Введите email: ')
# telephone = input('Введите номер телефона: ')

# info_user(name, surname, year_of_birth, city_of_residence, email, telephone)

def info_user(name, **kwargs):
    print(name, kwargs)
info_user('Rustam', surname = 'Safin', year_of_birth = 1987, city_of_residence = 'Khimki',
          email = 'kadastr056@yandex.ru', telephone = '8999999999')
