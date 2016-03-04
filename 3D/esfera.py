from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from random import random

# ====================================================================
#						      FUNCIONES
#
#
# ====================================================================
# 								DATOS
# Nombre : Jorge A. Castanio, Sebastian Velasquez, Oscar Eduardo Ramirez
# Codigo : 1153641, -----, -----
# Plan: Ingenieria de Sistemas
# Profesor: ----------
# Taller Numero 1 de Computacion Grafica
#=====================================================================
#3.1.3
#Programa que genera una esfera con radio r = 0,9 de color rosa.

def initGL(width, height):
	glClearColor(0.529, 0.529, 0.529, 0.0) #Establecemos color de fonde de ventana
	glMatrixMode(GL_PROJECTION) #Definimos matriz de proyeccion
	glColor3f(0.7, 0.5, 0.5) #Establecemos el color de inicio (en este caso rosa)

def dibujarEsfera():
	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT) #Borramos buffer de color y de profundidad

	glLoadIdentity () # Borramos la matriz (cada vez que se dibuje cargamos la matriz identidad)

# -----Transformaciones de vista, aca vamos a empezar a darle un poco de estilo a nuestra escena----
	gluLookAt(0.3, 0.3, 0.3, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)# punto de vista de la figura, los parametros son --> gluLookAt( GLdouble eyex, GLdouble eyey, GLdouble eyez,GLdouble centerx, GLdouble centery, GLdouble centerz,GLdouble upx, GLdouble upy, GLdouble upz )
	glScalef(1.0, 2.0, 1.0)# Define el aspecto de la figura, los parametros son -->(anchoIzquierda, Alto, AnchoDerecha)
	glutSolidSphere(0.45, 16, 16) # Genera una esfera solida, los parametros son --> (double radius, int slices, int stacks)
	glFlush()

def keyPressed(*args):
	key = args[0]
	if key == "r" or key =="R":
		glColor3f(0.5, 0.0, 0.0)
	elif key == "g" or key == "G":
		glColor3f(0.0, 0.5, 0.0)
	elif key ==	"b" or key == "B":
		glColor3f(0.0, 0.0, 0.5)

def mouseEvent(botonMouse, estadoMouse, x, y):
	if botonMouse == GLUT_LEFT_BUTTON and estadoMouse == GLUT_DOWN: #Si se clickeo con el boton izquierdo del mouse Y ESTE ESTA PRESIONADO
		glColor3f(random(), random(), random())

# Funcion que me imprime la matriz actual
def imprimirMatriz():
	matriz = glGetFloatv(GL_PROJECTION_MATRIX)
	print matriz

def main():
	global window # Variable global para la ventana
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB|GLUT_DEPTH) #M ostramos buffer simple, de color y profundidad
	glutInitWindowSize(500,500) # Establecemos tamanio de ventana
	glutInitWindowPosition(200,200)
	glEnable(GL_DEPTH_BUFFER)

	# Creando la ventana
	window = glutCreateWindow("Taller1 - Esfera") # Creamos ventana y le damos un nombre
	glutKeyboardFunc(keyPressed) # Evento tecla
	glutMouseFunc(mouseEvent) # Evento raton
	glutDisplayFunc(dibujarEsfera)
	glutIdleFunc(dibujarEsfera)
	imprimirMatriz()
	initGL(500,500) # Llamamos a Init
	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT) #Borramos el bufer de profuncididad e inicial
	glutMainLoop() #Ciclo para que la ventana no desaparezca

if __name__ == "__main__":
	main()
