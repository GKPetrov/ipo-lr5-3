a=open("text.txt")#открытие файла
text=a.read()#считывание файла
word_count=text.count(" ")#Подсчет кол-ва слов
print(f"число слов {word_count+1}")#Вывод
a.close()#Закрытие
