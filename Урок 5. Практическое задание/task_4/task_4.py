"""
{"One":"Один", "Two":"Два", "Three": "Три", "Four": "Четыре"}
"text_44.txt","w", encoding= 'utf-8' as new_file:
open("text_4.txt", encoding= 'utf-8' as my_file:
new_file.writelines([line.replace(line.split()[0], rus_dic.get(line.split()[0])) for line in my_file])
