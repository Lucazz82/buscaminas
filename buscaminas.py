import turtle
import random
#import textbox

#------------------------------------------------------------------------------#
# Ventana
ventanaPrincipal = turtle.Screen()
ventanaPrincipal.title("Buscaminas by @Lucazz_82")
anchoVentanaPrincipal = 800
altoVentanaPrincipal = 600
ventanaPrincipal.setup(width= anchoVentanaPrincipal, height=altoVentanaPrincipal)
ventanaPrincipal.bgcolor("black")
ventanaPrincipal.tracer(0)
#------------------------------------------------------------------------------#
# Variables
imagenFondo = './imagenes/0.gif'
ventanaPrincipal.addshape(imagenFondo)

imagenDelante = './imagenes/delante.gif'
ventanaPrincipal.addshape(imagenDelante)

imagenUno = './imagenes/1.gif'
ventanaPrincipal.addshape(imagenUno)

imagenDos = './imagenes/2.gif'
ventanaPrincipal.addshape(imagenDos)

imagenTres = './imagenes/3.gif'
ventanaPrincipal.addshape(imagenTres)

imagenCuatro = './imagenes/4.gif'
ventanaPrincipal.addshape(imagenCuatro)

imagenCinco = './imagenes/5.gif'
ventanaPrincipal.addshape(imagenCinco)

imagenSeis = './imagenes/6.gif'
ventanaPrincipal.addshape(imagenSeis)

imagenSiete = './imagenes/7.gif'
ventanaPrincipal.addshape(imagenSiete)

imagenOcho = './imagenes/8.gif'
ventanaPrincipal.addshape(imagenOcho)

imagenBomba = './imagenes/bomba.gif'
ventanaPrincipal.addshape(imagenBomba)

imagenBandera = './imagenes/bandera.gif'
ventanaPrincipal.addshape(imagenBandera)

dimensionesCuadrado = 25

ultimoClick = []
#------------------------------------------------------------------------------#
# Clases
class Cuadrado(turtle.Turtle):
    def __init__(self, valor, index):
        turtle.Turtle.__init__(self)
        self.estado = 0 # 0 = vacio / 1-8 = ese numero / -1 = bomba
        self.valorOculto = valor
        self.index = index

    def clickIzquierdo(self, *args):
        self.actualizarUltimoClick()
        if self.estado == 0:
            #celdaVacia 
            pass
        elif self.estado == -1:
            #perder
            pass
        else:
            self.cambiarImagen()
        

    def actualizarUltimoClick(self):
        global ultimoClick
        ultimoClick = self.index
        print(ultimoClick)

    def cambiarImagen(self):
        if self.estado == 0:
            self.shape(imagenFondo)

        elif self.estado == 1:
            self.shape(imagenUno)
        
        elif self.estado == 2:
            self.shape(imagenDos)
        
        elif self.estado == 3:
            self.shape(imagenTres)
        
        elif self.estado == 4:
            self.shape(imagenCuatro)

        elif self.estado == 5:
            self.shape(imagenCinco)

        elif self.estado == 6:
            self.shape(imagenSeis)

        elif self.estado == 7:
            self.shape(imagenSiete)
        
        elif self.estado == 8:
            self.shape(imagenOcho)

        
    def contarBombas(self):
        alrededores = [ 
            [self.index[0]+1, self.index[1]-1],
            [self.index[0]-1, self.index[1]],
            [self.index[0]-1, self.index[1]-1],
            [self.index[0], self.index[1]+1],
            [self.index[0], self.index[1]-1],
            [self.index[0]+1, self.index[1]+1],
            [self.index[0]+1, self.index[1]-1],
            [self.index[0]+1, self.index[1]]
        ]
        for celda in alrededores:
            cantidadBombas = 0
            if columnas[celda[0]][celda[1]].estado == -1:
                cantidadBombas += 1
        self.estado = cantidadBombas




    pass
#------------------------------------------------------------------------------#
# Funciones
def abrirMenu(*args):
    cantidadColumnas = int(turtle.numinput("Menu", "Ingrese una cantidad de columnas (1-25)", minval=1, maxval=25))
    cantidadFilas = int(turtle.numinput("Menu", "Ingrese una cantidad de filas (1-18)", minval=1, maxval=18))
    maxBombas = round(cantidadColumnas*cantidadFilas / 2)
    cantidadBombas = int(turtle.numinput("Menu", prompt="Ingrese una cantidad de bombas (1-" + str(maxBombas) + ")", minval=1, maxval=maxBombas))
    
    return [cantidadColumnas, cantidadFilas, cantidadBombas]

def ubicarBombas():
    global columnas

    ubicacionBombas = []
    for i in range(dimensiones[2]):
        while True:
            bomba = [random.randint(0, dimensiones[0]-1), random.randint(0, dimensiones[1]-1)] # Se le agrega un '-1' para que no se vaya de rango
            if bomba not in ubicacionBombas:
                break
        ubicacionBombas.append(bomba)
        columnas[bomba[0]][bomba[1]].estado = -1
    
    return ubicacionBombas

def crearCuadrados(posicion, valor, index):
    cuadrado = Cuadrado(valor, index)
    cuadrado.speed(0)
    cuadrado.shape(imagenDelante)
    cuadrado.penup()
    cuadrado.goto(posicion[0], posicion[1])
    return cuadrado

def redondear(numero):
    return int(numero)

def calcularPosicionCuadrados(index):
    print('El index es: ', index)
    x = dimensionesCuadrado*index[0]-redondear(dimensiones[0]/2)*dimensionesCuadrado#+dimensionesCuadrado
    y = dimensionesCuadrado*index[1]-redondear(dimensiones[1]/2)*dimensionesCuadrado-dimensionesCuadrado
    print([x,y])
    return [x,y]

def crearTablero(dimensiones):
    columnas = []
    for columna in range(dimensiones[0]):
        filas = []
        for fila in range(dimensiones[1]):
            index = [columna, fila]
            cuadrado = crearCuadrados(calcularPosicionCuadrados([columna,fila]), 0, index)
            cuadrado.onclick(cuadrado.clickIzquierdo, 1)
            filas.append(cuadrado)
        columnas.append(filas)
    return columnas

#------------------------------------------------------------------------------#
# Listeners


#------------------------------------------------------------------------------#
# Main Loop
dimensiones = abrirMenu()
columnas = crearTablero(dimensiones)
ubicarBombas()


print(ubicarBombas())

while True:
    ventanaPrincipal.update()
#------------------------------------------------------------------------------#



'''
class Cuadrado(turtle.Turtle):
    
    def __init__(self, prueba):
        turtle.Turtle.__init__(self)
        self.__posicion = prueba


    def prueba(self, *args):
        print("Pito")
    
    def cambiarColor(self, *args):
        self.color("green")
        print("La posicion es: ", self.__posicion)

    def clickDerecho(self, *args):
        self.shape(imagenDos)

def crearCuadrados(posicion, rango):
    cuadrado = Cuadrado(rango)
    #cuadrado.mover(rango)
    cuadrado.color('blue')
    cuadrado.speed(0)
    cuadrado.shape('square')
    cuadrado.penup()
    cuadrado.goto(posicion[0], posicion[1])
    print('El tipo es: ', type(cuadrado))
    return cuadrado

cantidadColumnas = range(10)
cuadrados = []

for i in cantidadColumnas:
    print(i)
    cuadrados.append(crearCuadrados([i*25, 50], i))



menu = turtle.Turtle()
menu.color('yellow')
menu.speed(0)
menu.shapesize(stretch_wid=2, stretch_len=2)
menu.shape(imagenUno)
menu.penup()
menu.goto(-25,50)

def accionMenu(*args):
    print("Hiciste click en el menu")

menu.onclick(accionMenu,1)

for i in cuadrados:
    i.onclick(i.cambiarColor, 1)
    i.onclick(i.clickDerecho, 3)
'''

