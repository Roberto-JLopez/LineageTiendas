import pyautogui
import time
#imagenes
agree="imagenes/Agree.png"
inicio="imagenes/Inicio.png"
log="imagenes/log.png"
message="imagenes/Message.png"
ok="imagenes/Ok.png"
sepu="imagenes/Sepu.png"
Star="imagenes/Star.png"
login="imagenes/Login.png"
Starlog="imagenes/Starlog.png"
buy="imagenes/Buy.png"

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


def comenzar_compra(imagen, certeza, intentos=10):
    for _ in range(intentos):
        try:
            print(f"Buscando la imagen: {imagen} con confianza: {certeza}")
            localizacion = pyautogui.locateCenterOnScreen(image=imagen, minSearchTime=5, confidence=certeza)

            if localizacion:
                click(localizacion)
                print("Compra realizada exitosamente.")
                return True

        except pyautogui.ImageNotFoundException:
            print(f"Error: No se encontró la imagen {imagen} después de {intentos} intentos.")


    print("No se pudo completar la compra.")
    return False


time.sleep(2)
compra = comenzar_compra(Star, 0.6, 5)