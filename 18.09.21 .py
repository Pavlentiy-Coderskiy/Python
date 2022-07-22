

n = input("Введите пример: ")

if n.find("+") != -1:
	sing = int(n.find("+"))
	first = int(n[:sing])
	second = int(n[sing+1:])
	n = str(first + second)
elif n.find("-") != -1:
	sing = int(n.find("-"))
	first = int(n[:sing])
	second = int(n[sing+1:])
	n = str(first - second)
elif n.find("/") != -1:
	sing = int(n.find("/"))
	first = int(n[:sing])
	second = int(n[sing+1:])
	n = str(first / second)
elif n.find("*") != -1:
	sing = int(n.find("*"))
	first = int(n[:sing])
	second = int(n[sing+1:])
	n = str(first * second)


print(n)





