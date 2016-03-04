from OpenGL.GL import *
from OpenGL.GLUT import *
from random import random
from math import sin
from math import cos
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
#2.1.3
#Programa que Genera un circulo con radio r = 1,5 de color negro. EL circulo que se va a generar estara centrado
#en el origen, por lo que del origen hacia la izquierda tendra una distancia de 0.75 igualmente hacia la derecha


def initGL(width, height):
	glClearColor(135, 135, 135, 0)
	glMatrixMode(GL_PROJECTION)
	glColor3f(0.0, 1.0, 0.0)

def dibujarCirculo():
	glClear(GL_COLOR_BUFFER_BIT)
	glBegin(GL_POLYGON)
	for i in range(400):
		x = 0.75*sin(i) #Cordenadas polares x = r*sin(t) donde r = radio/2 (Circunferencia centrada en el origen)
		y = 0.75*cos(i) #Cordenadas polares y = r*cos(t)
		glVertex2f(x, y)
	glEnd()
	glFlush()

def keyPressed(*args):
	key = args[0]
	if key == "r" or key =="R":
		glColor3f(1.0, 0.0, 0.0)
	elif key == "g" or key == "G":
		glColor3f(0.0, 1.0, 0.0)
	elif key ==	"b" or key == "B":
		glColor3f(0.0, 0.0, 1.0)

def mouseEvent(botonMouse, estadoMouse, x, y):
	if botonMouse == GLUT_LEFT_BUTTON and estadoMouse == GLUT_DOWN: #Si se clickeo con el boton izquierdo del mouse Y ESTE ESTA PRESIONADO
		glColor3f(random(), random(), random())

#Funcion que me imprime la matriz actual
def imprimirMatriz():
	matriz = glGetFloatv(GL_PROJECTION_MATRIX)
	print matriz

def main():
	global window
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
	glutInitWindowSize(500,500)
	glutInitWindowPosition(200,200)

	#creando la ventana
	window = glutCreateWindow("Taller1 - Triangulo")

	glutDisplayFunc(dibujarCirculo)
	glutIdleFunc(dibujarCirculo)
	imprimirMatriz()
	glutKeyboardFunc(keyPressed)
	glutMouseFunc(mouseEvent)
	initGL(500,500)
	glutMainLoop()

if __name__ == "__main__":
	main()
