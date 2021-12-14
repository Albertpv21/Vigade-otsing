from random import *
s=pos=neg=nol=[]
def arvud_loendis():
    print("Данные:")
    n=abs(int(input("Сколько целых чисел генерируем в список? => ")))
    mini=int(input("Введите минимальное число диапазона => "))
    maxi=int(input("Введите максимальное число диапазона => "))
    if mini>=maxi:
        mini,maxi=vahetus(mini,maxi)
    generaator(n,s,mini,maxi)
    print()
    print("Результаты:")
    print("Полученный список от",mini,"до",maxi,s)
    s.sort()
    print("Отсортированный список",s)
    jagamine(s,pos,neg,nol)
    print("Список положительных элементов",pos)
    print("Список отрицательных элементов",neg)
    print("Список нулевых элементов",nol)
    kesk=keskmine(pos)
    lisamine(s,kesk)
    print("Среднее положительных:",kesk)
    kesk=keskmine(neg)
    lisamine(s,kesk)
    print("Среднее отрицательных:",kesk)
    print("Добавляем средние в изначалный массив:")
    print(s)

def vahetus(a:int,b:int):
    """Kui min suurem kui max,siis vahetame neid omavahel
    :param int a:minimaalne arv,mis in suurem kui max
    :param int b:maximaalne arv,mis on väiksem kui min
    :rtype: int,int
    """
    abi=a
    a=b
    b=abi
    return a,b

def generaator(n:int,loend:list,a:int,b:int):
    """Genereerib juhusliku arvu
    :param list loend:список
    :param int n:количество чисел
    :param int a:минимальное число для генерации
    :param int b:максимально число для генерации
    :rtype: int
    """
    for i in range (n):
        loend.append(randint(a,b))
    

def jagamine(loend:list,p:list,n:list,nol:list):
    """Делит значения в список
    :param list p:список положительных чисел
    :param list loend:список чисел
    :param list n:список отрицательных чисел
    :param list nol:список нулевых чисел
    :rtype list
    """
    for el in loend:
        if el>0:
            p.append(el)
        elif el<0:
            n.append(el)
        else:
            nol.append(el)

def keskmine(loend):
    """находит среднее положительное число
    :param list loend:список чисел
    :rtype int n:число введеное пользователем
    """
    n=len(loend)
    if n==0:
        kesk=0
    else:
        sum=0
        for i in loend:
            sum+=i
        kesk=round(sum/n,2)
    return kesk

def lisamine(loend:list,el:float):
    """Добавляет список и структуру чисел
    :rtype loend:список чисел
    :rtype float el:
    :rtype float sort: сортирует
    """
    loend.append(el)
    loend.sort()

arvud_loendis()
    


