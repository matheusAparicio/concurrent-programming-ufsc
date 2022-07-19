from threading import Lock

#  A total alteração deste arquivo é permitida.
#  Lembre-se de que algumas variáveis globais são setadas no arquivo simulation.py
#  Portanto, ao alterá-las aqui, tenha cuidado de não modificá-las. 
#  Você pode criar variáveis globais no código fora deste arquivo, contudo, agrupá-las em
#  um arquivo como este é considerado uma boa prática de programação. Frameworks como o Redux,
#  muito utilizado em frontend em libraries como o React, utilizam a filosofia de um store
#  global de estados da aplicação e está presente em sistemas robustos pelo mundo.

release_system = False
mutex_print = Lock()
mutexNukeTimerDecrease = Lock()
mutexPlanetBombed = Lock()
mutexRocketNukePlanet = Lock()
planets = {}
bases = {}
mines = {}
simulation_time = None

moon_need_resources = False #variável destinada a saber se a lua precisa de recursos
lions_alive = 0
mutex_lion = Lock()
lock_oil = Lock()
lock_uranium = Lock()


# Mutex usado no voyage do rocket.py para definir o comportamento do foguete.
def acquireRocketNukePlanet():
    global mutexRocketNukePlanet
    mutexRocketNukePlanet.acquire()

def releaseRocketNukePlanet():
    global mutexRocketNukePlanet
    mutexRocketNukePlanet.release()

# Quando um planeta for atingido por uma bomba, garante que a nuke_detected do planeta seja executada completamente.
def acquirePlanetBombed():
    global mutexPlanetBombed
    mutexPlanetBombed.acquire()

def releasePlanetBombed():
    global mutexPlanetBombed
    mutexPlanetBombed.release()

# Garante que os timers dos polos norte e sul dos planetas sejam decrementados juntos.
def acquireNukeTimerDecrease():
    global mutexNukeTimerDecrease
    mutexNukeTimerDecrease.acquire()

def releaseNukeTimerDecrease():
    global mutexNukeTimerDecrease
    mutexNukeTimerDecrease.release()

def set_lions_alive(n):
    global lions_alive
    lions_alive = n

def get_lions_alive():
    global lions_alive
    return lions_alive

def set_moon_need_resources(do_need): #func que altera o estado da necessidade de recurson na lua
    global moon_need_resources
    moon_need_resources = do_need

def get_moon_need_resources(): #func que retorna se a lua precisa de recursos
    global moon_need_resources
    return moon_need_resources

def acquire_lion(): #adquire mutex que protege a variável lion
    global mutex_lion
    mutex_lion.acquire()

def release_lion():#libera mutex que protege a variável lion
    global mutex_lion
    mutex_lion.release()

def acquire_oil(): #adquire mutex que protege acesso à mina de petróleo
    global mutex_lion
    lock_oil.acquire()

def release_oil():#libera mutex que protege acesso à mina de petróleo
    global mutex_lion
    lock_oil.release()

def acquire_uranium(): #adquire mutex que protege acesso à mina de uranio
    global mutex_lion
    lock_uranium.acquire()

def release_uranium():#libera mutex que protege acesso à mina de uranio
    global mutex_lion
    lock_uranium.release()

def acquire_print():
    global mutex_print
    mutex_print.acquire()

def release_print():
    global mutex_print
    mutex_print.release()

def set_planets_ref(all_planets):
    global planets
    planets = all_planets

def get_planets_ref():
    global planets
    return planets

def set_bases_ref(all_bases):
    global bases
    bases = all_bases

def get_bases_ref():
    global bases
    return bases

def set_mines_ref(all_mines):
    global mines
    mines = all_mines

def get_mines_ref():
    global mines
    return mines

def set_release_system():
    global release_system
    release_system = True

def get_release_system():
    global release_system
    return release_system

def set_simulation_time(time):
    global simulation_time
    simulation_time = time

def get_simulation_time():
    global simulation_time
    return simulation_time
