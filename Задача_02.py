# Создать и заполнить файл случайными целыми значениями. Выполнить сортировку содержимого файла по возрастанию. 

from random import randint

x = int(input('Из какого количества чисел должен состоять файл?: '))
data_file = open('Integer.txt', 'w')
for _ in range(x):
         data_file.write(str(randint(1,780)) + ' ') 
data_file.close() 
print('')
print('Содержимое созданого файла:')    
path = 'Integer.txt'
data = open(path,'r')
for line in data:
    print(line)   
data.close()  
print('')
print('Отсортированные значения по возростанию:') 
m = line.split()
newList = list(map(int,m)) 
newList.sort()
print(newList)
print('')
