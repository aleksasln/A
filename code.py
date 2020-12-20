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

root = Tk()
root.title("GUI на Python")
root.geometry("400x350")

number = IntVar() #Чтобы переменная принимала различные целые значения

btn = Button(text='''Нажмите на кнопку,
                   \nчтобы определить Вашу очередность ''', background="#555", foreground="#ccc",
             padx="20", pady="8", font="Verdana 13", command=random_number) #Создаем кнопку
btn.pack()

label1 = Label(textvariable=number, fg="#eee", bg="#333") #Создаем окно, изменяющие значение после нажатия на кнопку

label1.place(relx=.5, rely=.5, anchor="c", height=30, width=130, bordermode=OUTSIDE)

root.mainloop()
