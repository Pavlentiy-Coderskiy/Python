c = int(input("Число которое надо перевести: "))
l = []
while c > 0:
	if c % 2 == True:
		c //= 2
		l.append(1)
	elif c % 2 == False:
		c //= 2
		l.append(0)

l.reverse()
print(*l)

