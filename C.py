Number = int(input("Число которое надо перевести: "))
binar_list = []
while Number > 0:
	if Number % 2:
		Number //= 2
		binar_list.append(1)
	else:
		Number //= 2
		binar_list.append(0)

binar_list.reverse()
print(*binar_list)

