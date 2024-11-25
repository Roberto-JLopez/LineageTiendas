import pyautogui
import subprocess
import time
import keyboard

#ruta del juego 
game=r"C:\Program Files (x86)\Lineage II Elite C4 - copia\system\L2.exe"
username=("ventas0020")
password=("1234")

#imagenes
agree=r"C:\Users\rober\PycharmProjects\LineageTiendas\Agree.png"
exit=r"C:\Users\rober\PycharmProjects\LineageTiendas\exit.png"
inicio=r"C:\Users\rober\PycharmProjects\LineageTiendas\inicio.png"
log=r"C:\Users\rober\PycharmProjects\LineageTiendas\Log.png"
message=r"C:\Users\rober\PycharmProjects\LineageTiendas\message.png"
ok=r"C:\Users\rober\PycharmProjects\LineageTiendas\ok.png"
sepu=r"C:\Users\rober\PycharmProjects\LineageTiendas\sepu.png"
Star=r"C:\Users\rober\PycharmProjects\LineageTiendas\star.png"
login=r"C:\Users\rober\PycharmProjects\LineageTiendas\login.png"
Starlog=r"C:\Users\rober\PycharmProjects\LineageTiendas\starlog.png"
buy=r"C:\Users\rober\PycharmProjects\LineageTiendas\buy.png"

# Función para hacer click
def click(buscar_elemento):
    pyautogui.click(buscar_elemento)  # Simular un clic izquierdo del ratón
    pyautogui.mouseDown()  # Presiona el botón izquierdo del ratón
    time.sleep(0.01)  # Espera 0.01 segundos
    pyautogui.mouseUp()  # Suelta el botón izquierdo del ratón

# Función para hacer click
def dobleclick(buscar_elemento):
    pyautogui.doubleClick(buscar_elemento)  # Simular un clic izquierdo del ratón
    pyautogui.mouseDown()  # Presiona el botón izquierdo del ratón
    time.sleep(0.01)  # Espera 0.01 segundos
    pyautogui.mouseUp()  # Suelta el botón izquierdo del ratón

#buscar elementos ok, star etc
def buscar_elemento (imagen, certeza, intentos=10):
    for _ in range(intentos):
        try:
            localicazacion=pyautogui.locateCenterOnScreen(imagen, confidence=certeza)
            if localicazacion:
                click(localicazacion)
                print ("ingresando")
                return True
        except pyautogui.ImageNotFoundException:
         print("Error: Imagen no encontrada. Intentando nuevamente...")
         time.sleep(5)
        # Si llegamos aquí, significa que no se encontró la imagen después de varios intentos
    print("No se pudo localizar la imagen después de varios intentos.")
    return False   


def poner_a_comprar (imagenIten):
     pyautogui.press("enter")
     pyautogui.write("/buy")
     pyautogui.press("enter")
     compra_iten(imagenIten)

     #Compra de itens
def compra_iten (imagenIten, certeza=0.8, intentos=5):
    for _ in range(intentos):
        try:
            localizacion=pyautogui.locateOnScreen(imagenIten, confidence=certeza)
            if localizacion:
                coordenadas=pyautogui.center(localizacion)
                dobleclick(coordenadas)
                time.sleep(1)
                pyautogui.write ("100000000")
                pyautogui.press('enter')
                pyautogui.write("2")
                pyautogui.press('enter')
                print ("comprando sepu")
                return True
            
        except pyautogui.ImageNotFoundException:
         print("Error: Imagen no encontrada. Intentando nuevamente...")
         time.sleep(5)
     # Si llegamos aquí, significa que no se encontró la imagen después de varios intentos
    print("No se pudo localizar la imagen después de varios intentos.")
    return False

time.sleep(2)
comrpar_sepu=poner_a_comprar(sepu)