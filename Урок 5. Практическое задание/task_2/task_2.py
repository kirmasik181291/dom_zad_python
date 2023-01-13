"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
with open("text_4.txt", "r", encoding= 'utf-8') as f_obj:
    useful = [f'{count}. {line.strip()} - {len(line.split())} слов'
              for count, line in enumerate(f_obj, 1)]
    print(*useful, f"всего строк - {len(useful)}.", sep="\n")
