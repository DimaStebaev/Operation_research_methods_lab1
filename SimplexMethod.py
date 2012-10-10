#!/usr/bin/python
# -*- coding: utf-8 -*- 

import sys

#sys.argv+=['example3.txt']

basis = []

def swap(Table, row, cel):    
    if len(Table)==0:
        raise Exception("Пустая симплекс-таблица")
    rc = Table[row][cel]
    for j in range(len(Table[0])):
        Table[row][j]/=rc*1.0
    for i in range(len(Table)):
        rc = Table[i][cel]
        for j in range(len(Table[0])):
            if i!=row:
                Table[i][j]-=Table[row][j]*rc
    basis[row] = cel

if __name__ == '__main__':
    if len(sys.argv)<=1:
        print """
Вас приветствует программа, которая решает основную задачу линейного программирования симплекс-методом. Чтобы воспользоватья ей, запустите этот с крипт с единственный параметром: именем файла с условием.

Формат файла с условием следующий:

Все строчки, которые начинаются с #, игнорируются.
Все пустые строчки игнорируются.

Первая строка должна содержать целевую функцию в формате:
[целевая функция] = [ { + | - }] [a] xi [ { + | - } [a] xi , [ ... ]] [ { + | - }b] -> {min | max}
где 
i - неповторяющееся целое неотрицательное число, обозначающее номер переменной
(переменные начинают нумероваться с нуля),
a - целое неотрицательное число, обозначающее коэффицент перед переменной.
b - целое неотрицательное число, обозначающее свободный член.

Оставшиеся строки должны содержать ограничения в формате:
[ { + | - }] [a] xi [ { + | - } [a] xi , [ ... ]] { <= | >= } b
где 
i - неповторяющееся целое неотрицательное число, обозначающее номер переменной
(переменные начинают нумероваться с нуля, и не должно быть переменных, которые не участвуют в целефой функции),
a - целое неотрицательное число, обозначающее коэффицент перед переменной.
b - целое неотрицательное число, обозначающее свободный член.
     
"""
    else:
        filename = sys.argv[1]
        try:        
            f = open(filename, 'r')           
        except IOError:
            print "Ошибка при открытии файла " + filename
        else:
            first = True
            A = []
            b = []
            less = []
            while True:
                line = f.readline()
                if line=='':
                    break
                line = line.replace(' ', '')
                line = line.replace('\t', '')
                line = line.replace('\r', '')
                line = line.replace('\n', '')
                if len(line)<1 or line[0]=='#':
                    continue
                
                if first:
                    #разбор строки с целефой функцией
                    first = False
                    minimize = line.find('->min')!=-1;
                    line = line[:line.find('->')];                    
                    func = line[line.find('=')+1:]
                    sign = func[0]!='-'
                    if func[0]=='+' or func[0]=='-':
                        func = func[1:]
                    if func[0]=='x':
                        value = 1
                    else:
                        value = int(func[:func.find('x')])
                    func = func[func.find('x')+1:]
                    
                    i = func.find('+')
                    if i == -1:
                        i=func.find('-')
                    elif func.find('-')>=0:
                        i = min(i, func.find('-'))
                    if i>0:
                        index = int(func[:i])
                        func = func[i:]                    
                    else:
                        index = int(func)
                    
                    a = [0]*(index+1)
                    a[index] = value;
                    if not sign:
                        a[index]*=-1
                        
                    while func.find('x')!=-1:                    
                        value = func[:func.find('x')]
                        if value == '+':
                            value = 1
                        elif value == '-':
                            value = -1
                        else:
                            value = int(value)
                        func = func[func.find('x')+1:]
                        i = func.find('+')
                        if i == -1:
                            i=func.find('-')
                        elif func.find('-')>=0:
                            i = min(i, func.find('-'))
                        if i>0:
                            index = int(func[:i])
                            func = func[i:]
                        else:
                            index = int(func)
                            func = ""
                        if index >=len(a):
                            a += [0]*(index+1 - len(a))
                        a[index] = value                             
                    if len(func)>0:
                        ab = int(func)
                    else:
                        ab = 0
                    
                    a_origin = a[:]
                    if minimize:
                        a = [-x for x in a]
                                      
                else:
                    #разбор строки с условием
                    A.append([0]*len(a))
                    if line.find('<=')!=-1:                        
                        b.append(int(line[line.find('<=')+2:]))
                        less.append(True)
                        func = line[:line.find('<=')]
                    else:
                        b.append(int(line[line.find('>=')+2:]))
                        less.append(False)
                        func = line[:line.find('>=')]
                        
                    sign = func[0]!='-'
                    if func[0]=='+' or func[0]=='-':
                        func = func[1:]
                    if func[0]=='x':
                        value = 1
                    else:
                        value = int(func[:func.find('x')])
                    func = func[func.find('x')+1:]
                    
                    i = func.find('+')
                    if i == -1:
                        i=func.find('-')
                    elif func.find('-')>=0:
                        i = min(i, func.find('-'))
                    if i>0:
                        index = int(func[:i])
                        func = func[i:]                    
                    else:
                        index = int(func)
                    A[len(A)-1][index] = value;
                    if not sign:
                        A[len(A)-1][index]*=-1
                        
                    while func.find('x')!=-1:                    
                        value = func[:func.find('x')]
                        if value == '+':
                            value = 1
                        elif value == '-':
                            value = -1
                        else:
                            value = int(value)
                        func = func[func.find('x')+1:]
                        i = func.find('+')
                        if i == -1:
                            i=func.find('-')
                        elif func.find('-')>=0:
                            i = min(i, func.find('-'))
                        if i>0:
                            index = int(func[:i])
                            func = func[i:]
                        else:
                            index = int(func)                        
                        A[len(A)-1][index] = value
                        
            #a - коэффиценты целефой функции
            #ab - свободный член целефой функции
            #A - матрица коэффицентов ограницений
            #b - свободные члены условий            
            #print a
            #print A
            #print b                     
            
            #составим симплекс-таблицу
            Table = [0]*(len(b)+1)
            for i in range(len(Table)):
                Table[i] = [0]*(len(a)+len(b)+1)
            for i in range(len(b)):
                for j in range(len(a)):
                    Table[i][j] = A[i][j]
                Table[i][len(Table[i])-1] = b[i]
                if less[i]:
                    Table[i][len(a)+i] = 1;
                else:  
                    Table[i][len(a)+i] = -1;
            for j in range(len(a)):
                Table[len(b)][j] = -a[j]
            Table[len(b)][len(Table[len(b)])-1] = ab            
            basis = range(len(a), len(a)+len(b))    
            
            #swap(Table, 0, 0)            
            #for i in Table:
            #    print i
            
            #Поиск опорного плана
            ready = False
            while not ready:
                ready = True
                for i in range(len(b)):
                    if Table[i][len(Table[i])-1] < 0:
                        ready = False
                        exist = False                        
                        for j in range(len(Table[i])-1):
                            if Table[i][j]>0:
                                exist = True
                                c = j
                                break
                        if not exist:
                            raise Exception('Система несовместна')
                        r = 0;
                        for I in range(len(b)):
                            if Table[I][len(Table[i])-1]/Table[I][c] < 0 and Table[I][len(Table[i])-1]/Table[I][c] > Table[r][len(Table[i])-1]/Table[r][c]:
                                r = I;
                        break
                if not ready:
                    swap(Table, r, c)
                    
            #Опорный план найден. Находим оптимальное решение
            
            ready = False
            while not ready:
                #Проверяем оптимальность
                ready = True;
                for j in range(len(a)):
                    if Table[len(b)][j]<0:
                        ready = False
                        break
                if ready:
                    break
                
                #Вычисляем, какую переменную будем вводить
                c = 0;
                for j in range(len(Table[0])-1):
                    if Table[len(b)][j]<Table[len(b)][c]:
                        c = j
                        
                #Вычисляем, какую переменную будем выводить
                for i in range(len(b)):
                    if Table[i][c]!=0:
                        r = i
                        break
                for i in range(len(b)):
                    if Table[i][c]!=0 and Table[i][len(Table[i])-1]/Table[i][c]>0 and Table[i][len(Table[i])-1]/Table[i][c] <  Table[r][len(Table[r])-1]/Table[r][c]:
                        r = i
                        
                #Вводим
                swap(Table, r, c)
                #print '---------------------------------'
                #for i in Table:
                #    print i                           
            
            answer = [0]*(len(a)+len(b))
            for i in range(len(basis)):
                answer[basis[i]] = Table[i][len(a)+len(b)]
            print 'Ответ: ', answer[:len(a)]
            extremum = 0
            for i in range(len(a_origin)):
                extremum += a_origin[i]*answer[i]              
            print 'Значение целефой функции: ', extremum
            #for i in Table:
            #    print i    
                             
            f.close()          
