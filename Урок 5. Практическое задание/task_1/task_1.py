"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
with open("text_1.txt", 'w', encoding='utf-8') as f:
    while True:
        line = input('input new string or empty string to done:')
        if not line:
            break
        #f.write(f"{line}\n")
        print(line, file=f)
