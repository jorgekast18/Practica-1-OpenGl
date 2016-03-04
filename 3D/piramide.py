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
#3.1.2
#Programa que genera Genere una esfera con radio r = 0;5 de color azul.

def initGL(width, height):
	glClearColor(0.529, 0.529, 0.529, 0.0)
	glMatrixMode(GL_PROJECTION)
	glColor3f(0.8, 0.4, 0.0)

def dibujarPiramide():
	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
	glLoadIdentity ()

# -----Transformaciones de vista, se le da un estilo a la escena----
    #punto de vista
	gluLookAt (0.2, 0.2 ,0.4, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
	glScalef (1.0, 2.0, 1.0) # Define el aspecto de la piramide
	glutWireCone (0.4,0.3, 3, 4) # Define la piramide
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
	if botonMouse == GLUT_LEFT_BUTTON and estadoMouse == GLUT_DOWN:
		glColor3f(random(), random(), random())

#Funcion que me imprime la matriz actual
def imprimirMatriz():
	matriz = glGetFloatv(GL_PROJECTION_MATRIX)
	print matriz

def main():
	global window
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB|GLUT_DEPTH)
	glutInitWindowSize(500,500)
	glutInitWindowPosition(200,200)
	glEnable(GL_DEPTH_BUFFER)

	window = glutCreateWindow("Taller1 - Piramide")
	glutKeyboardFunc(keyPressed)
	glutMouseFunc(mouseEvent)
	glutDisplayFunc(dibujarPiramide)
	glutIdleFunc(dibujarPiramide)
	imprimirMatriz()
	initGL(500,500)
	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
	glutMainLoop()

if __name__ == "__main__":
	main()