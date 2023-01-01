from tkinter import *
import tkinter as tk
import subprocess
from turtle import width
from unittest import result
from matplotlib import widgets

def clear():
    word1_field.delete(0,END)
    word2_field.delete(0,END)
    word3_field.delete(1.0 , END)
    
def miroire():
        input1=word1_field.get() 
        word2_field.delete(0,END)
        word3_field.delete(1.0,END)
        miroire=subprocess.run(f"java Main1 {input1}",capture_output=True, shell=True).stdout
        miroire.decode(encoding="UTF-8")
        word3_field.insert(1.0, miroire)
    
def pow():
    input2=word1_field.get()
    input3=word2_field.get()
    word3_field.delete(1.0 , END)
    resultat=subprocess.run(f"java Main2 {input2} {input3}",capture_output=True, shell=True).stdout
    resultat.decode(encoding="UTF-8")
    word3_field.insert(1.0,resultat)
def pp():
    subprocess.Popen(r"C:\Users\RGB\Desktop\coding\TpTHL\part0.exe")
    root.quit()
    root.destroy()
root =tk.Tk()

root.configure(background = '#c49e85')
root.geometry("700x500")
#! window name
root.title("Part one")
#!--------------------------- part 1 --------------------
headlabel = Label(root, text = '    Partie 1 de TP THL : ', bg = "#c49e85",font=50)
label1 = Label(root, text = "Donner un mot :         ", bg = '#c49e85',font=50)
# label2 = Label(root, text = "le miroire :", bg = 'c49e85',font=50)
     
headlabel.grid(row = 0, column = 0 , columnspan=2)
label1.grid(row = 1, column = 0 , columnspan=1, pady=8)
# label2.grid(row = 3, column = 0, padx = 10)

word1_field = Entry( width=15 ,bg="#ffd6af" ,font=('Arial', 17 ))
word2_field = Entry(width= 15 , bg="#ffd6af" ,font=('Arial', 17 ))

word1_field.grid(row = 2, column = 0, padx = 10, pady = 0)
word2_field.grid(row = 4, column = 0, padx = 10, pady = 7)

button1 = Button(root, text = "Miroire",command=miroire ,bg="#6b4b3e",fg="#ffd6af",font=50)
button1.grid(row = 2, column = 1)

label4 = Label(root, text = "Donner la puissance :",bg="#c49e85",font=50)
label4.grid(row = 3, column = 0, padx = 10)

button3 = Button(root, text = "Puissance", command=pow ,bg="#6b4b3e",fg="#ffd6af",font=50)
button3.grid(row =4, column = 1 ,pady=7)

word3_field = Text( width=30 ,height=9 ,bg="#ffd6af" , font=('Arial', 15))
word3_field.grid(row = 6, column = 0, padx=7 ,pady=10, columnspan=2 )

button2 = Button(root, text = "Clear", bg="#6b4b3e",fg="#ffd6af",command=clear ,font=50)
button2.grid(row = 7, column = 0,pady=10,columnspan=2)

button3 = Button(root, text = "Programme principal", bg="#6b4b3e",fg="#ffd6af", font=50, command=pp)
button3.grid(row = 7, column = 3, pady=10 )

word4_field = Text( width=30 ,height=18 ,bg="#ffd6af" , font=('Arial', 15))
word4_field.grid(row = 0, column = 3, padx=7 ,pady=10, rowspan=7)


# text="         Langage et grammaires :                                                                  Soit un langage L(G) généré par la                                                            grammaire G=<T, N, S, P> tel que :                                                              T={a, b}         N={S, A, B, C}                                                                    P : S→AB        A→aA/bA/ab                                                                     B→bC            C→aC/bC/ɛ                                                                                                                       Travaille de : oudahi katia                                                                       Design de : khalil hamidani"
text="Manipulation/opérations sur les mots                                                        Soit l’alphabet T={a, b, c}.                                                                      Ce programme permet de :                                                                     1) Générer le mot miroir d’un mot     quelconque de T*. Ce mot sera        donné en entrée à votre programme.                                                        2) Générer la puissance n d’un mot   quelconque de T*. Le mot et la         valeur de n seront donnés en entréeà votre programme.                                                                                                                                          Travaille de : Ouadahi Katia            Gui de : Hamidani Khalil"
word4_field.insert(1.0,text)
word4_field.config(state=DISABLED)
#!--------------------------- part 1 --------------------

# label3 = Label(root, text = "Input word :",font=50)

# label5 = Label(root, text = "resultat :",font=50)

# label3.grid(row = 5, column = 0)

# label5.grid(row = 9, column = 0, padx = 10)

# word3_field = Entry( width=30 )
# word4_field = Entry(width= 30)
# word5_field = Entry(width= 30)

# word3_field.grid(row = 5, column = 1, padx = 10, pady = 10)
# word4_field.grid(row = 7, column = 1, padx = 10, pady = 10)
# word5_field.grid(row = 9, column = 1, padx = 10, pady = 10)











root.mainloop()