import telebot
import math 
from telebot import types
from random import choice
import config
print("Бот работает") 

bot = telebot.TeleBot(config.TOKEN, skip_pending=True) # Токен бота

# Списки для вариативности ошибок 
list1 = ["А?","Чего?","Что?", "Не понял"] 
list2 = ["Напиши /start","/start","Просто напиши /start","Для начала напиши /start","/start чтобы начать"]
list3 = ["Понял","Окей","Хорошо","Без проблем","Могу"]
list4 = ["Перечитай что нужно сделать", "Похоже ты не понял,глянь выше",
"Попробуй еще раз", "Нее, ты не понял, перечитывай",
"Я же выделил что нужно сделать...", "Пробовал читать что написано выше?",
"Я так-то все расписал, но ты все равно не понял"]

	
# Кнопочки 
@bot.message_handler(commands=["start"])
def start(message):
	markup = types.InlineKeyboardMarkup(row_width=2) 
	item_sum = types.InlineKeyboardButton("Сумма(+)", callback_data="Sum") 
	item_minus = types.InlineKeyboardButton("Разность(-)", callback_data="Minus") 
	item_division = types.InlineKeyboardButton("Деление(/)", callback_data="Divisoin") 
	item_multiplication = types.InlineKeyboardButton("Умножение(*)", callback_data="Multiplication") 
	item_root = types.InlineKeyboardButton("Корень числа(√)", callback_data="Root")
	item_factorial = types.InlineKeyboardButton("Факториал(!)", callback_data="Factorial")
	item_degree = types.InlineKeyboardButton("Степень(^)", callback_data="Degree") 
	item_pi = types.InlineKeyboardButton("Число Пи(π)", callback_data="Pi")
	item_discriminant = types.InlineKeyboardButton("Дискриминант(D)",callback_data="Discriminant")
	item_percent = types.InlineKeyboardButton("Процент от числа(%)",callback_data="Percent")
	

	markup.add(item_sum, item_minus, item_division, item_multiplication, item_root,
				item_factorial, item_degree, item_pi, item_discriminant, item_percent)

	bot.send_message(message.chat.id,
	"<b>Выбери операцию</b>", reply_markup=markup, parse_mode="html")


@bot.message_handler(content_types=["text"])
def wtf(message):
	bot.send_message(message.chat.id,f"{choice(list1)}")
	bot.send_message(message.chat.id,f"{choice(list2)}")	

#Ответ бота на выбранную операцию   
@bot.callback_query_handler(func=lambda call:True)
def callback(call):
		if call.message:
			if call.data == "Factorial":
				msg = bot.send_message(call.message.chat.id,f"{choice(list3)}, напиши число которое нужно возвести в <b>факториал</b>", parse_mode="html")
				bot.register_next_step_handler(msg,factarial)

			elif call.data == "Root":
				msg = bot.send_message(call.message.chat.id,f"{choice(list3)}, напиши число из которого надо найти <b>квадоатный корень</b>", parse_mode="html")
				bot.register_next_step_handler(msg,root)

			elif call.data == "Degree":
				msg = bot.send_message(call.message.chat.id,f"{choice(list3)}, напиши <b>два</b> числа через <u>запятую</u> которые надо возвасти в степень,\nгде первое число - которое надо возводить \nа второе в какую степень",
																							 parse_mode="html")
				bot.register_next_step_handler(msg,degree)

			elif call.data == "Sum":
				msg = bot.send_message(call.message.chat.id,f"{choice(list3)}(+), напиши <b>два</b> числа через <u>запятую</u>", parse_mode="html")
				bot.register_next_step_handler(msg,sum_function)

			elif call.data == "Minus":
				msg = bot.send_message(call.message.chat.id,f"{choice(list3)}(-), напиши <b>два</b> числа через <u>запятую</u>", parse_mode="html")
				bot.register_next_step_handler(msg,min_function)

			elif call.data == "Divisoin":
				msg = bot.send_message(call.message.chat.id,f"{choice(list3)}(:), напиши <b>два</b> числа через <u>запятую</u>", parse_mode="html")
				bot.register_next_step_handler(msg,division)

			elif call.data == "Multiplication":
				msg = bot.send_message(call.message.chat.id,f"{choice(list3)}(x), напиши <b>два</b> числа через <u>запятую</u>", parse_mode="html")
				bot.register_next_step_handler(msg,multiplication)
			
			elif call.data == "Pi":
				msg = bot.send_message(call.message.chat.id,f"π = 3,1415926535 8979323846 2643383279 5028841971 6939937510 5820974944 5923078164 0628620899 8628034825 3421170679 8214808651 3282306647 0938446095 5058223172 5359408128 4811174502 8410270193 8521105559 6446229489 5493038196 4428810975 6659334461 2847564823 3786783165 2712019091 4564856692 3460348610 4543266482 1339360726 0249141273 7245870066 0631558817 4881520920 9628292540 9171536436 7892590360 0113305305 4882046652 1384146951 9415116094 3305727036 5759591953 0921861173 8193261179 3105118548 0744623799 6274956735 1885752724 8912279381 8301194912 9833673362 4406566430 8602139494 6395224737 1907021798 6094370277 0539217176 2931767523 8467481846 7669405132 0005681271 4526356082 7785771342 7577896091 7363717872 1468440901 2249534301 4654958537 1050792279 6892589235 4201995611 2129021960 8640344181 5981362977 4771309960 5187072113 4999999837 2978049951 0597317328 1609631859 5024459455 3469083026 4252230825 3344685035 2619311881 7101000313 7838752886 5875332083 8142061717 7669147303 5982534904 2875546873 1159562863 8823537875 9375195778 1857780532 1712268066 1300192787 6611195909 2164201989", parse_mode="html")
				
			elif call.data == "Discriminant":
				msg = bot.send_message(call.message.chat.id,f"{choice(list3)}, напиши <b>три</b> числа через <u>запятую</u>,\nгде по порядку перечислены a,b,c", parse_mode="html")
				bot.register_next_step_handler(msg,discrimanant)
			
			elif call.data == "Percent":
				msg = bot.send_message(call.message.chat.id,f"{choice(list3)}, напиши <b>два</b> числа через <u>запятую</u>,\nгде первое это сколько процентов, а второе от какого числа",
																															 parse_mode="html")
				bot.register_next_step_handler(msg,percent)


# Фактариал
def factarial(message):
	try:
		bot.send_message(message.chat.id,f"!{message.text} = {math.factorial(int(message.text))}")

	except:
		bot.send_message(message.chat.id,f"{choice(list1)}")
		bot.send_message(message.chat.id,f"{choice(list4)}")

# Квадратный корень 
def root(message):
	try:
		bot.send_message(message.chat.id,f"√{message.text} = {math.sqrt(int(message.text))}")
	except:
		bot.send_message(message.chat.id,f"{choice(list1)}")
		bot.send_message(message.chat.id,f"{choice(list4)}")

# Степень
def degree(message):
	try:
		a = message.text
		n = a.split(",")
		bot.send_message(message.chat.id,f"{n[0]}^{n[1]} = {float(n[0])** float(n[1])}")

	except:
		bot.send_message(message.chat.id,f"{choice(list1)}")
		bot.send_message(message.chat.id,f"{choice(list4)}")
		

# Сумма
def sum_function(message):
	try:
		a = message.text
		n = a.split(",")
		bot.send_message(message.chat.id,f"{n[0]} + {n[1]} = {float(n[0]) + float(n[1])}")

	except:
		bot.send_message(message.chat.id,f"{choice(list1)}")
		bot.send_message(message.chat.id,f"{choice(list4)}")

# Разность 
def min_function(message):
	try:
		a = message.text
		n = a.split(",")
		bot.send_message(message.chat.id,f"{n[0]} - {n[1]} = {float(n[0]) - float(n[1])}")

	except:
		bot.send_message(message.chat.id,f"{choice(list1)}")
		bot.send_message(message.chat.id,f"{choice(list4)}")

# Деление
def division(message):
	try:
		a = message.text
		n = a.split(",")
		bot.send_message(message.chat.id,f"{n[0]} : {n[1]} = {float(n[0]) / float(n[1])}")

	except:
		bot.send_message(message.chat.id,f"{choice(list1)}")
		bot.send_message(message.chat.id,f"{choice(list4)}")

# Умножение
def multiplication(message):
	try:
		a = message.text
		n = a.split(",")
		bot.send_message(message.chat.id,f"{n[0]} x {n[1]} = {float(n[0]) * float(n[1])}")

	except:
		bot.send_message(message.chat.id,f"{choice(list1)}")
		bot.send_message(message.chat.id,f"{choice(list4)}")

# Дискриминант 
def discrimanant(message):
	try:
		mt = message.text 
		num = mt.split(",")

		di = float(num[1])**2 - 4 * float(num[0]) * float(num[2]) 
		bot.send_message(message.chat.id, f"D = {di}")
			
		if di > 0:
			x1 = (-float(num[1]) + di**0.5) / (2 * float(num[0]))
			x2 = (-float(num[1]) - di**0.5) / (2 * float(num[0]))
			bot.send_message(message.chat.id, f"x1 ={x1}")
			bot.send_message(message.chat.id, f"x2 ={x2}")


		elif di == 0:
			x1 = -float(num[1]) / (2 * float(num[0]))
			bot.send_message(message.chat.id, f"Тут всего один корень, X ={x1}")

		else: 
			bot.send_message(message.chat.id,"Иксы не найти, довольствуйся дискриминантом")

	except:
		bot.send_message(message.chat.id,f"{choice(list1)}")
		bot.send_message(message.chat.id,f"{choice(list4)}")
		
# Процент 
def percent(message):
	try:
		a = message.text
		n = a.split(",")
		bot.send_message(message.chat.id,f"{n[0]}% от {n[1]} = {float(n[1])/100 * float(n[0])}")

	except:
		bot.send_message(message.chat.id,f"{choice(list1)}")
		bot.send_message(message.chat.id,f"{choice(list4)}")


bot.polling(none_stop=True)



