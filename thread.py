import machine
import time
import ufirebase as firebase
import network
import _thread

led = machine.Pin(2,machine.Pin.OUT)
def wifiSetup():
  #wifi ser modo passivo
  sta_if = network.WLAN(network.STA_IF)
  #ativa o modulo wifi do esp32 no modo passivo
  sta_if.active(True)
  #conectando a uma rede wifi (nome da rede e pass)
  sta_if.connect('Wokwi-GUEST', '')
  
  #fica verificando se esta conectado a rede
  while not sta_if.isconnected():
    print(".", end="")
    time.sleep(0.1)

  print("Conectado")

firebase.setURL("https://automacao2-5a4c3-default-rtdb.firebaseio.com/")
def setFirebase():
  firebase.put("/fiap",{"led":"valor1"}, bg=0 )

def setLed():
    global get_local
    while True:
        print("valor:"+ str(get_local))
        time.sleep(1)
        if get_local == 1:
            led.value(1)
        else:
            led.value(0)

def getFirebase():
    global get_local
    while True:
        firebase.get("/fiap/led","dado")
        get_local = int(firebase.dado)

        print("get:"+str(firebase.dado))

get_local = 0 

wifiSetup()
#setFirebase()
_thread.start_new_thread(setLed,())
getFirebase()



  

