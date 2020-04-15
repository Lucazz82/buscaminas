import turtle
import random
import time
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

imagenReiniciar = './imagenes/reiniciar.gif'
ventanaPrincipal.addshape(imagenReiniciar)

imagenGanar = "./imagenes/trophy.gif"
ventanaPrincipal.addshape(imagenGanar)

imagenPerder = "./imagenes/wasted.gif"
ventanaPrincipal.addshape(imagenPerder)

imagenBombaTocada = "./imagenes/boom.gif"
ventanaPrincipal.addshape(imagenBombaTocada)

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

    def reiniciar(self):
        for columna in self.tablero:
            for fila in columna:
                fila.hideturtle()
                fila.clear()
        self.tablero = []
        self.crearTablero()
    pass


class Menu():
    def __init__(self):
        self.cantidadColumnas = 0
        self.cantidadFilas = 0
        self.__maxbombas = 0
        self.cantidadBombas = 0
        self.reiniciar()

    def modificarColumnas(self):
        return int(turtle.numinput("Menu", "Ingrese una cantidad de columnas (1-25)", minval=1, maxval=25))

    def modificarFilas(self):
        return int(turtle.numinput("Menu", "Ingrese una cantidad de filas (1-18)", minval=1, maxval=18))

    def calcularMaximoBombas(self):
        return round(self.cantidadColumnas*self.cantidadFilas / 2)

    def modificarBombas(self):
        return int(turtle.numinput("Menu", prompt="Ingrese una cantidad de bombas (1-" + str(self.__maxbombas) + ")", minval=1, maxval=self.__maxbombas))

    def reiniciar(self):
        self.cantidadColumnas = self.modificarColumnas()
        self.cantidadFilas = self.modificarFilas()
        self.__maxbombas = self.calcularMaximoBombas()
        self.cantidadBombas = self.modificarBombas()

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
    
    def reiniciar(self):
        self.__ultimoClick = []

    pass

class Banderas():
    def __init__(self):
        self.__ubicacion = []
    
    def agregar(self,valor):
        self.__ubicacion.append(valor)

    def borrar(self, valor):
        self.__ubicacion.remove(valor)

    def cantidad(self):
        return len(self.__ubicacion)

    def comprobar(self):
        print("Prueba")
        array = []
        for bomba in bombas.visualizar():
            array.append(bomba in self.__ubicacion)
        
        return not False in array

    def reiniciar(self):
        self.__ubicacion = []

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

    def reiniciar(self):
        self.__ubicacion = []
        
    pass

class Tiempo():
    def __init____(self):
        self.__tiempo_utc
        self.temporizador
        self.parar
        self.reiniciar()
        
    
    def reiniciar(self):
        self.__tiempo_utc = time.time()
        self.temporizador = 0
        self.parar = False

    def actualizar(self):
        self.temporizador = int(time.time() - self.__tiempo_utc)

    def tiempo_temporizador(self):
        self.actualizar()
        segundos = self.temporizador
        if segundos < 60:
            if segundos < 10:
                return "00:0{}".format(segundos)
            else:
                return "00:{}".format(segundos)
        elif 60 <= segundos < 3600:
            minutos = int(segundos/60)
            n_segundos = segundos - minutos*60
            if minutos < 10:
                minutos = "0{}".format(minutos)
            if n_segundos < 10:
                n_segundos = "0{}".format(n_segundos)
            return "{}:{}".format(minutos, n_segundos)
        else:
            horas = int(segundos/3600)
            minutos = int(segundos - horas*3600)
            n_segundos = segundos - horas*3600 - minutos*60

            if horas < 10:
                horas = "0{}".format(horas)
            if minutos < 10:
                minutos = "0{}".format(minutos)
            if n_segundos < 10:
                n_segundos = "0{}".format(n_segundos)
        return "{}:{}:{}".format(horas, minutos, n_segundos)

class Trofeo():
    def __init__(self, imagen):
        self.objeto = 0
        self.imagen = imagen

    def visualizar(self):
        self.bloquear()
        self.pararReloj()
        ganar = turtle.Turtle()
        ganar.speed(0)
        ganar.shape(self.imagen)
        ganar.penup()
        ganar.goto(0, 0)
        self.objeto = ganar

    def ocultar(self):
        if self.objeto:
            self.objeto.hideturtle()
            self.objeto.clear()

    def bloquear(self):
        for columnas in tablero.tablero:
            for fila in columnas:
                fila.descubierto = True

    def pararReloj(self):
        tiempo.parar = True

class Perder(Trofeo):
    def perder(self, index):
        self.visualizar()
        for bomba in bombas.visualizar():
            bomba = list(bomba)
            if bomba != index:
                tablero.tablero[bomba[0]][bomba[1]].shape(imagenBomba)
            else:
                tablero.tablero[bomba[0]][bomba[1]].shape(imagenBombaTocada)
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
                    # print("Perdiste porque tocaste una bomba")
                    perder.perder(self.index)
                elif not self.numero:
                    self.cambiarImagen()
                    self.clickCeldaVacia()
                    arrayCeldaVacia.limpiar()
                elif self.numero:           # Esto es readundante, habria que fijarse si sacarlo afecta a la funcionalidad
                    self.cambiarImagen()
        
    def clickDerecho(self, *agrs):
        if not self.descubierto:
            if not self.bandera:
                banderas.agregar(self.index)
                self.shape(imagenBandera)
                self.bandera = True
            else:
                banderas.borrar(self.index)
                self.shape(imagenDelante)
                self.bandera = False

            cantidad_banderas.clear()
            cantidad_banderas.write("Banderas: {}/{}".format(banderas.cantidad(), menu.cantidadBombas), align="center", font=("courier", 12, "normal"))
            if banderas.comprobar():
                trofeo.visualizar()
                


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

                


    pass
#------------------------------------------------------------------------------#
# Funciones
def funciones_reiniciar(*agrs):
        banderas.reiniciar()
        bombas.reiniciar()
        menu.reiniciar()
        tablero.reiniciar()
        tiempo.reiniciar()
        ultimoClick.reiniciar()
        bombas.ubicar()
        tablero.ubicarNumeros()
        cantidad_banderas.clear()
        cantidad_banderas.write("Banderas: {}/{}".format(banderas.cantidad(), menu.cantidadBombas), align="center", font=("courier", 12, "normal"))
        cantidad_bombas.clear()
        cantidad_bombas.write("Bombas: {}".format(menu.cantidadBombas), align="center", font=("courier", 12, "normal"))
        trofeo.ocultar()
        perder.ocultar()



#------------------------------------------------------------------------------#
# Listeners


#------------------------------------------------------------------------------#
# Main Loop
bombas = Bombas()
banderas = Banderas()
arrayCeldaVacia = celdaVacia()
ultimoClick = ultimoClick() # ver si es util sino sacarlo a la mierda porque no hace nada
menu = Menu()
tablero = Tablero()
tablero.crearTablero()
bombas.ubicar()
tablero.ubicarNumeros()
trofeo = Trofeo(imagenGanar)
perder = Perder(imagenPerder)


# Temporizador
tiempo = Tiempo()
tiempo.reiniciar()
temporizador = turtle.Turtle()
temporizador.speed(0)
temporizador.color("white")
temporizador.penup()
temporizador.hideturtle()
temporizador.goto(0, 220)

# Cantidad de Bombas
cantidad_bombas = turtle.Turtle()
cantidad_bombas.speed(0)
cantidad_bombas.color("white")
cantidad_bombas.penup()
cantidad_bombas.hideturtle()
cantidad_bombas.goto(300, 250)
cantidad_bombas.write("Bombas: {}".format(menu.cantidadBombas), align="center", font=("courier", 12, "normal"))

# Cantidad de Banderas
cantidad_banderas = turtle.Turtle()
cantidad_banderas.speed(0)
cantidad_banderas.color("white")
cantidad_banderas.penup()
cantidad_banderas.hideturtle()
cantidad_banderas.goto(300, 220)
cantidad_banderas.write("Banderas: {}/{}".format(banderas.cantidad(), menu.cantidadBombas), align="center", font=("courier", 12, "normal"))

# Boton Reiniciar
reiniciar = turtle.Turtle()
reiniciar.speed(0)
reiniciar.shape(imagenReiniciar)
reiniciar.penup()
reiniciar.onclick(funciones_reiniciar, 1)
reiniciar.goto(-350,250)


while True:
    ventanaPrincipal.update()
    if not tiempo.parar:
        temporizador.clear()
        temporizador.write(tiempo.tiempo_temporizador(), align="center", font=("courier", 24, "normal"))
#------------------------------------------------------------------------------#
