# Дан список чисел. Создать список, в который попадают числа, описываемые возрастающую последовательность. 
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д. Порядок элементов менять нельзя

list = [3, 1, 2, 3, 4, 6, 1, 7, 9, 5, 99]

def sorting(list):
    newList = [list[0]]
    for i in list:
        if i > max(newList):
            newList.append(i)
    return newList

print('Изначальный список \n',list)    
print('Обработанный список \n',sorting(list))
