from logging import exception
import globals
from threading import Thread, Condition, Lock
from space.rocket import Rocket
from random import *
#from random import choice, random
from time import sleep

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
    
    def base_rocket_launch(self, rocket):
        if (rocket.name == "LION"):
            match self.name:
                    case 'ALCANTRA':
                        if self.fuel >= 100:
                            self.fuel -= 100
                            #lógica do foguete indo até a lua OK
                            rocket.voyage_to_moon()
                    case _:
                        if self.fuel >= 115:
                            self.fuel -= 115
                            #lógica do foguete indo até a lua OK
                            rocket.voyage_to_moon()
        else:
            match rocket.name:
                case 'DRAGON':
                    match self.name:
                        case 'ALCANTRA':
                            if self.fuel >= 70:
                                self.fuel -= 70
                                #fazer lógica do foguete indo até o planeta OK
                        case 'MOON':
                            if self.fuel >= 50:
                                self.fuel -= 50
                                #fazer lógica do foguete indo até o planeta OK
                        case _:
                            if self.fuel >= 100:
                                self.fuel -= 100
                                #fazer lógica do foguete indo até o planeta OK
                case 'FALCON':
                    match self.name:
                        case 'ALCANTRA':
                            if self.fuel >= 100:
                                self.fuel -= 100
                                #fazer lógica do foguete indo até o planeta OK
                        case 'MOON':
                            if self.fuel >= 90:
                                self.fuel -= 90
                                #fazer lógica do foguete indo até o planeta OK
                        case _:
                            if self.fuel >= 120:
                                self.fuel -= 120
                                #fazer lógica do foguete indo até o planeta OK
                case _:
                    print("Invalid rocket name")

            # Escolhe aleatoriamente o destino do foguete
            destination = choice(list(globals.get_planets_ref().values()))

            # Caso o planeta tenha sido atingido recentemente por 2 bombas o foguete aguarda para ser lançado.
            while (destination.timerNorth > 0 and destination.timerSouth > 0):
                sleep(.1)
            else:
                rocket.voyage(destination)

    def refuel_oil(self):
        mines = globals.get_mines_ref() #busca dict de minas
        oil_mine = mines['oil_earth'] #seleciona mina de petróleo
        if(oil_mine.unities >= 120): #se houver combustivel na mina
            '''adicionar mutex aqui para somente uma base acessar a mina'''
            oil_mine.unities = oil_mine.unities - 120 #retira combustivel da mina
            self.fuel = self.fuel + 120 #adiciona combustivel na base
            print(f"Base {self.name} abasteceu e tem agora: COMBUSTIVEL:{self.fuel}.")

    def refuel_uranium(self):
        mines = globals.get_mines_ref() #busca dict de minas
        uranium_mine = mines['uranium_earth'] #seleciona mina de urano
        if(uranium_mine.unities >= 35): #houver urano na mina...
            '''adicionar mutex aqui para somente uma base acessar a mina'''
            uranium_mine.unities = uranium_mine.unities - 35 #retira urano da mina
            self.uranium = self.uranium + 35 #adiciona urano na base
            print(f"Base {self.name} abasteceu e tem agora: URANO:{self.uranium}.")
    
    def create_rocket(self):
        rocket = None
        if((self.name != 'MOON') and globals.get_moon_need_resources() and (globals.get_lions_alive() < 2)): #se a lua precisa de recursos e tem menos de 2 lions prontos
            if(self.uranium >= 75 and self.fuel >=120): #se tem recursos suficientes para transporte
                lua = globals.get_bases_ref()['moon'] #referencia a lua pra monitorar capacidades
                rocket = Rocket('LION') #cria foguete lion
                self.rockets += 1 #aumenta foguetes na base
                globals.acquire_lion() #protege a integridade da qtd de lions
                globals.set_lions_alive(globals.get_lions_alive() + 1) #indica que existe mais um foguete lion para nao ter excedentes
                globals.release_lion() #libera a variável pra uso
                if lua.uranium < lua.constraints[0]: #garante que só vai mandar uranio se precisar
                    self.uranium -= 75
                    rocket.uranium_cargo += 75
                self.fuel -= 120
                rocket.fuel_cargo += 120
                print(f'Base {self.name} criou um foguete {rocket.name}')
        else:
            if(self.uranium >= 35): #se tem urano suficiente pra criar ogiva
                if(random() < 0.5): #cria foguetes explosivos aleatóriamente
                    rocket = Rocket('DRAGON')
                else:
                    rocket = Rocket('FALCON')
                self.uranium -= 35 #reduz urano para criar ogiva
                self.rockets += 1 #aumenta foguetes na base
                print(f'Base {self.name} criou um foguete {rocket.name}')
        return rocket



    def run(self):
        globals.acquire_print()
        self.print_space_base_info()
        globals.release_print()
        rockets = []
        cost_per_dragon = 0
        cost_per_falcon = 0
        cost_per_lion = 0
        lock = Lock()
        match self.name:
            case 'MOON':
                cost_per_dragon = 50
                cost_per_falcon = 90
            case 'ALCANTRA':
                cost_per_dragon = 70
                cost_per_falcon = 100
                cost_per_lion = 100
            case 'MOSCOW':
                cost_per_dragon = 100
                cost_per_falcon = 120
                cost_per_lion = 115
            case 'CANAVERAL CAPE':
                cost_per_dragon = 100
                cost_per_falcon = 120
                cost_per_lion = 115
        cost_per_rocket = {
            'DRAGON': cost_per_dragon,
            'FALCON': cost_per_falcon,
            'LION': cost_per_lion
        }

        while(globals.get_release_system() == False):
            pass

        while(True):
            #TENTA FAZER LANÇAMENTO
            if(len(rockets) > 0 and self.fuel >= cost_per_rocket[rockets[0].name]): #se tem foguete pra lançar e tiver combustivel pro lançamento
                launched = rockets.pop(0) 
                self.base_rocket_launch(launched) #lança primeiro foguete adicionado à lista
                self.rockets -= 1 #reduz número de foguetes na base
                print(f'Base {self.name} lançou {launched.name}:{launched.id}')

            #ABASTECE E CRIA FOGUETES
            lions_alive = globals.get_lions_alive() 
            if(self.name == 'MOON'): # A lua é a unica base que se comporta diferente para receber recursos
                #se um dos armazenamentos nao está cheio e tem menos de dois foguetes de carga prontos
                if (self.fuel < self.constraints[1] or self.uranium < self.constraints[0]) and lions_alive < 2:
                    globals.set_moon_need_resources(True) #a lua precisará de recursos
                    print(f"{self.name} requisita recursos!")
                #se ambos armazenamentos da lua estão cheios
                elif(self.uranium >= self.constraints[0] and self.fuel >= self.constraints[1]):
                    globals.set_moon_need_resources(False) #a lua para de requisitar recursos
                    print(f"{self.name} não precisa mais de recursos!")
                if(self.rockets < self.constraints[2]): #se tem capacidade pra armazenar foguetes
                    rocket = self.create_rocket() #cria foguete (a verificação de disponibilidade de recursos é feita na func)
                    if rocket != None: #se o retorno foi um foguete...
                        rockets.append(rocket) #adiciona foguete na lista de foguetes da base
            else: #Comportamento de qualquer outra base
                if(self.fuel < self.constraints[1]):#colocando essa condição aqui garante que no longo prazo se nao for necessário não haverá custo com a execução da função
                    self.refuel_oil() #abastece combustível
                if(self.uranium < self.constraints[0]):#colocando essa condição aqui garante que no longo prazo se nao for necessário não haverá custo com a execução da função
                    self.refuel_uranium() #abastece urano
                if self.rockets < self.constraints[2]: #se tem capacidade pros foguetes...
                    rocket = self.create_rocket() #cria foguete
                    if rocket != None:
                        rockets.append(rocket) #adiciona foguete na lista de foguetes da base
            
