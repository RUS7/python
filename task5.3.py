'''3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить,
кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины
дохода сотрудников.'''


with open('my_file3.txt', encoding='utf-8') as salary:
    sal = []
    poor = []
    my_list = salary.read().split('\n')
    for i in my_list:
        i = i.split()
        poor.append(i[1])
        if float(i[1]) < 20000:
            poor.append(i[0])
        sal.append(i[1])
print(f'Сотрудники получающие зарплату меньше 20000: {poor}, средний оклад {sum(map(int, sal)) / len(sal)}')
