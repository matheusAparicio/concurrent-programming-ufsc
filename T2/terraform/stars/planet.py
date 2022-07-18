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

    def nuke_detected(self, damagePercentage, pole="north"):
        globals.acquirePlanetBombed()
        if (self.terraform > 0):
            before_percentage = self.terraform
            while(before_percentage == self.terraform):
                self.terraform -= damagePercentage # Fazer o planeta receber dano após bombardeado.
            print(f"[NUKE DETECTION] - The planet {self.name} was bombed. {self.terraform}% UNHABITABLE\n")

        #Quando o planeta é atingido, é feita a verificação se ele foi atingido recentemente e em quais polos para saber se o planeta explodirá ou não.
        if (self.timerNorth > 0 and self.timerSouth > 0):
            print(f"KABUM! O corpo celeste {threading.currentThread()} foi destruído pois muitas bombas o atingiram simultaneamente.\n")
            self.alive = False
        elif (self.timerNorth > 0 and pole == "north"):
            print(f"KABUM! O corpo celeste {threading.currentThread()} foi destruído pois 2 bombas atingiram o polo norte simultaneamente.\n")
            self.alive = False
        elif (self.timerSouth > 0 and pole == "south"):
            print(f"KABUM! O corpo celeste {threading.currentThread()} foi destruído pois 2 bombas atingiram o polo sul simultaneamente.\n")
            self.alive = False
        else:
            match pole:
                case "north":
                    self.timerNorth = 25
                case "south":
                    self.timerSouth = 25
                case _:
                    print(f"Erro! Polo atingido do corpo celeste {threading.currentThread()} não foi identificado.")
        globals.releasePlanetBombed()

        # Teste.
        if self.terraform <= 0:
            print(f"{self.name} terraformado com sucesso!")
            self.alive = False
            '''
            if (globals.getUnhabitablePlanets() > 0):
                globals.setUnhabitablePlanets(globals.getUnhabitablePlanets() - 1)
            else:
                print("Todos os planetas foram terraformados! Programa sendo finalizado...")
                a = input("Aperte enter para finalizar o programa. ")
                os._exit(1)
            '''
        # globals.notifyHabitable()

    def print_planet_info(self):
        print(f"🪐 - [{self.name}] → {self.terraform}% UNINHABITABLE")

    def run(self):
        globals.acquire_print()
        self.print_planet_info()
        globals.release_print()

        print(f"--------{threading.currentThread()}--------\n")

        while(globals.get_release_system() == False):
            pass

        self.timerNorth = 0
        self.timerSouth = 0
        self.alive = True

        while (self.alive):
            #Fazer o contador diminuir durante a execução da thread do planeta
            globals.acquireNukeTimerDecrease()
            if (self.timerNorth > 0):
                self.timerNorth -= 1
            if (self.timerSouth > 0):
                self.timerSouth -= 1
            globals.releaseNukeTimerDecrease()
            