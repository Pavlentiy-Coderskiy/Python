import random
print("===================Камень, Ножницы, Бумага======================")
print("=================================================================")
print("Добро пожаловать в игру :D")
print("Игра состоит из трех раундов")
print("Побеждает тот кто наберет больше очков")
print("\t[k] -Камень\n\t[n] - Ножницы\n\t[b] - Бумага")

pl_select = ""
pc_select = ""
pl_score = 0
pc_score = 0
print("====================Игра началась==================") 
for i in range(3):
    print("============================Raund=====================", i+1)
    pc_select = random.choice("кнб")

    while True:
        pl_select = input("Введите вариант(к/н/б): ")
        if (pl_select in "кбн")  and (len(pl_select)==1):
            break
        else:
            print("Введено не верно")
    print("Комп выкинул",pc_select)
    if pc_select == pl_select:
        print("Ничья")
    elif pc_select== "к"and pl_select =="н":
        print("Выйграл комп")
        pc_select = pc_select +1
    elif pc_select== "н"and pl_select =="б":
        print("Выйграл комп")
        pc_select = pc_select + 1
    elif pc_select== "б"and pl_select =="к":
        print("Выйграл комп")
        pc_select = pc_select + 1
    elif pc_select== "н"and pl_select =="к":
        print("Ты Выйграл")
        pl_select = pl_select + 1   
    elif pc_select== "к"and pl_select =="б":
        print("Ты Выйграл")
        pl_select = pl_select + 1  
    elif pc_select== "б"and pl_select =="н":
        print("Ты Выйграл")
        pl_select = pl_select += 1  
print("Результаты:")
if player_score > pc_score:
    print("Ты победил!")
if player_score < pc_score:
    print("Ты проиграл!")
if player_score == pc_score:
    print("Ничья!")    

