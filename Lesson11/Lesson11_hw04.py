# 4.  Прочитать информацию из файла, в котором содержится тест дзен python(предварительно сформировать файл,
#     вручную скопировав текст дзен из интерпретатора). Упорядочить все слова из этого файла в порядке возрастания 
#     длины слова. То есть результирующий список слов будет иметь примерно такой вид: ['a', 'a', 'of', 'by', 'is', 'is', 'is' … 
#     'implementation', 'implementation’]. 
#     Подсказка, необходимо при вызове метода sort или функции sorted указывать аргумент key.
#     https://docs.python.org/3/library/functions.html#sorted, 
#     https://docs.python.org/3/library/stdtypes.html#list.sort

zen_l = []
with open ('zen.txt', 'r') as zen_f:
    #  Формироавние списка одной сторокой, но не так очевидно
    # i = [zen_l.extend(line.lower().strip().strip('.').strip('!').split(' ')) for line in zen_f] 
    for line in zen_f:
        zen_l.extend(line.lower().strip().strip('.').strip('!').split(' '))
zen_l.sort()
sorted_list = sorted(zen_l, key=len)
print(sorted_list)
