'''5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает
 фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение.
  Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке). Далее запросите
  численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.'''

revenue = int(input('Введите выручку фирмы: '))
charge = int(input('Введите расходы фирмы: '))
if revenue > charge:
    print('Работа фирмы приносит прибыль')
    profitability = (revenue - charge) / revenue *100
    print(f'Рентабельность фирмы {profitability} %')
    staff = int(input('Какова численность сотрудников в фирме? '))
    print(f'Прибыль фирмы в расчете на одного сотрудника {(revenue - charge) / staff} %')
else:
    print('Фирма работает в убыток')