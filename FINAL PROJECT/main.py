from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox



root = Tk()
btn = Button


#Отображение окна 
root.title("Телефонная книга")
root.geometry("400x330+750+400")
root.resizable(False, False)
# root.iconbitmap("ICON.ico")
#Функция выхода 
def on_closing():
    if messagebox.askokcancel("Выход", "Вы действительно хотите выйти?"):
        root.destroy()
#Функция Помощи
def help():
	messagebox.showinfo("Помощь", "phuharev1@gmail.com - ПОЧТА ДЛЯ СВЯЗИ С НАМИ")

#Функция"О нас" 
def About_us():
	messagebox.showinfo("О нас", "РАЗРAБОТЧИК: Павел Хухарев")

#Функция первой кнопки
def bttn_cmd1():
	text = etry1.get()
	global name
	name = ("Имя: "+str(text)) 
	etry1.delete(0, END)
	print(name)
	


#Функция второй кнопки
def bttn_cmd2():
	text = etry1.get()
	global Sname
	Sname = ("Фамилия: "+str(text)) 
	etry1.delete(0, END)
	print(Sname)


#Функция третьей кнопки
def bttn_cmd3():
	text = etry1.get()
	global Dname
	Dname = ("Отчество: "+str(text)) 
	etry1.delete(0, END)
	print(Dname)
	

#Функция четвертой кнопки
def bttn_cmd4():
	text = etry1.get()
	global PH
	PH = ("Телефон: "+str(text)) 
	etry1.delete(0, END)
	print(PH)
	

#Функция пятой кнопки
def bttn_cmd5():
	text = etry1.get()
	global EmI
	EmI = ("Почта: "+str(text)) 
	etry1.delete(0, END)
	print(EmI)
	



#Функция первой кнопки + её удаление
def bttn1():
	bttn_cmd1()
	btn1.destroy()
	
#Функция второй кнопки + её удаление
def bttn2():
	bttn_cmd2()	
	btn2.destroy()

#Функция третьей кнопки + её удаление 
def bttn3():
	bttn_cmd3()	
	btn3.destroy()
	
#Функция четвертой кнопки + её удаление
def bttn4():
	bttn_cmd4()	
	btn4.destroy()
	
#Функция пятой кнопки + её удаление
def bttn5():
	bttn_cmd5()
	ph_list()
	print(PhList)
	btn5.destroy()
	



#Создание списка 	
def ph_list():
	global PhList
	PhList = []
	PhList.append(name)
	PhList.append(Sname)
	PhList.append(Dname)
	PhList.append(PH)
	PhList.append(EmI)






#Текст на верху
lbl1 = Label(text = "По очереди введите:", font=40, fg="#121212")
lbl2 = Label(text = "Имя, Фамилия,Отчество,", font=40, fg="#121212")
lbl3 = Label(text = "Телефон и Почту:", font=40, fg="#121212")
lbl1.pack()
lbl2.pack()
lbl3.pack()

#Строка ввода
etry1 = Entry(root, width=20, fg="white", bg="#4f4e4e")
etry1.pack()

#Отображение первой кнопки(Имя)
btn1 = Button(root, text="Добавить Имя", fg="#121212",command=bttn1,
			 bg="#D1D1D1",) 
btn1.pack()
#Отображение второй кнопки(Фамилия)
btn2 = Button(root, text="Добавить Фамилию", fg="#121212", command=bttn2,
			 bg="#D2D2D2",)
btn2.pack()
							
#Отображение третьей кнопки(Отчество)
btn3 = Button(root, text="Добавить Отчество", fg="#121212", command=bttn3,
			 bg="#D3D3D3",)
btn3.pack()

#Отображение четвертой кнопки(Телефон)
btn4 = Button(root, text="Добавить Телефон", fg="#121212", command=bttn4,
			 bg="#D4D4D4",)
btn4.pack()
#Отображение пятой кнопки()
btn5 = Button(root, text="Добавить Почту", fg="#121212",command=bttn5,
			 bg="#D4D5D5",)
btn5.pack()





#Верхнее меню
menu = Menu(root)
root.config(menu=menu)

help_menu = Menu(menu, tearoff=0)
help_menu.add_command(label='Помощь', command=help)
help_menu.add_command(label='О нас', command=About_us)


menu.add_cascade(label='Помощь', menu=help_menu)
menu.add_cascade(label='Выход',command=on_closing)

text = Text(root)
text.pack(expand=YES, fill=BOTH)




	





root.mainloop()