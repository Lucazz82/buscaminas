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
        self.estado = 0 # 0 = vacio / 1-8 = ese numero
        self.valorOculto = valor
        self.index = index
        self.bomba = False
        self.descubierto = False
        self.bandera = False
        self.numero = False
        self.alrededores = []

    def definirAlrededores(self):
        if dimensiones[0] > self.index[0]+1 >= 0 and dimensiones[1] > self.index[1]-1 >=0:
            self.alrededores.append(columnas[self.index[0]+1][self.index[1]-1])
        
        if dimensiones[0] > self.index[0]+1 >= 0 and dimensiones[1] > self.index[1] >=0:
            self.alrededores.append(columnas[self.index[0]+1][self.index[1]])
        
        if dimensiones[0] > self.index[0]+1 >= 0 and dimensiones[1] > self.index[1]+1 >=0:
            self.alrededores.append(columnas[self.index[0]+1][self.index[1]+1])

        if dimensiones[0] > self.index[0] >= 0 and dimensiones[1] > self.index[1]-1 >=0:
            self.alrededores.append(columnas[self.index[0]][self.index[1]-1])

        if dimensiones[0] > self.index[0] >= 0 and dimensiones[1] > self.index[1]+1 >=0:
            self.alrededores.append(columnas[self.index[0]][self.index[1]+1])

        if dimensiones[0] > self.index[0]-1 >= 0 and dimensiones[1] > self.index[1]-1 >=0:
            self.alrededores.append(columnas[self.index[0]-1][self.index[1]-1])

        if dimensiones[0] > self.index[0]-1 >= 0 and dimensiones[1] > self.index[1] >=0:
            self.alrededores.append(columnas[self.index[0]-1][self.index[1]])

        if dimensiones[0] > self.index[0]-1 >= 0 and dimensiones[1] > self.index[1]+1 >=0:
            self.alrededores.append(columnas[self.index[0]-1][self.index[1]+1])


    def clickIzquierdo(self, *args):
        self.actualizarUltimoClick()

        if not self.descubierto:
            if self.bomba:
                print("Perdiste porque tocaste una bomba")
            elif self.estado == 0:
                self.cambiarImagen()
                self.clickCeldaVacia(0)
            else:
                self.cambiarImagen()
        
    def clickDerecho(self, *agrs):
        if not self.bandera:
            self.shape(imagenBandera)
            self.bandera = True
        else:
            self.shape(imagenDelante)
            self.bandera = False


    def actualizarUltimoClick(self):
        global ultimoClick
        ultimoClick = self.index
        #print(ultimoClick)

    def cambiarImagen(self):
        self.descubierto = True
        
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
        cantidadBombas = 0
        self.definirAlrededores()
        for celda in self.alrededores:
            if dimensiones[0] > celda.index[0] >= 0 and dimensiones[1] > celda.index[1] >= 0:
                if celda.bomba:
                    cantidadBombas += 1
        if cantidadBombas > 0:
            self.numero = True
        self.estado = cantidadBombas
        

    def clickCeldaVacia(self, valor):
        for celda in self.alrededores:
            if not celda.descubierto:
                celda.cambiarImagen()
            if not celda.numero:
                #sinNumero.append(celda)
                celda.clickCeldaVacia(True)
    
    # Funcion Provicional
    def mostrarBombas(self):
        if self.bomba:
            self.shape(imagenBomba)
                


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
        columnas[bomba[0]][bomba[1]].bomba = True
    
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
    #print('El index es: ', index)
    x = dimensionesCuadrado*index[0]-redondear(dimensiones[0]/2)*dimensionesCuadrado#+dimensionesCuadrado
    y = dimensionesCuadrado*index[1]-redondear(dimensiones[1]/2)*dimensionesCuadrado-dimensionesCuadrado
    #print([x,y])
    return [x,y]

def crearTablero(dimensiones):
    columnas = []
    for columna in range(dimensiones[0]):
        filas = []
        for fila in range(dimensiones[1]):
            index = [columna, fila]
            cuadrado = crearCuadrados(calcularPosicionCuadrados([columna,fila]), 0, index)
            cuadrado.onclick(cuadrado.clickIzquierdo, 1)
            cuadrado.onclick(cuadrado.clickDerecho, 3)
            filas.append(cuadrado)
        columnas.append(filas)
    return columnas

def ubicarNumeros():
    for columna in columnas:
        for fila in columna:
            fila.contarBombas()

# Funcion para debuguear
def mostrarBombas():
    for i in columnas:
        for celda in i:
            if celda.bomba:
                celda.mostrarBombas()

def mostrarNumeros():
    for i in columnas:
        for celda in i:
            pass
            #print('El estado de esta celda es: ', celda.estado)

#------------------------------------------------------------------------------#
# Listeners


#------------------------------------------------------------------------------#
# Main Loop
dimensiones = abrirMenu()
columnas = crearTablero(dimensiones)
ubicarBombas()
ubicarNumeros()

mostrarBombas()
mostrarNumeros()

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

