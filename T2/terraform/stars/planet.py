from threading import Thread
import threading #TODO remover
from time import sleep #TODO remover
import random #TODO remover

import globals

class Planet(Thread):

    ################################################
    # O CONSTRUTOR DA CLASSE NÃO PODE SER ALTERADO #
    ################################################
    def __init__(self, terraform,name):
        Thread.__init__(self)
        self.terraform = terraform
        self.name = name

    def nuke_detected(self, damagePercentage):
        if (self.terraform > 0):
            before_percentage = self.terraform
            while(before_percentage == self.terraform):
                self.terraform -= damagePercentage # fazer o planeta receber dano após bombardeado
            print(f"[NUKE DETECTION] - The planet {self.name} was bombed. {self.terraform}% UNHABITABLE\n")

        #Se o planeta já tiver sido atingido e o contador ainda não tiver sido zerado, o planeta explode.
        if (self.timer > 0):
            print(f"KABUM! O corpo celeste {threading.currentThread()} foi destruído pois muitas bombas o atingiram simultaneamente.\n")
            self.alive = False
        else:
            self.timer = 25

    def print_planet_info(self):
        print(f"🪐 - [{self.name}] → {self.terraform}% UNINHABITABLE")

    def run(self):
        globals.acquire_print()
        self.print_planet_info()
        globals.release_print()

        print(f"--------{threading.currentThread()}--------\n")

        while(globals.get_release_system() == False):
            pass

        #TODO fazer o nuke_detected ser chamado pela propria bomba

        self.timer = 0
        self.alive = True

        while (self.alive):
            print(f"-------- Loop {threading.currentThread()}--------\n")

            #Fazer o contador diminuir durante a execução da thread do planeta
            if (self.timer > 0):
                self.timer -= 1
            
            #TODO retirar isso aqui depois
            if (random.randint(0, 30) == 5):
                self.nuke_detected(5)

        #while(True):
        #    self.nuke_detected(5)