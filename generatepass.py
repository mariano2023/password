from tkinter import *
import random
import string


def generatePass():
    lst=[]
    for i in range(1,13):
        alphabet_lower=list(string.ascii_lowercase)
        alphabet_upper=list(string.ascii_uppercase)
        alphabet_symbols=list(string.punctuation)
        str=alphabet_lower+alphabet_symbols+alphabet_upper
        character=random.choice(str)
        lst.append(character)
    a="".join(lst)
    print(a)
    label.config(text=a)
    #newlabel=Label(root, text="Hello").pack()

root = Tk() #ventana
root.title("Generador de Password")
root.geometry('500x500')
root.resizable(0,0)



my_button = Button(root, text='Generar', font='arial 15 bold', command=generatePass).pack()
my_label = Label(root, text='').pack() #pack significa visible
exit_button = Button(root, text='Salir', font='arial 15 bold', command=root.destroy).pack()
my_label = Label(root, text='').pack() #pack significa visible
label_et=Label(root, text="Este es el password : ")
label_et.pack()
label=Label(root,text="", font='arial 15 bold')
label.pack()


root.mainloop()



 