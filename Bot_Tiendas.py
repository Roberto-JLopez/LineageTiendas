import pyautogui
import subprocess
import time
import keyboard
import threading
import sys
#ruta del juego 
game=r"C:\Program Files (x86)\Lineage II Elite C4 - copia\system\L2.exe"

#imagenes
agree="imagenes/agree.png"
exit="imagenes/exit.png"
inicio="imagenes/inicio.png"
log="imagenes/Log.png"
message="imagenes/message.png"
ok="imagenes/ok.png"
sepu="imagenes/sepu.png"
Star="imagenes/star.png"
login="imagenes/login.png"
Starlog="imagenes/starlog.png"
buy="imagenes/buy.png"



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
            localizacion=pyautogui.locateCenterOnScreen(imagen, confidence=certeza)
            if localizacion:
                click(localizacion)
                print ("ingresando")
                return True
        except pyautogui.ImageNotFoundException:
         print("Error: Imagen de no encontrada. Intentando nuevamente...")
         time.sleep(5)
        # Si llegamos aquí, significa que no se encontró la imagen después de varios intentos
    print("No se pudo localizar la imagen después de varios intentos.")
    exit()  # Terminar el programa
#arrancar la compra
def comenzar_compra (imagen, certeza, intentos=10):
    for _ in range(intentos):
        try:
            localizacion=pyautogui.locateCenterOnScreen(imagen, confidence=certeza)
            if localizacion:
                click(localizacion)
                print ("comprando listo")
                return True
        except pyautogui.ImageNotFoundException:
         print("Error: Imagen no encontrada. Intentando nuevamente...")
         time.sleep(5)
        # Si llegamos aquí, significa que no se encontró la imagen después de varios intentos
    print("No se pudo localizar la imagen después de varios intentos.")
    exit()  # Terminar el programa
#poner mensaje
def mensaje (imagen, certeza, intentos=10):
    for _ in range(intentos):
        try:
            localizacion=pyautogui.locateCenterOnScreen(imagen, confidence=certeza)
            if localizacion:
                click(localizacion)
                keyboard.write(">>Entrance Sepulcher<<")
                pyautogui.press('enter')
                print ("mensaje listo")
                return True
        except pyautogui.ImageNotFoundException:
         print("Error: Imagen no encontrada. Intentando nuevamente...")
         time.sleep(5)
        # Si llegamos aquí, significa que no se encontró la imagen después de varios intentos
    print("No se pudo localizar la imagen después de varios intentos.")
    exit()  # Terminar el programa
   
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
            pyautogui.press("enter")
            pyautogui.write("/buy")
            pyautogui.press("enter")
            print("Error: Imagen no encontrada. Intentando nuevamente...")
            time.sleep(5)
     # Si llegamos aquí, significa que no se encontró la imagen después de varios intentos
    print("No se pudo localizar la imagen después de varios intentos.")
    exit()  # Terminar el programa

#logueo    
    
def loguenado_cuenta (imagen, username, password, certeza=0.8, intentos=10):
    for _ in range(intentos):
        try:
            localizacion = pyautogui.locateOnScreen(imagen, confidence=certeza)
            if localizacion:
                coordenadas=pyautogui.center(localizacion)
                click(coordenadas)               
                pyautogui.write(username)
                pyautogui.press("tab")
                pyautogui.write(password)
                print("Cuenta logueada exitosamente")
                return True
# Si no se encuentra la imagen, esperamos 5 segundos antes de intentar nuevamente
        except pyautogui.ImageNotFoundException:
         print("Error: Imagen no encontrada. Intentando nuevamente...")
         time.sleep(5)
     # Si llegamos aquí, significa que no se encontró la imagen después de varios intentos
    print("No se pudo localizar la imagen después de varios intentos.")
    exit()  # Terminar el programa

# Función para finalizar el programa cuando se presione Alt+Q
def monitorear_salir():
    print("Monitoreando para salir...")
    while True:
        if keyboard.is_pressed("alt") and keyboard.is_pressed("q"):
            print("Tecla Alt + Q presionada. Terminando el programa...")
            sys.exit()  # Terminar el programa de forma segura

# Iniciar el hilo para monitorear
hilo_monitoreo = threading.Thread(target=monitorear_salir, daemon=True)
hilo_monitoreo.start()

#godar = ["ventas0001","ventas0002","ventas0003","ventas0004","ventas0005","ventas0006",
#"ventas0007","ventas0008","ventas0009","ventas0010"]
#aden = ["ventas0011","ventas0012","ventas0013","ventas0014","ventas0015","ventas0016",
# "ventas0017","ventas0018""ventas0019","ventas0020"]
username= ["ventas0018",
"ventas0019",]
password = "1234"
for i in username:
    print (f"logueando {i}")
    # Paso 1: Abrir el juego
    subprocess.Popen(game)
    print("abriendo el juego")
    time.sleep(10)
    logueo_exitoso= loguenado_cuenta(login, i, password, 0.8, 5)
    time.sleep(2)
    buscar_login= buscar_elemento(log,0.8,10)
    time.sleep(2)
    buscar_agree=buscar_elemento(agree,0.8,10)
    time.sleep(2)
    buscar_ok=buscar_elemento(ok,0.8,10)
    time.sleep(2)
    buscar_starlog=buscar_elemento(Starlog,0.8,5)
    time.sleep(10)
    pyautogui.write("/buy")
    pyautogui.press("enter")
    time.sleep(2)
    comrpar_sepu=compra_iten(sepu)
    poner_mensaje=mensaje(message,0.8,5)
    time.sleep(2)
    compra= comenzar_compra(Star,0.8,5)
    # Presiona Alt + H
    pyautogui.hotkey('alt', 'h')
    # Minimizar la ventana activa
    pyautogui.hotkey('win', 'down')
print (f"{i} logueada pasamos a {i+1}")


