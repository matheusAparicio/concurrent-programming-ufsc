import globals
from threading import Thread
from space.rocket import Rocket
from random import choice, random

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
        if(oil_mine.unities >= 125): #se houver capacidade e combustivel na mina
            #adicionar mutex aqui para somente uma base acessar a mina
            oil_mine.unities = oil_mine.unities - 125 #retira combustivel da mina
            self.fuel = self.fuel + 125 #adiciona combustivel na base
            print(f"Base {self.name} está abasteceu e tem agora {self.fuel} unidades de combustível.")

    def refuel_uranium(self):
        mines = globals.get_mines_ref() #busca dict de minas
        uranium_mine = mines['uranium_earth'] #seleciona mina de urano
        if(uranium_mine.unities >= 50): #houver capacidade e urano na mina...
            #adicionar mutex aqui para somente uma base acessar a mina
            uranium_mine.unities = uranium_mine.unities - 50 #retira urano da mina
            self.uranium = self.uranium + 50 #adiciona urano na base
            print(f"Base {self.name} está abasteceu e tem agora {self.uranium} unidades de urano.")

    def refuel_from_rockets(self): #func para base receber recursos de um foguete
        pass #fazer lógica
    
    def create_rocket(self):
        if(self.name != 'MOON' and globals.moon_need_resources): #se a lua precisa de recursos
            if(self.uranium >= 75 and self.fuel >=120): #se tem recursos suficientes
                rocket = Rocket('LION') #cria foguete lion
                self.rockets += 1 #aumenta foguetes na base
                globals.set_lions_alive(globals.get_lions_alive() + 1) #indica que existe mais um foguete lion para nao ter excedentes
                self.uranium -= 75
                rocket.uranium_cargo += 75
                self.fuel -= 120
                rocket.fuel_cargo +=120

                return rocket
        else:
            if(self.uranium > 35): #se tem urano suficiente pra criar ogiva
                if(random() < 0.5): #cria foguetes explosivos aleatóriamente
                    rocket = Rocket('DRAGON')
                else:
                    rocket = Rocket('FALCON')
    def run(self):
        globals.acquire_print()
        self.print_space_base_info()
        globals.release_print()

        while(globals.get_release_system() == False):
            pass

        while(True):
            if(self.name == 'MOON'): # A lua é a unica base que se comporta diferente para receber recursos
                #se o armazenamento nao está cheio e tem menos de dois foguetes de carga prontos...
                if((self.fuel < self.constraints[1] or self.uranium <self.constraints[0]) and globals.lions_alive < 3):
                    globals.set_moon_need_resources(True) #a lua precisará de recursos

                elif(self.fuel < self.constraints[1] or self.uranium <self.constraints[0]):
                    self.refuel_from_rockets(self) #recebe recursos do foguete lion

            else:
                if(self.fuel < self.constraints[1]):#colocando essa condição aqui garante que no longo prazo se nao for necessário não haverá custo com a execução da função
                    self.refuel_oil()
                elif(self.uranium < self.constraints[0]):#colocando essa condição aqui garante que no longo prazo se nao for necessário não haverá custo com a execução da função
                    self.refuel_uranium()
            
