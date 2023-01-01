import os
from tkinter import *
import tkinter as tk
import subprocess

def runp1():
    subprocess.Popen(r"C:\Users\RGB\Desktop\coding\TpTHL\part1.exe")
    root.quit()
    root.destroy()

def runp2():
    subprocess.Popen(r"C:\Users\RGB\Desktop\coding\TpTHL\part2.exe")
    root.quit()
    root.destroy()
    
def runp3():
    subprocess.Popen(r"C:\Users\RGB\Desktop\coding\TpTHL\part3.exe")
    root.quit()
    root.destroy()

root = tk.Tk()
root.configure(background = '#c49e85')
root.geometry("704x500")
root.title("Tp THL")
headlabel = Text( width=62 ,height=16.5 ,bg="#ffd6af" , font=('Roboto', 15))
headlabel.grid(row = 0, column = 0, padx=8 ,pady=(8,1),columnspan=3)
headlabel.config(highlightbackground="#ffd6af")
tp="Département  Informatique                                               Année 2021/2022 L2 Info                                                                                                                                                       TP : THL                                                                                                                                                                       Objectif :Les grammaires sont des outils formels qui permettent de réaliser     l’analyse syntaxique. Ce programme est un analyseur syntaxique qui utilise un environnement de programmation des langages \"java\" et \"Python\" pour la       realisation des trois partie de ce TP :                                                                                                                                                                             Partie 1 : Manipulation et opérations sur les mots                                         Partie 2 : Langage et grammaires                                                               Partie 3 : Analyseur syntaxique                                                                                                                                                                                     Ce TP est realiser par 4 membres :                                                                                                                                                                                 Hamidani khalil       Feddane Chaima       Ouadahi Katia       Labtani daouia"
headlabel.insert(1.0,tp)
headlabel.config(state=DISABLED)
btn1 = Button(root, text = "Partie 1", bg="#6b4b3e",fg="#c49e85", font=50,command=runp1)
btn1.grid(row = 1, column = 0, pady=30)
btn2 = Button(root, text = "Partie 2", bg="#6b4b3e",fg="#c49e85", font=50,command=runp2)
btn2.grid(row = 1, column = 1, pady=30)
btn3 = Button(root, text = "Partie 3", bg="#6b4b3e",fg="#c49e85", font=50,command=runp3)
btn3.grid(row = 1, column = 2, pady=30)
root.mainloop()
