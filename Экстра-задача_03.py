# Дан файл с английскими именами. Начните с сортировки в алфавитном порядке. Затем подсчитайте алфавитные значения каждого имени и умножьте это значение
# на порядковый номер имени в отсортированном списке для получения количества очков имени.
# Например, если список отсортирован по алфавиту, имя COLIN (алфавитное значение которого 3 + 15 + 12 + 9 + 14 = 53) является 938-м в списке. 
# Поэтому, имя COLIN получает 938 × 53 = 49714 очков.
# Какова сумма очков имен в файле?


print('')
print('Исходный файл:')
print('')
path = 'english_names.txt'
data = open(path,'r')
for line in data:
    print(line)    
print(' ')
print('Отсортированный файл в алфавитном порядке:')
print('')
with open( 'english_names.txt', 'r' ) as file:
    sortFile = file.read().replace('"','').split(',') 
    sortFile.sort()
    print(sortFile)
print('')    

alphabet={'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,
     'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}

def get_scores(sortFile):
    summ=0
    c=1
    for i in sortFile:
        coin=0
        for j in i:
            coin+=alphabet[j]
        summ+=coin*c
        c+=1
    return summ
print('Сумма очков имён в файле:')
print(get_scores(sortFile))
print('')
