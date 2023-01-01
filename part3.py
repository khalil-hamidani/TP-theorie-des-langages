from cgi import test
from tkinter import *
import tkinter as tk
import subprocess
from turtle import width
from unittest import result
from matplotlib import widgets
from matplotlib.pyplot import text
from numpy import pad
from pyparsing import Or

root =tk.Tk()

root.configure(background = '#c49e85')
root.geometry("700x500")
#! window name
root.title("Part 3")

def clear():
    word1_field.delete(0,END)
    word2_field.delete(1.0,END)    

def tester():
    input1=word1_field.get()
    word2_field.delete(1.0,END)
    # if (input1 !='a') or (input1 !='b'):
    #     temp = "Le mot doit appartenir aux terminaux                     T={a, b}"
    #     word2_field.insert(1.0, temp)
    if input1 == "":
        temp = "Le mot appartient au langage"
        word2_field.insert(1.0, temp)
    elif input1 == "*": 
        temp = "Le mot \"*\" \nn'appartient pas au langage"
        word2_field.insert(1.0, temp)
    else :
        test1=subprocess.run(f"java exo3 {input1}",capture_output=True,shell=True).stdout  
        test1.decode(encoding="UTF-8")
        word2_field.insert(1.0, test1)
    
def pp():
    subprocess.Popen(r"C:\Users\RGB\Desktop\coding\TpTHL\part0.exe")
    root.quit()
    root.destroy()
    
headlabel = Label(root, text = 'Partie 3 de TP THL : ',bg="#c49e85",font=50)
headlabel.grid(row = 0, column = 0 , pady=(0,10))

label1 = Label(root, text = "Donner un mot pour tester :", bg = '#c49e85',font=65)
label1.grid(row = 1, column = 0  , pady=10)

word1_field = Entry( width=20 ,bg="#ffd6af", font=('Arial', 20 ))
word1_field.grid(row = 3, column = 0, padx=25)

button1 = Button(root, text = "Tester", bg="#6b4b3e",fg="#ffd6af", font=50,command=tester)
button1.grid(row = 4, column = 0, pady=20)

button2 = Button(root, text = "Clear", bg="#6b4b3e",fg="#ffd6af", font=50, command=clear)
button2.grid(row = 6, column = 0, pady=10)

button3 = Button(root, text = "Programme principal", bg="#6b4b3e",fg="#ffd6af", font=50, command=pp)
button3.grid(row = 6, column = 3, pady=15 )

word2_field = Text( width=30 ,height=8,bg="#ffd6af" , font=('Arial', 15))
word2_field.grid(row = 5, column = 0, padx=0  )

word4_field = Text( width=30 ,height=18 ,bg="#ffd6af" , font=('Roboto', 15))
word4_field.grid(row = 0, column = 3, padx=1 ,pady=(9,0), rowspan=6)

textt="             Analyseur syntaxique                                                                    Soit la grammaire G tel que :                                                                      G=<T, N, S, P>     T={a, b}                                                                      N={S}          P={S→aaSb/Sa/ɛ}                                                               Ce programme vérifie si ce mot         appartient au langage L(G). On          supposera que ce mot est                 lexicalement correct.(il ne comporte   que des éléments de l’ensemble T)                                                                                                                                                                         Travaille de : Feddane Chaïma          Design de : khalil hamidani"
word4_field.insert(1.0,textt)
word4_field.config(state=DISABLED)
root.mainloop()