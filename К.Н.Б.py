import random
print("------------------камень, ножницы, бумага------------------------")
print("-----------------------------------------------------------------")
print("Добро пожаловать в игру")
print("Игра состоит из трех раундов")
print("Побеждает тот кто наберет больше очков")
print("\t[k] - камень\n\t[n] - ножницы\n\t[b] - бумага")
 
player_score = 0
pc_score = 0
player_select = 0
pc_select = 0
print("---------------------------Игра началась------------------------")      
for i in range(3):
      print("\t----------РАУНД №"+ str(i+1) +"----------------")
      pc_select = random.choice("knb")
      while True:
          player_select = input("\tТвой выбор:")
          if (player_select == "k") or (player_select == "n") or (player_select == "b"):
              break
      else:
                print("\tОШИБКА")
      print("\tКомп выбрал:"+ pc_select)
      if player_select == pc_select:
          print("\tНичья")
      elif player_select =="k" and pc_select =="n":
          print("\tТы победил")
          player_score = player_score + 1
      elif player_select =="k" and pc_select =="b":
          print("\tКомп победил")
          pc_score = pc_score + 1
      elif player_select =="b" and pc_select =="k":
          print("\tТы победил")
          player_score = player_score + 1
      elif player_select =="b" and pc_select =="n":
          print("\tКомп победил")
          pc_score = pc_score + 1
      elif player_select =="n" and pc_select =="k":
          print("\tКомп победил")
          player_score = player_score + 1
      elif player_select =="n" and pc_select =="b":
          print("\tТы победил")
          pc_score = pc_score + 1
print("Результаты:")
if player_score > pc_score:
    print("Ты победил!")
if player_score < pc_score:
    print("Ты проиграл!")
if player_score == pc_score:
    print("Ничья!")    