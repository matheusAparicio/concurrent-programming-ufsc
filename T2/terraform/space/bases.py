import globals
from threading import Thread
from space.rocket import Rocket
from random import choice

class SpaceBase(Thread):

    ################################################
    # O CONSTRUTOR DA CLASSE NÃO PODE SER ALTERADO #
    ################################################
    def __init__(self, name, fuel, uranium, rockets):
        Thread.__init__(self)
        self.name = name
        self.uranium = 0
        self.fuel = 0
        self.rockets = 0
        self.constraints = [uranium, fuel, rockets]

    def print_space_base_info(self):
        print(f"🔭 - [{self.name}] → 🪨  {self.uranium}/{self.constraints[0]} URANIUM  ⛽ {self.fuel}/{self.constraints[1]}  🚀 {self.rockets}/{self.constraints[2]}")
    
    def base_rocket_resources(self, rocket_name):
        match rocket_name:
            case 'DRAGON':
                if self.uranium > 35 and self.fuel > 50:
                    self.uranium = self.uranium - 35
                    if self.name == 'ALCANTARA':
                        self.fuel = self.fuel - 70
                    elif self.name == 'MOON':
                        self.fuel = self.fuel - 50
                    else:
                        self.fuel = self.fuel - 100
            case 'FALCON':
                if self.uranium > 35 and self.fuel > 90:
                    self.uranium = self.uranium - 35
                    if self.name == 'ALCANTARA':
                        self.fuel = self.fuel - 100
                    elif self.name == 'MOON':
                        self.fuel = self.fuel - 90
                    else:
                        self.fuel = self.fuel - 120
            case 'LION':
                if self.uranium > 35 and self.fuel > 100:
                    self.uranium = self.uranium - 35
                    if self.name == 'ALCANTARA':
                        self.fuel = self.fuel - 100
                    else:
                        self.fuel = self.fuel - 115
            case _:
                print("Invalid rocket name")


    def refuel_oil(self):
        mines = globals.get_mines_ref() #busca dict de minas
        oil_mine = mines['oil_earth'] #seleciona mina de petróleo
        if(self.fuel < self.constraints[1] and oil_mine.unities >= 125): #se houver capacidade e combustivel na mina
            #adicionar mutex aqui para somente uma base acessar a mina
            oil_mine.unities = oil_mine.unities - 125 #retira combustivel da mina
            self.fuel = self.fuel + 125 #adiciona combustivel na base
            print(f"Base {self.name} está abasteceu e tem agora {self.fuel} unidades de combustível.")

    def refuel_uranium(self):
        mines = globals.get_mines_ref() #busca dict de minas
        uranium_mine = mines['uranium_earth'] #seleciona mina de urano
        if(self.uranium < self.constraints[0] and uranium_mine.unities >= 50): #houver capacidade e urano na mina...
            #adicionar mutex aqui para somente uma base acessar a mina
            uranium_mine.unities = uranium_mine.unities - 50 #retira urano da mina
            self.uranium = self.uranium + 50 #adiciona urano na base
            print(f"Base {self.name} está abasteceu e tem agora {self.uranium} unidades de urano.")


    def run(self):
        globals.acquire_print()
        self.print_space_base_info()
        globals.release_print()

        while(globals.get_release_system() == False):
            pass

        while(True):
            self.refuel_oil()
            self.refuel_uranium()
            
