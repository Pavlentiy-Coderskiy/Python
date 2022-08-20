import speech_recognition as sp 


mic  = sp.Microphone(device_index= 1)


list_microphone = mic.list_microphone_names()


for i in list_microphone:
	print(i)






