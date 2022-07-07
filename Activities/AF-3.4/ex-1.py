from time import sleep
from random import randint
from threading import Thread, Lock, Condition

def produtor(id):
  global buffer
  for i in range(10):
    sleep(randint(0,2))           # fica um tempo produzindo...
    item = 'item ' + str(i)
    with lock:
      while len(buffer) == tam_buffer:
        print('>>> Buffer cheio. Produtor ira aguardar.')
        lugar_no_buffer.wait()    # aguarda que haja lugar no buffer
      buffer.append(item)
      print('Produzido %s (ha %i itens no buffer)' % (item,len(buffer)))
      print(f"Id: {id}")
      item_no_buffer.notify()

def consumidor(id):
  global buffer
  for i in range(10):
    with lock:
      while len(buffer) == 0:
        print('>>> Buffer vazio. Consumidor ira aguardar.')
        item_no_buffer.wait()   # aguarda que haja um item para consumir 
      item = buffer.pop(0)
      print('Consumido %s (ha %i itens no buffer)' % (item,len(buffer)))
      print(f"Id: {id}")
      lugar_no_buffer.notify()
    sleep(randint(0,2))         # fica um tempo consumindo...

buffer = []
tam_buffer = 5
lock = Lock()

lugar_no_buffer = Condition(lock)

item_no_buffer = Condition(lock)

produtor1 = Thread(target=lambda: produtor(0))
produtor2 = Thread(target=lambda: produtor(1))

consumidor1 = Thread(target=lambda: consumidor(2))
consumidor2 = Thread(target=lambda: consumidor(3))

produtor1.start()
produtor2.start()

consumidor1.start()
consumidor2.start()

produtor1.join()
produtor2.join()

consumidor1.join()
consumidor2.join()