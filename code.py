from tkinter import *
import random
N = int(input("Сколько маленьких бочек должно быть в мешке: "))
spam = list(range(1, N+1)) #Создаем список
def random_number(): #Функция для выдачи рандомных номеров бочек
    if  len(spam)>1 :
        number.set(random.choice(spam))
        a=random.choice(spam)
        spam.remove(a)
    else:
        number.set(spam)
