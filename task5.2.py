'''2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.'''

with open('my_file2.txt', encoding='utf-8') as my_file:
    lines = my_file.readlines()
    print('Количество строк в файле "my_file2.txt": ', len(lines))
    i = 1
    for line in lines:
        print(f'В {i} строке {len(line.split())} слов(а)')
        i+=1