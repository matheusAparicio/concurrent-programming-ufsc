from random import *
from time import sleep
import globals


class Rocket:

    ################################################
    # O CONSTRUTOR DA CLASSE NÃO PODE SER ALTERADO #
    ################################################
    def __init__(self, type):
        self.id = randrange(1000)
        self.name = type
        if(self.name == 'LION'):
            self.fuel_cargo = 0
            self.uranium_cargo = 0
            

    def nuke(self, planet): # Permitida a alteração
        targetPole = choice(["north", "south"])
        planet.nuke_detected(self.damage(), targetPole)
        print(f"[EXPLOSION] - The {self.name} ROCKET reached the planet {planet.name} on {targetPole} Pole")
    
    def voyage(self, planet): # Permitida a alteração (com ressalvas)
        # Essa chamada de código (do_we_have_a_problem e simulation_time_voyage) não pode ser retirada.
        # Você pode inserir código antes ou depois dela e deve
        # usar essa função.
        self.simulation_time_voyage(planet)
        failure =  self.do_we_have_a_problem()
        self.nuke(planet)

    def voyage_to_moon(self):
        print(f'Foguete {self.name} com ID {self.id} indo pra Lua')
        sleep(0.011) #representa 4 dias de viagem
        lua = globals.get_bases_ref()['moon'] #referencia pra lua
        # lua.uranium += self.uranium_cargo #abastece lua com urano
        # lua.fuel += self.fuel_cargo #abastece lua com combustivel
        globals.acquire_lion() #protege a integridade da qtd de lions
        globals.set_lions_alive(globals.get_lions_alive() - 1) #libera vaga pra criação de outro lion
        lua.refuel_from_rocket(self)
        print(f'Foguete {self.name} com ID {self.id} abasteceu a Lua')
        globals.release_lion() #libera a variável pra uso
        print(f'Base {lua.name} foi abastecida e tem agora URANO: {lua.uranium} COMBUSTÌVEL: {lua.fuel}')


    ####################################################
    #                   ATENÇÃO                        # 
    #     AS FUNÇÕES ABAIXO NÃO PODEM SER ALTERADAS    #
    ###################################################
    def simulation_time_voyage(self, planet):
        if planet.name == 'MARS':
            sleep(2) # Marte tem uma distância aproximada de dois anos do planeta Terra.
        else:
            sleep(5) # IO, Europa e Ganimedes tem uma distância aproximada de cinco anos do planeta Terra.

    def do_we_have_a_problem(self):
        if(random() < 0.15):
            if(random() < 0.51):
                self.general_failure()
                return True
            else:
                self.meteor_collision()
                return True
        return False
            
    def general_failure(self):
        print(f"[GENERAL FAILURE] - {self.name} ROCKET id: {self.id}")
    
    def meteor_collision(self):
        print(f"[METEOR COLLISION] - {self.name} ROCKET id: {self.id}")

    def successfull_launch(self, base):
        if random() <= 0.1:
            print(f"[LAUNCH FAILED] - {self.name} ROCKET id:{self.id} on {base.name}")
            return False
        return True
    
    def damage(self):
        return random()

    def launch(self, base, planet):
        if(self.successfull_launch(base)):
            print(f"[{self.name} - {self.id}] launched.")
            self.voyage(planet)        
