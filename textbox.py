import turtle

ventanaPrincipal = turtle.Screen()
ventanaPrincipal.title("Buscaminas by @Lucazz_82")
anchoVentanaPrincipal = 800
altoVentanaPrincipal = 600
ventanaPrincipal.setup(width= anchoVentanaPrincipal, height=altoVentanaPrincipal)
ventanaPrincipal.bgcolor("black")
ventanaPrincipal.tracer(0)

#print(25/2*25)
#print(round(25/2*25))
def redondear(numero):
    return int(numero)

def prueba(valor):
    if valor:
        print("Entre al if")
    print("estoy afuera del if")

#prueba(True)

class Poronga():
    arriba = "Hola"
    numero = 0

    def sumarNumero(self, *args):
        self.numero += 1

    def imprimirNumero(self, *args):
        print(self.numero)
    pass

poronga = Poronga()
ventanaPrincipal.onclick(poronga.sumarNumero, 1)
ventanaPrincipal.onclick(poronga.imprimirNumero, 3)

a = [10,5]
b = [10,5]

#array = sum(i in a for j in b)

def comprobar(valor):
    return valor in b

def agregar_cero(valor):
    if valor < 10:
        return "0"+ str(valor)
    pass
tablero = [[0,1],[3,4]]

print(tablero[0][1])
if 0:
    print("hola")
else:
    print("chau")

while True:
    ventanaPrincipal.update()
    