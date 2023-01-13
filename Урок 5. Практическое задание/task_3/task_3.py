"""
4)	Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
with open('text_3.txt','r',encoding= 'utf-8') as f:
    employees_dict= {line.split()[0]: float(line.split()[1]) for line in f}
    print(f'Average salary = {round(sum(employees_dict.values())/ len(employees-dict),3)}\n'
          f'Employees with salary less than 20k {[e[0] for e in employess_dict.items() if e[1] < 20000]}')
