#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from tkinter import *

class App:
    def __init__(self, master):

        #Valeur compteurs par défaut
        global counter_value
        counter_value = int() #faut il utiliser une variable globale? comment ?
        counter_value = 5234
        
        qty_cycles=96
        timer_ON=300
        timer_OFF=300
        timer_REST=300
        timer_CHARGE=300

        #Dimensions des cadres
        Wf=900
        Hf=600
        
        WC1=0.6*Wf
        HC1=Hf
        WC1a=WC1
        HC1a=0.2*HC1
        WC1b=WC1
        HC1b=0.8*HC1
        
        WC2=0.4*Wf
        HC2=Hf
        WC2a=WC2
        HC2a=0.75*HC2
        WC2b=WC2
        HC2b=0.25*HC2

        #Dessine les cadres
        frame = Frame(master, width=Wf, height=Hf)
        frame.pack()
        frame.pack_propagate(0)

        cadre1 =Frame(frame, width=WC1, height=HC1)
        cadre1.pack(side=LEFT)
        cadre1.pack_propagate(0)

        cadre1A =Frame(cadre1, bg="blue", width=WC1a, height=HC1a)
        cadre1A.pack(side=TOP)
        cadre1A.pack_propagate(0)

        cadre1B =Frame(cadre1, bg="brown", width=WC1b, height=HC1b)
        cadre1B.pack(side=TOP, fill=BOTH, expand=TRUE)
        cadre1B.pack_propagate(0)
        cadre1B.columnconfigure(0, weight=1)
        cadre1B.columnconfigure(1, weight=5)
        cadre1B.columnconfigure(2, weight=1)
        cadre1B.columnconfigure(3, weight=1)
        cadre1B.columnconfigure(4, weight=2)
        
        cadre2 =Frame(frame, width=WC2, height=HC2)
        cadre2.pack(side=LEFT)
        cadre2.pack_propagate(0)     

        cadre2A =Frame(cadre2, bg="red", width=WC2a, height=HC2a)
        cadre2A.pack(side=TOP)
        cadre2A.pack_propagate(0)

        cadre2B =Frame(cadre2, bg="green", width=WC2b, height=HC2b)
        cadre2B.pack(side=TOP)
        cadre2B.pack_propagate(0)

        #Position des objets
        fakeline1=Label(cadre1B, text="", bg="brown")
        fakeline1.grid(row=1, column=0)
        fakeline2=Label(cadre1B, text="", bg="brown")
        fakeline2.grid(row=2, column=0)
        fakeline3=Label(cadre1B, text="", bg="brown")
        fakeline3.grid(row=3, column=0)
        fakeline4=Label(cadre1B, text="", bg="brown")
        fakeline4.grid(row=4, column=0)
        fakeline5=Label(cadre1B, text="", bg="brown")
        fakeline5.grid(row=5, column=0)
        fakeline6=Label(cadre1B, text="", bg="brown")
        fakeline6.grid(row=6, column=0)
        fakeline7=Label(cadre1B, text="", bg="brown")
        fakeline7.grid(row=7, column=0)
        fakeline8=Label(cadre1B, text="", bg="brown")
        fakeline8.grid(row=8, column=0)


        
        label1=Label(cadre1B, text = "Counter initial value")
        label1.grid(row=1, column=1,padx=10, pady=5, sticky=W)
        label2=Label(cadre1B, text = "Quantity of ON/OFF cycles")
        label2.grid(row=3, column=1,padx=10, pady=5, sticky=W)
        label3=Label(cadre1B, text = "ON timer (sec)")
        label3.grid(row=4, column=1,padx=10, pady=5, sticky=W)
        label4=Label(cadre1B, text = "OFF timer (sec)")
        label4.grid(row=5, column=1,padx=10, pady=5, sticky=W)
        label5=Label(cadre1B, text = "Rest time (sec)")
        label5.grid(row=7, column=1,padx=10, pady=5, sticky=W)
        label6=Label(cadre1B, text = "Charging time (sec)")
        label6.grid(row=8, column=1,padx=10, pady=5, sticky=W)

        button1P= Button(cadre1B, text="+", command=self.button1P_action)
        button1P.grid (row=1, column =2,padx=10, pady=5)
        button1M= Button(cadre1B, text="-")
        button1M.grid (row=1, column =3,padx=10, pady=5)
        button2P= Button(cadre1B, text="+")
        button2P.grid (row=3, column =2,padx=10, pady=5)
        button2M= Button(cadre1B, text="-")
        button2M.grid (row=3, column =3,padx=10, pady=5)
        button3P= Button(cadre1B, text="+")
        button3P.grid (row=4, column =2,padx=10, pady=5)
        button3M= Button(cadre1B, text="-")
        button3M.grid (row=4, column =3,padx=10, pady=5)
        button4P= Button(cadre1B, text="+")
        button4P.grid (row=5, column =2,padx=10, pady=5)
        button4M= Button(cadre1B, text="-")
        button4M.grid (row=5, column =3,padx=10, pady=5)
        button5P= Button(cadre1B, text="+")
        button5P.grid (row=7, column =2,padx=10, pady=5)
        button5M= Button(cadre1B, text="-")
        button5M.grid (row=7, column =3,padx=10, pady=5)
        button6P= Button(cadre1B, text="+")
        button6P.grid (row=8, column =2,padx=10, pady=5)
        button6M= Button(cadre1B, text="-")
        button6M.grid (row=8, column =3,padx=10, pady=5)

        value1=Label(cadre1B, textvariable = str(counter_value))
        value1.grid(row=1, column=4,padx=10, pady=5, sticky=E)
        value2=Label(cadre1B, text = qty_cycles)
        value2.grid(row=3, column=4,padx=10, pady=5, sticky=E)
        value3=Label(cadre1B, text = timer_ON)
        value3.grid(row=4, column=4,padx=10, pady=5, sticky=E)
        value4=Label(cadre1B, text = timer_OFF)
        value4.grid(row=5, column=4,padx=10, pady=5, sticky=E)
        value5=Label(cadre1B, text = timer_REST)
        value5.grid(row=7, column=4,padx=10, pady=5, sticky=E)
        value6=Label(cadre1B, text = timer_CHARGE)
        value6.grid(row=8, column=4,padx=10, pady=5, sticky=E)
        
    def say_hi(self):
        print ("hi there, everyone!")


    def button1P_action (self):
        counter_value += 1
        value1.config(text=str(counter_value))
        value1.grid(row=1, column=4,padx=10, pady=5, sticky=E)

root = Tk()
app = App(root)
root.mainloop()

