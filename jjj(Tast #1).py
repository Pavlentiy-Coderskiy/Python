a = int(input("Введите 1 число: "))
b = int(input("Введите 2 число: "))
c = []
d =[]
e = []
for i in range(a, b):
   c.append(i)
for i in c:
   if i % 7 == 0:
       d.append(i)
   if i % 5 == 0:
       e.append(i)
print(c)
c.reverse()
print(c)
print(d)
print(e)