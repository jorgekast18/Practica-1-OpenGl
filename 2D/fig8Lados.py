from OpenGL.GL import *
from OpenGL.GLUT import *
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
#2.1.4
#Programa que genera una figura con 8 lados

def initGL(width, height):
	glClearColor(135, 135, 135, 0)
	glMatrixMode(GL_PROJECTION)
	glColor3f(0.0, 0.0, 1.0)

def dibujarOctagono():
	glClear(GL_COLOR_BUFFER_BIT)

	glBegin(GL_POLYGON)
	glVertex2f(0.8, 0.2)
	glVertex2f(0.4, 0.4)
	glVertex2f(-0.4, 0.4)
	glVertex2f(-0.8, 0.2)
	glVertex2f(-0.8, -0.2)
	glVertex2f(-0.4, -0.4)
	glVertex2f(0.4, -0.4)
	glVertex2f(0.8, -0.2)
	glEnd()
	glFlush()
	#glutSwapBuffers();

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
	window = glutCreateWindow("Taller1 - Figura de 8 lados")

	glutDisplayFunc(dibujarOctagono)
	glutIdleFunc(dibujarOctagono)
	imprimirMatriz()
	glutKeyboardFunc(keyPressed)
	glutMouseFunc(mouseEvent)
	initGL(500,500)
	glutMainLoop()

if __name__ == "__main__":
	main()
