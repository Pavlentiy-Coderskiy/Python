# MD = {"Arab" : "Phone"}
# MD["Arab"] = "Nomure"
# print(MD["Arab"])
# MD["Key"] = "Val"
# print(MD)
# MD[input()] = input()
# print(MD)
MD2 = dict.fromkeys(("A","B","C"), 1)
MD3 = dict.fromkeys(("A","B","F"), 1)


MD2.update(MD3)


print(MD2)
print(MD2.values()) #Значения 
print(MD2.keys()) #Ключи
print(MD2.items()) #Все пары ключ - значение 

MD2.get("G")
print(MD.setdefault("G"))


MD2.pop("G")
print(MD2)
MD2.popitem("f")
MD4["A"]["key"] = "Val"




