import telebot
import math 
from telebot import types
from random import choice
import config
print("Бот работает") 

bot = telebot.TeleBot(config.TOKEN, skip_pending=True) # Токен бота

# Списки для вариативности ошибок 
l = ["А?","Чего?","Что?", "Не понял"] 
l2 = ["Напиши /start","/start","Просто напиши /start","Для начала напиши /start","/start чтобы начать"]
l3 = ["Понял","Окей","Хорошо","Без проблем","Могу"]
l4 = ["Перечитай что нужно сделать", "Похоже ты не понял,глянь выше",
"Попробуй еще раз", "Нее, ты не понял, перечитывай",
"Я же выделил что нужно сделать...", "Пробовал читать что написано выше?",
"Я так-то все расписал, но ты все равно не понял"]

	
# Кнопочки 
@bot.message_handler(commands=["start"])
def start(message):
	markup = types.InlineKeyboardMarkup(row_width=2) 
	itm1 = types.InlineKeyboardButton("Сумма(+)", callback_data="Sum") 
	itm2 = types.InlineKeyboardButton("Разность(-)", callback_data="Min") 
	itm3 = types.InlineKeyboardButton("Деление(/)", callback_data="Div") 
	itm4 = types.InlineKeyboardButton("Умножение(*)", callback_data="Mult") 
	itm5 = types.InlineKeyboardButton("Корень числа(√)", callback_data="Root")
	itm6 = types.InlineKeyboardButton("Факториал(!)", callback_data="Fact")
	itm7 = types.InlineKeyboardButton("Степень(^)", callback_data="Degr") 
	itm8 = types.InlineKeyboardButton("Число Пи(π)", callback_data="Pi")
	itm9 = types.InlineKeyboardButton("Дискриминант(D)",callback_data="Discr")
	itm10 = types.InlineKeyboardButton("Процент от числа(%)",callback_data="Perc")
	

	markup.add(itm1, itm2, itm3, itm4, itm5, itm6, itm7, itm8, itm9, itm10)

	bot.send_message(message.chat.id,
	"<b>Выбери операцию</b>", reply_markup=markup, parse_mode="html")


@bot.message_handler(content_types=["text"])
def wtf(message):
	bot.send_message(message.chat.id,f"{choice(l)}")
	bot.send_message(message.chat.id,f"{choice(l2)}")	

#Ответ бота на выбранную операцию   
@bot.callback_query_handler(func=lambda call:True)
def callback(call):
		if call.message:
			if call.data == "Fact":
				msg = bot.send_message(call.message.chat.id,f"{choice(l3)}, напиши число которое нужно возвести в <b>факториал</b>", parse_mode="html")
				bot.register_next_step_handler(msg,fact)

			elif call.data == "Root":
				msg = bot.send_message(call.message.chat.id,f"{choice(l3)}, напиши число из которого надо найти <b>квадоатный корень</b>", parse_mode="html")
				bot.register_next_step_handler(msg,root)

			elif call.data == "Degr":
				msg = bot.send_message(call.message.chat.id,f"{choice(l3)}, напиши <b>два</b> числа через <u>запятую</u> которые надо возвасти в степень,\nгде первое число - которое надо возводить \nа второе в какую степень",
																							 parse_mode="html")
				bot.register_next_step_handler(msg,degr)

			elif call.data == "Sum":
				msg = bot.send_message(call.message.chat.id,f"{choice(l3)}(+), напиши <b>два</b> числа через <u>запятую</u>", parse_mode="html")
				bot.register_next_step_handler(msg,sum1)

			elif call.data == "Min":
				msg = bot.send_message(call.message.chat.id,f"{choice(l3)}(-), напиши <b>два</b> числа через <u>запятую</u>", parse_mode="html")
				bot.register_next_step_handler(msg,min1)

			elif call.data == "Div":
				msg = bot.send_message(call.message.chat.id,f"{choice(l3)}(:), напиши <b>два</b> числа через <u>запятую</u>", parse_mode="html")
				bot.register_next_step_handler(msg,div)

			elif call.data == "Mult":
				msg = bot.send_message(call.message.chat.id,f"{choice(l3)}(x), напиши <b>два</b> числа через <u>запятую</u>", parse_mode="html")
				bot.register_next_step_handler(msg,mult)
			
			elif call.data == "Pi":
				msg = bot.send_message(call.message.chat.id,f"π = 3,1415926535 8979323846 2643383279 5028841971 6939937510 5820974944 5923078164 0628620899 8628034825 3421170679 8214808651 3282306647 0938446095 5058223172 5359408128 4811174502 8410270193 8521105559 6446229489 5493038196 4428810975 6659334461 2847564823 3786783165 2712019091 4564856692 3460348610 4543266482 1339360726 0249141273 7245870066 0631558817 4881520920 9628292540 9171536436 7892590360 0113305305 4882046652 1384146951 9415116094 3305727036 5759591953 0921861173 8193261179 3105118548 0744623799 6274956735 1885752724 8912279381 8301194912 9833673362 4406566430 8602139494 6395224737 1907021798 6094370277 0539217176 2931767523 8467481846 7669405132 0005681271 4526356082 7785771342 7577896091 7363717872 1468440901 2249534301 4654958537 1050792279 6892589235 4201995611 2129021960 8640344181 5981362977 4771309960 5187072113 4999999837 2978049951 0597317328 1609631859 5024459455 3469083026 4252230825 3344685035 2619311881 7101000313 7838752886 5875332083 8142061717 7669147303 5982534904 2875546873 1159562863 8823537875 9375195778 1857780532 1712268066 1300192787 6611195909 2164201989", parse_mode="html")
				
			elif call.data == "Discr":
				msg = bot.send_message(call.message.chat.id,f"{choice(l3)}, напиши <b>три</b> числа через <u>запятую</u>,\nгде по порядку перечислены a,b,c", parse_mode="html")
				bot.register_next_step_handler(msg,discr)
			
			elif call.data == "Perc":
				msg = bot.send_message(call.message.chat.id,f"{choice(l3)}, напиши <b>два</b> числа через <u>запятую</u>,\nгде первое это сколько процентов, а второе от какого числа",
																															 parse_mode="html")
				bot.register_next_step_handler(msg,perc)


# Фактариал
def fact(message):
	try:
		bot.send_message(message.chat.id,f"!{message.text} = {math.factorial(int(message.text))}")

	except:
		bot.send_message(message.chat.id,f"{choice(l)}")
		bot.send_message(message.chat.id,f"{choice(l4)}")

# Квадратный корень 
def root(message):
	try:
		bot.send_message(message.chat.id,f"√{message.text} = {math.sqrt(int(message.text))}")
	except:
		bot.send_message(message.chat.id,f"{choice(l)}")
		bot.send_message(message.chat.id,f"{choice(l4)}")

# Степень
def degr(message):
	try:
		a = message.text
		n = a.split(",")
		bot.send_message(message.chat.id,f"{n[0]}^{n[1]} = {float(n[0])** float(n[1])}")

	except:
		bot.send_message(message.chat.id,f"{choice(l)}")
		bot.send_message(message.chat.id,f"{choice(l4)}")
		

# Сумма
def sum1(message):
	try:
		a = message.text
		n = a.split(",")
		bot.send_message(message.chat.id,f"{n[0]} + {n[1]} = {float(n[0]) + float(n[1])}")

	except:
		bot.send_message(message.chat.id,f"{choice(l)}")
		bot.send_message(message.chat.id,f"{choice(l4)}")

# Разность 
def min1(message):
	try:
		a = message.text
		n = a.split(",")
		bot.send_message(message.chat.id,f"{n[0]} - {n[1]} = {float(n[0]) - float(n[1])}")

	except:
		bot.send_message(message.chat.id,f"{choice(l)}")
		bot.send_message(message.chat.id,f"{choice(l4)}")

# Деление
def div(message):
	try:
		a = message.text
		n = a.split(",")
		bot.send_message(message.chat.id,f"{n[0]} : {n[1]} = {float(n[0]) / float(n[1])}")

	except:
		bot.send_message(message.chat.id,f"{choice(l)}")
		bot.send_message(message.chat.id,f"{choice(l4)}")

# Умножение
def mult(message):
	try:
		a = message.text
		n = a.split(",")
		bot.send_message(message.chat.id,f"{n[0]} x {n[1]} = {float(n[0]) * float(n[1])}")

	except:
		bot.send_message(message.chat.id,f"{choice(l)}")
		bot.send_message(message.chat.id,f"{choice(l4)}")

# Дискриминант 
def discr(message):
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
		bot.send_message(message.chat.id,f"{choice(l)}")
		bot.send_message(message.chat.id,f"{choice(l4)}")
		
# Процент 
def perc(message):
	try:
		a = message.text
		n = a.split(",")
		bot.send_message(message.chat.id,f"{n[0]}% от {n[1]} = {float(n[1])/100 * float(n[0])}")

	except:
		bot.send_message(message.chat.id,f"{choice(l)}")
		bot.send_message(message.chat.id,f"{choice(l4)}")


bot.polling(none_stop=True)



