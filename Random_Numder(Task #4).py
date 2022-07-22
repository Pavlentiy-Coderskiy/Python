import random
a = int(input("ВЕДИТЕ КОЛИЧЕСТВО РАНДОМНЫХ ЦИФР:"))
l = [random.randint(0, 100) for i in range(a)]
print(l)


