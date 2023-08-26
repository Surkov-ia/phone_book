import os
import os.path
import re


InformsFileVar1 = os.path.join("C:\GeekBrains\Pithon_REPASITORY\Seminar\Sem08","Informs1.txt")
InformsFileVar2 = os.path.join("C:\GeekBrains\Pithon_REPASITORY\Seminar\Sem08","Informs2.txt")

"""Функция для выбора функций(меню)"""
def Navigation():
    while True:
        menu = input("Введите действие → ").lower()
        if menu == "1": return VarChek(var=0)
        if menu == "2": return VarChek1(var1=0)
        if menu == "3": return VarChek2(var2=0)
        if menu == "4": return VarChek3(var3=0)
        if menu == "5": return VarChek4(var4=0) 
        if menu == "6": exit()

"""Функция для проверки длины вводных данных"""
def ChekSize(arr):
    if len(arr) > 4:
        arr = arr[:4]
    if len(arr) < 4:
        a = len(arr)
        while a < 4:
            arr.append("-")
            a += 1
    return arr

"""Функция для выбора варианта заполнения"""
def VarChek(var):
    print("1 - заполняет данными в строку \n"
          "2 - заполняет данными в столбец")
    var = int(input("Введите номер варианта → "))
    while var != 1 and var !=2:
        print("Ты дурак?! Даю тебе последний шанс")
        var = int(input("Введите номер варианта → "))
    if var == 1:
        RecordVar1(ChekSize(input("Введите фамилию, имя, отчество, номер телефона, человека через пробел → ").split()))
    else:
        RecordVar2(ChekSize(input("Введите фамилию, имя, отчество, номер телефона, человека через пробел → ").split()))
        
"""Функция открытия и записи в файл информации (если файл уже есть то мы добавляем в него данные)"""      
def RecordVar1(arr):
    dict = {0: "Фамилия:", 1: " Имя:", 2: " Отчество:", 3: " Номер:"}
    count = 0
    if os.path.exists(InformsFileVar1):
        with open(InformsFileVar1,"a",encoding = "utf-8") as file:
            for i in arr:
                file.writelines(dict[count] + " " + i + "|")
                count += 1
            file.write("\n")
            return print(f"Данные пользователя были успешно добавлены!")         
    else:
        with open(InformsFileVar1,"w+",encoding = "utf-8") as file:
            file.write("\n")
            for i in arr:
                file.writelines(dict[count] + " " + i + "|")
                count += 1
            file.write("\n")
            return print(f"Данные пользователя были успешно добавлены!")

def RecordVar2(arr):
    dict = {0:"Фамилия:", 1: "Имя:", 2: "Отчество:", 3: "Номер:"}
    count = 0
    if os.path.exists(InformsFileVar2):
        with open(InformsFileVar2,"a",encoding = "utf-8") as file:
            for i in arr:
                file.writelines(dict[count] + " " + i + "\n")
                count += 1
            # file.write("\n")
            return print(f"Данные пользователя были успешно добавлены!")         
    else:
        with open(InformsFileVar2,"w+",encoding = "utf-8") as file:
            for i in arr:
                file.writelines(dict[count] + " " + i + "\n")
                # file.write("\n")
                count += 1
            file.write("\n")
            return print(f"Данные пользователя были успешно добавлены!")

"""Функция для выбора варианта поиска"""
def VarChek1(var1):
    print("Выберите вариант документа для поиска данных \n"
          "Вариант 1 заполнен строкой  \n"
          "Вариант 2 заполнен столбцом ")
    var1 = int(input("Введите номер варианта → "))
    while var1 != 1 and var1 !=2:
        print("Ты дурак?! Даю тебе последний шанс")
        var1 = int(input("Введите номер варианта → "))
    if var1 == 1:
        SearchV1(input("Введите Фамилию человека для поиска → "))
    else:
        SearchV2(input("Введите Фамилию человека для поиска → "))

"""Функция поиска Данных пользователя и их печати"""
def SearchV1(teg):
    if os.path.exists(InformsFileVar1):
        resList =[]
        with open(InformsFileVar1,"r",encoding = "utf-8") as file:
            new_array = [(line.split()) for line in file.readlines()]
            for i in range(0,len(new_array)):
                if teg in new_array[i]:
                     print(f"По ващему запросу {teg} удалось найти:   ") 
                     return print(*new_array[i])
            return print(f"По вашему запросу {teg} ничего не найдено")
    else: print("Файла не существует!")

def SearchV2(teg):
    if os.path.exists(InformsFileVar2):
        with open(InformsFileVar2,"r",encoding = "utf-8") as file:
            new_array = [re.sub("\s+","",line) for line in file.readlines()]
            for i in range(0,len(new_array)):
                if teg in new_array[i]:
                    return print(f"По ващему запросу {teg} удалось найти: \n {new_array[i]} \n {new_array[i+1]} \n {new_array[i+2]} \n {new_array[i+3]}")
            return print(f"По вашему запросу {teg} ничего не найдено")
    else: print("Файла не существует!")

"""Функция для выбора варианта чтения"""
def VarChek2(var2):
    print("1 - Открывает фаил заполненый данными в строку \n"
          "2 - Открывает фаил заполненый данными в столбец")
    var2 = int(input("Введите номер варианта → "))
    while var2 != 1 and var2 !=2:
        print("Ты дурак?! Даю тебе последний шанс")
        var2 = int(input("Введите номер варианта → "))
    if var2 == 1:
        ReadV1()
    else:
        ReadV2()
     
"""Функция чтения фаилов"""
def ReadV1():
    with open(InformsFileVar1,'r',encoding = 'utf-8') as file:
        for line in file:
            print(line)

def ReadV2():
    with open(InformsFileVar2,'r',encoding = 'utf-8') as file:
        for line in file:
            print(line)

"""Функция для выбора варианта поиска"""
def VarChek3(var3):
    print("Выберите вариант документа для изменения данных \n"
          "Вариант 1 заполнен строкой  \n"
          "Вариант 2 заполнен столбцом ")
    var3 = int(input("Введите номер варианта → "))
    while var3 != 1 and var3 !=2:
        print("Ты дурак?! Даю тебе последний шанс")
        var3 = int(input("Введите номер варианта → "))
    if var3 == 1:
        ChangeV1()
    else:
        ChangeV2()

"""Функция изменения данных в файле"""
def ChangeV1():
    teg, diction, new_teg = input("Введите Фамилию человека для замены его данных → "), input('Введите что вы хотите изменить (1 - Фамилия, 2 - Имя, 3 - Отчество, 4 - Номер) → ') , input('Введите новые данные → ')
    check = False
    new_array = []
    dict = {"1": "Фамилия:", "2": "Имя:", "3": "Отчество:", "4": "Номер:"}
    if diction not in dict.keys():
        return print(f"Ваше значение {diction} не подходит условию!")
    with open(InformsFileVar1,"r",encoding = "utf-8") as file:
        new_array =  [line for line in file.readlines()]
        for i in range(len(new_array)):
            if teg in new_array[i]:
                new = new_array[i].split("|")
                check = True
                if diction == "1": 
                    new[0] = dict[diction] + " " + new_teg + "|"
                    new_array[i] = new[0]+" "+new[1]+"|"+" "+new[2]+"|"+" "+new[3]+"|"+"\n"
                if diction == "2": 
                    new[1] = dict[diction] + " " + new_teg + "|"
                    new_array[i] = new[0]+"|"+" "+new[1]+" "+new[2]+"|"+" "+new[3]+"|"+"\n"
                if diction == "3": 
                    new[2] = dict[diction] + " " + new_teg + "|"
                    new_array[i] = new[0]+"|"+" "+new[1]+"|"+" "+new[2]+" "+new[3]+"|"+"\n"
                if diction == "4": 
                    new[3] = dict[diction] + " " + new_teg + "|"
                    new_array[i] = new[0]+"|"+" "+new[1]+"|"+" "+new[2]+"|"+" "+new[3]+"\n"
    if check == True:               
        with open(InformsFileVar1,"w",encoding = "utf-8") as file:
            file.writelines(new_array)
            return print(f"Данные пользователя {teg} были успешно изменены!")
    else: return print(f"По вашему запросу {teg} ничего не найдено!")     

def ChangeV2():
    teg, diction, new_teg = input("Введите Фамилию человека для замены его данных → "), input('Введите что вы хотите изменить (1 - Фамилия, 2 - Имя, 3 - Отчество, 4 - Номер) → ') , input('Введите новые данные → ')
    check = False
    dict = {"1": "Фамилия:", "2": "Имя:", "3": "Отчество:", "4": "Номер:"}
    if diction not in dict.keys():
        return print(f"Ваше значение {diction} не подходит условию!")
    with open(InformsFileVar2,"r",encoding = "utf-8") as file:
        new_array = [line for line in file.readlines()]
        for i in range(len(new_array)):
            if teg in new_array[i]:
                check = True
                if diction == "1": new_array[i] = dict[diction] + " " + new_teg + "\n"
                if diction == "2": new_array[i+1] = dict[diction] + " "  + new_teg + "\n"
                if diction == "3": new_array[i+2] = dict[diction] + " "  + new_teg + "\n"
                if diction == "4": new_array[i+3] = dict[diction] + " "  + new_teg + "\n"    
    if check == True:               
        with open(InformsFileVar2,"w",encoding = "utf-8") as file:
            file.writelines(new_array)
            return print(f"Данные пользователя {teg} были успешно изменены!")
    else: return print(f"По вашему запросу {teg} ничего не найдено!")   

"""Функция для выбора варианта удаления"""
def VarChek4(var4):
    print("Выберите вариант документа для изменения данных \n"
          "Вариант 1 заполнен строкой  \n"
          "Вариант 2 заполнен столбцом ")
    var3 = int(input("Введите номер варианта → "))
    while var3 != 1 and var3 !=2:
        print("Ты дурак?! Даю тебе последний шанс")
        var3 = int(input("Введите номер варианта → "))
    if var3 == 1:
        Delete1()
    else:
        Delete2()

"""Функция удаления данных пользователя из файла"""
def Delete1():
    teg = input("Введите Фамилию человека для удаления его данных → ")
    check = False
    with open(InformsFileVar1,"r",encoding = "utf-8") as file:
       new_array = [line for line in file.readlines()]
       for i in range(len(new_array)):
           if teg in new_array[i]:
               check = True
               new_array[i] = ''
    if check == True:
        with open(InformsFileVar1,"w",encoding = "utf-8") as file:
            file.writelines(new_array)
            return print(f"Данные пользователя {teg} были успешно удалены")
    return print(f"По вашему запросу {teg} ничего не найдено")     

def Delete2():
    teg = input("Введите Фамилию человека для удаления его данных → ")
    check = False
    with open(InformsFileVar2,"r",encoding = "utf-8") as file:
       new_array = [line for line in file.readlines()]
       for i in range(len(new_array)):
           if teg in new_array[i]:
               check = True
               new_array[i], new_array[i+1], new_array[i+2], new_array[i+3] = '', '', '', ''
    if check == True:
        with open(InformsFileVar2,"w",encoding = "utf-8") as file:
            file.writelines(new_array)
            return print(f"Данные пользователя {teg} были успешно удалены")
    return print(f"По вашему запросу {teg} ничего не найдено")     