'''1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.'''

# f = open('my_file.txt', 'w', encoding='utf-8')
# f.write(input('Ваша ФИО: '))
# f.close()

with open('my_file.txt', 'w', encoding='utf-8') as f:
    while True:
        text = input('Введите текст: ')
        f.write(text)
        if text == '':
            break