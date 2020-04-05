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

#------------------------------------------------------------------------------#
# Clases
class Tablero():
    def __init__(self):
        self.tablero = []
    
    def crearCuadrados(self, posicion, valor, index):
        cuadrado = Cuadrado(valor, index)
        cuadrado.speed(0)
        cuadrado.shape(imagenDelante)
        cuadrado.penup()
        cuadrado.goto(posicion[0], posicion[1])
        return cuadrado

    def crearTablero(self):
        for columna in range(menu.cantidadColumnas):
            #print('columna')
            filas = []
            for fila in range(menu.cantidadFilas):
                index = [columna, fila]
                cuadrado = self.crearCuadrados(self.calcularPosicionCuadrados([columna,fila]), 0, index)
                cuadrado.onclick(cuadrado.clickIzquierdo, 1)
                cuadrado.onclick(cuadrado.clickDerecho, 3)
                filas.append(cuadrado)
            self.tablero.append(filas)

    def redondear(self, numero):
        return int(numero)

    def calcularPosicionCuadrados(self, index):
        x = dimensionesCuadrado*index[0]-self.redondear(menu.cantidadColumnas/2)*dimensionesCuadrado
        y = dimensionesCuadrado*index[1]-self.redondear(menu.cantidadFilas/2)*dimensionesCuadrado-dimensionesCuadrado
        return [x,y]

    def ubicarNumeros(self):
        for columna in self.tablero:
            for fila in columna:
                fila.contarBombas()
    pass


class Menu():
    def __init__(self):
        self.cantidadColumnas = self.modificarColumnas()
        self.cantidadFilas = self.modificarFilas()
        self.__maxbombas = self.calcularMaximoBombas()
        self.cantidadBombas = self.modificarBombas()

    def modificarColumnas(self):
        return int(turtle.numinput("Menu", "Ingrese una cantidad de columnas (1-25)", minval=1, maxval=25))

    def modificarFilas(self):
        return int(turtle.numinput("Menu", "Ingrese una cantidad de filas (1-18)", minval=1, maxval=18))

    def calcularMaximoBombas(self):
        return round(self.cantidadColumnas*self.cantidadFilas / 2)

    def modificarBombas(self):
        return int(turtle.numinput("Menu", prompt="Ingrese una cantidad de bombas (1-" + str(self.__maxbombas) + ")", minval=1, maxval=self.__maxbombas))

    def prueba(self):
        print(self.cantidadBombas)
        print(self.cantidadColumnas)
        print(self.cantidadFilas)


class celdaVacia():
    def __init__(self):
        self.__celda = []

    def limpiar(self):
        self.__celda = []

    def agregar(self, valor):
        self.__celda.append(valor)

    def comprobar(self, valor):
        return valor in self.__celda
        
    pass

class ultimoClick():
    def __init__(self):
        self.__ultimoClick = []
    
    def actualizar(self, valor):
        self.__ultimoClick = valor

    pass

class Banderas():
    def __init__(self):
        self.__ubicacion = []
    
    def agregar(self,valor):
        self.__ubicacion.append(valor)

    def borrar(self, valor):
        self.__ubicacion.remove(valor)

    def comprobar(self):
        print("Prueba")
        array = []
        for bomba in bombas.visualizar():
            array.append(bomba in self.__ubicacion)
        
        return not False in array

    pass

class Bombas():
    def __init__(self):
        self.__ubicacion = []

    def agregar(self, valor):
        self.__ubicacion.append(valor)

    def comprobar(self, valor):
        return valor in self.__ubicacion

    def visualizar(self):
        return self.__ubicacion

    def ubicar(self):

        for i in range(menu.cantidadBombas):
            while True:
                bomba = [random.randint(0, menu.cantidadColumnas-1), random.randint(0, menu.cantidadFilas-1)] # Se le agrega un '-1' para que no se vaya de rango
                if not self.comprobar(bomba):
                    break
            self.agregar(bomba)
            tablero.tablero[bomba[0]][bomba[1]].bomba = True

    pass

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
        
        if menu.cantidadColumnas > self.index[0]+1 >= 0 and menu.cantidadFilas > self.index[1]-1 >=0:
            self.alrededores.append(tablero.tablero[self.index[0]+1][self.index[1]-1])
        
        if menu.cantidadColumnas > self.index[0]+1 >= 0 and menu.cantidadFilas > self.index[1] >=0:
            self.alrededores.append(tablero.tablero[self.index[0]+1][self.index[1]])
        
        if menu.cantidadColumnas > self.index[0]+1 >= 0 and menu.cantidadFilas > self.index[1]+1 >=0:
            self.alrededores.append(tablero.tablero[self.index[0]+1][self.index[1]+1])
        
        if menu.cantidadColumnas > self.index[0] >= 0 and menu.cantidadFilas > self.index[1]-1 >=0:
            self.alrededores.append(tablero.tablero[self.index[0]][self.index[1]-1])
        
        if menu.cantidadColumnas > self.index[0] >= 0 and menu.cantidadFilas > self.index[1]+1 >=0:
            self.alrededores.append(tablero.tablero[self.index[0]][self.index[1]+1])
        
        if menu.cantidadColumnas > self.index[0]-1 >= 0 and menu.cantidadFilas > self.index[1]-1 >=0:
            self.alrededores.append(tablero.tablero[self.index[0]-1][self.index[1]-1])

        if menu.cantidadColumnas > self.index[0]-1 >= 0 and menu.cantidadFilas > self.index[1] >=0:
            self.alrededores.append(tablero.tablero[self.index[0]-1][self.index[1]])
        
        if menu.cantidadColumnas > self.index[0]-1 >= 0 and menu.cantidadFilas > self.index[1]+1 >=0:
            self.alrededores.append(tablero.tablero[self.index[0]-1][self.index[1]+1])

    def clickIzquierdo(self, *args):

        if not self.descubierto:
            ultimoClick.actualizar(self.index)
            if self.bandera:
                self.clickDerecho()
            else:
                if self.bomba:
                    print("Perdiste porque tocaste una bomba")
                elif not self.numero:
                    self.cambiarImagen()
                    self.clickCeldaVacia()
                elif self.numero:           # Esto es readundante, habria que fijarse si sacarlo afecta a la funcionalidad
                    self.cambiarImagen()
        
    def clickDerecho(self, *agrs):
        if not self.bandera:
            banderas.agregar(self.index)
            self.shape(imagenBandera)
            self.bandera = True
        else:
            banderas.borrar(self.index)
            self.shape(imagenDelante)
            self.bandera = False
        
        if banderas.comprobar():
            print("Ganaste")


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
            if menu.cantidadColumnas > celda.index[0] >= 0 and menu.cantidadFilas > celda.index[1] >= 0:
                if celda.bomba:
                    cantidadBombas += 1
        if cantidadBombas > 0:
            self.numero = True
        self.estado = cantidadBombas
        

    def clickCeldaVacia(self):
        for celda in self.alrededores:
            if not arrayCeldaVacia.comprobar(celda):
                arrayCeldaVacia.agregar(celda)
                celda.cambiarImagen()
                if not celda.numero:
                    celda.clickCeldaVacia()
        
        

    # Funcion Provicional
    def mostrarBombas(self):
        if self.bomba:
            self.shape(imagenBomba)
                


    pass
#------------------------------------------------------------------------------#
# Funciones
'''
def abrirMenu(*args):
    cantidadColumnas = int(turtle.numinput("Menu", "Ingrese una cantidad de columnas (1-25)", minval=1, maxval=25))
    cantidadFilas = int(turtle.numinput("Menu", "Ingrese una cantidad de filas (1-18)", minval=1, maxval=18))
    maxBombas = round(cantidadColumnas*cantidadFilas / 2)
    cantidadBombas = int(turtle.numinput("Menu", prompt="Ingrese una cantidad de bombas (1-" + str(maxBombas) + ")", minval=1, maxval=maxBombas))
    
    return [cantidadColumnas, cantidadFilas, cantidadBombas]
'''
'''
def ubicarBombas():
    global columnas

    
    for i in range(dimensiones[2]):
        while True:
            bomba = [random.randint(0, dimensiones[0]-1), random.randint(0, dimensiones[1]-1)] # Se le agrega un '-1' para que no se vaya de rango
            if bombas.comprobar(bomba):
                break
        bombas.agregar(bomba)
        columnas[bomba[0]][bomba[1]].bomba = True
'''
'''
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
'''
'''
def ubicarNumeros():
    for columna in columnas:
        for fila in columna:
            fila.contarBombas()
'''

#------------------------------------------------------------------------------#
# Listeners


#------------------------------------------------------------------------------#
# Main Loop
bombas = Bombas()
banderas = Banderas()
arrayCeldaVacia = celdaVacia()
ultimoClick = ultimoClick()
menu = Menu()
tablero = Tablero()
tablero.crearTablero()
bombas.ubicar()
tablero.ubicarNumeros()


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

