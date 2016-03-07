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
#3.1.4
#Programa que genera una figura irregular.

def initGL(width, height):
	glClearColor(0.529, 0.529, 0.529, 0.0)
	glMatrixMode(GL_PROJECTION)
	glColor3f(0.5, 0.7, 0.5)

def dibujarIrregular():
	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
	glLoadIdentity ()

# -----Transformaciones de vista, se le da un estilo a la escena
    #punto de vista
	gluLookAt(0.5,0.2,0.5, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
	glScalef (0.5, 0.5, 0.5)

	glBegin(GL_QUADS)
	glColor3f(0.0, 0.0, 0.5)
	glVertex3f( 0.0,  1.0, 0.0)

	glColor3f(0.5, 0.0, 0.0)
	glVertex3f(-1.0, -1.0, 0.0)

	glColor3f(0.0, 0.5, 0.0)
	glVertex3f( 1.0, -1.0, 0.0)

	glColor3f(0.5, 0.5, 0.0)
	glVertex3f( 1.0, 1.0, 1.0)

	glEnd()

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

# Funcion que me imprime la matriz actual
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

	window = glutCreateWindow("Taller1 - Figura irregular")
	glutKeyboardFunc(keyPressed)
	glutMouseFunc(mouseEvent)
	glutDisplayFunc(dibujarIrregular)
	glutIdleFunc(dibujarIrregular)
	imprimirMatriz()
	initGL(500,500)
	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
	glutMainLoop()

if __name__ == "__main__":
	main()
