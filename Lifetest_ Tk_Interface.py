#!/usr/bin/env python
# -*- coding: utf-8 -*-

# bibliothèques
try:
    import RPi.GPIO as GPIO
except ImportError:
    print('LOADING MOCK GPIO')
    import mock_gpio as GPIO

import argparse
import json
import pathlib
import sys
import time
from tkinter import*


#Valeur états de l'appli par défaut

DEFAULT_APP_STATE = {
    'cycles': 0,
    'date': None,
    'pas_incr': 1,
    'counter_val': 1,
    'qty_cycles': 96,
    'timer_ON': 300,
    'timer_OFF': 300,
    'timer_REST': 300,
    'timer_CHARGE': 300
}
      

#Déposer et charger les états de l'appli

def dump_app_state(file_path, **kwargs):
    state = load_app_state(file_path)
    state.update(kwargs)
    state['date'] = date_sec_epoch()

    with open(file_path, 'w') as fd:
        json_str = json.dumps(state)
        fd.write(json_str)


def load_app_state(file_path):
    path = pathlib.Path(file_path)
    if not path.exists():
        return DEFAULT_APP_STATE

    with path.open('r') as fd:
        json_str = fd.read()
        d = json.loads(json_str)
        return d



#Valeur interface Tkinter par défaut




#Déposer et charger les valeurs interface Tkinter 





#Prévoir une classe pour l'interface Tkinter
    #Sur appui départ cycle => lancer déroulement du programme

class Interface(object):



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

        value1=Label(cadre1B, textvariable = str(counter_val))
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
        counter_val += 1
        value1.config(text=str(counter_val))
        value1.grid(row=1, column=4,padx=10, pady=5, sticky=E)

    def get_counter_val(self):
        return load_app_state(self.app_state_file)['counter_val']

    def set_counter_val(self, pas_incr):
        dump_app_state(self.app_state_file, counter_val=counter_val)

    def get_qty_cycles(self):
        return load_app_state(self.app_state_file)['qty_cycles']

    def set_qty_cycles(self, pas_incr):
        dump_app_state(self.app_state_file, qty_cycles=qty_cycles)

    def get_timer_ON(self):
        return load_app_state(self.app_state_file)['timer_ON']

    def set_timer_ON(self, pas_incr):
        dump_app_state(self.app_state_file, timer_ON=timer_ON)
        
    def get_timer_OFF(self):
        return load_app_state(self.app_state_file)['timer_OFF']

    def set_timer_OFF(self, pas_incr):
        dump_app_state(self.app_state_file, timer_OFF=timer_OFF)
        
    def get_timer_REST(self):
        return load_app_state(self.app_state_file)['timer_REST']

    def set_timer_REST(self, pas_incr):
        dump_app_state(self.app_state_file, timer_REST=timer_REST)
        
    def get_timer_CHARGE(self):
        return load_app_state(self.app_state_file)['timer_CHARGE']

    def set_timer_CHARGE(self, pas_incr):
        dump_app_state(self.app_state_file, timer_CHARGE=timer_CHARGE)


#Prévoir une classe pour le déroulement du programme    
class App(object):
    def __init__(self, log_file, app_state_file):
        self.log_file = log_file
        self.app_state_file = app_state_file

    def get_cycles(self):
        return load_app_state(self.app_state_file)['cycles']

    def set_cycles(self, cycle):
        dump_app_state(self.app_state_file, cycles=cycle)

    def get_pas_incr(self):
        return load_app_state(self.app_state_file)['pas_incr']

    def set_pas_incr(self, pas_incr):
        dump_app_state(self.app_state_file, pas_incr=pas_incr)

    def log_to_csv(self, cycles):
        log_to_csv(self.log_file, cycles)


def date_sec_epoch():
    #return time.strftime('%d/%m/%y %H:%M:%S', time.localtime())
    return time.time()

def log_time():
    return time.strftime('%d/%m/%y %H:%M:%S', time.localtime(date_sec_epoch()))

def arduino_idle():
    GPIO.output(25,GPIO.LOW)

def pause_board(msg, delay=15):
    print(msg, time.strftime('%d/%m/%y %H:%M:%S', time.localtime(date_sec_epoch())))
    arduino_idle()
    time.sleep(delay)

def log_to_csv(file_path, cycles):
    with open(file_path, "a") as fd:
        fd.write(str(date_sec_epoch()))
        fd.write(", ")
        fd.write(log_time())
        fd.write(", ")
        fd.write(str(cycles))
        fd.write("\n")

def init_cycles(app):
    cycles_string = app.get_cycles()
    print ('La derniere valeur enregistree du compteur est {}'.format(cycles_string))
    choix = input('Souhaitez vous modifier la valeur ? Y/N \n')

    if choix.lower() in ['y', 'yes']:
        cycles_string = input('\nSaisir la nouvelle valeur pour le compteur \n')
        print ('\nLa nouvelle valeur du compteur est {} \n'.format(cycles_string))
        app.set_cycles(int(cycles_string))        # dump de l'etat courant

    elif choix.lower() in ['n', 'no']:
        print ('\nLa valeur enregistree du compteur est {} \n'.format(cycles_string))
        cycle = int(cycles_string)

    else:
        print ("Le choix n'est pas repertorie, le prog s'arrete ici ! \n \n")
        sys.exit(0)


def init_pas_incr(app):
    pas_incr = app.get_pas_incr()
    print ('chaque fin de boucle ajoute {} cycles de 5min ON'.format(pas_incr))
    choix = input('Souhaitez vous modifier la valeur ? Y/N \n')

    if choix.lower() in ['y', 'yes']:
        pas_incr = input('\nSaisir la nouvelle valeur de pas \n')
        print ('\nchaque fin de boucle ajoute {} cycles de 5min ON \n'.format(pas_incr))
        app.set_pas_incr(int(pas_incr))        # dump de l'etat courant

    elif choix.lower() in ['n', 'no']:
        print ('\nchaque fin de boucle ajoute dorénavant {} cycles de 5min ON \n'.format(pas_incr))
        pas_incr = int(pas_incr)

    else:
        print ("Le choix n'est pas repertorie, le prog s'arrete ici ! \n \n")
        sys.exit(0)

def main(args):

    root = Tk()
    app = App(root)
    root.mainloop()

    app = App(
        log_file=args.log_file,
        app_state_file=args.app_state_file
    )
    # configurations
    GPIO.setmode(GPIO.BCM)                      # mode de numérotation des pins
    GPIO.setwarnings(False)                     # supprime les messages d'erreurs

    # declaration des I/O
    GPIO.setup(25,GPIO.OUT, initial=GPIO.LOW)           # la pin 25 réglee en sortie, valeur basse par défaut => départ cycle ARDUINO
    GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # la pin 4 réglée en entrée => bouton bascule programme actif sur raspberry
    GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)   # la pin 19 réglée en entrée => signal haut envoyé par arduino en fin de programme arduino

    # variables perso
    init_cycles(app)
    init_pas_incr(app)
    
    # Verifie les conditions pour lancer le prog arduino
    while True:

        fin_arduino = GPIO.input(19)
        bouton_bascule = GPIO.input(4)

        current_day = time.strftime('%A',time.localtime(date_sec_epoch()))
        current_hour = int(time.strftime('%H',time.localtime(date_sec_epoch())))

        # tant que l'arduino n'a pas termine son programme continue ce qui suit
        if fin_arduino == 0:
            print ("cycles ON/OFF terminé", log_time())
            
            # verifie que le bouton bascule raspberry est active
            if bouton_bascule == 0:
                print ("selecteur en position ON", log_time())
            
                # condition if, si jour = jour de semaine samedi ou dimanche alors demarrer, sinon attendre 15 minutes
                if current_day.lower() in ["monday", "tuesday", "wednesday", "thursday", "friday"]:
                    print ("programme dans les jours fixes", log_time())
                
                    # condition if, si heure >8H et <17H alors demarrer, sinon attendre 15 minutes
                    if current_hour >= 8 and  current_hour <= 17:
                        print ("programme dans les heures fixes", log_time())

                        #depart cycle
                        GPIO.output(25,GPIO.HIGH)       # depart cycle pour l'arduino

                        #affichage dans le shell
                        print ("depart programme le ", log_time(), "\n")

                        old_cycle = cycle
                        cycle += pas_incr
                        print('Le compteur passe de {} à {}'.format(old_cycle, cycle))

                        app.set_cycles(cycle)        # dump de l'etat courant
                        app.log_to_csv(cycle)

                        time.sleep(50)              # on ne change rien pendant X minutes, initalement 1 minute (tps supérieur au déroulement du prog arduino)

                    else:
                        pause_board("programme en dehors des heures fixes")

                else:
                    pause_board("programme en dehors des jours fixes")

            else:
                pause_board("selecteur en position OFF")

        else:
            pause_board("cycles ON/OFF déja en cours")


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--log-file',
                        default='Log_Lifetest.csv',
                        help="Path to the log file (CSV)")
    parser.add_argument('-a', '--app-state-file',
                        default='app_state.json',
                        help="Path to the app state file (JSON)")
    return parser.parse_args()


if __name__ == '__main__':
    main(get_args())

     
