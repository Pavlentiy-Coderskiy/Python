 animals = ['Кот','Собака','Воробей','Тигр']
print(animals[0])
print(animals[1])
print(animals[2])
print(animals[3])

print('=================')

print(animals[-1])
print(animals[-2])
print(animals[-3])
print(animals[-4])


a = animals.count("Собака")
print(a)

animals.append("Панда") 
print(animals)

animals.insert("0,Альпака")
 
a = int(input("add number:"))
animals.pop(a)

animals.sort()
print(animals)


