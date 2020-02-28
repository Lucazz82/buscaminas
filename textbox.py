import turtle

def abrirMenu(*args):
    turtle.numinput("Menu", "Ingrese un numero")

#print(25/2*25)
#print(round(25/2*25))
def redondear(numero):
    return int(numero)

cerrar = True
while cerrar:
    numero = input("Ingrese un numero: ")
    if numero == 'a':
        cerrar = False
    else:
        numero = float(numero)
        print(redondear(numero))