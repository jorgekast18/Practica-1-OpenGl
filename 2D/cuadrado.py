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
#2.1.1
#Programa que genera un cuadrado de L = 0.7, centrado en el origen
#Como el cuadro esta centrado en el origen, entonces del origen a la izquierda habra 0.35 y
#del origen a la derecha habra tambien 0.35, para que la suma nos de 0.7


def initGL(width, height):
	glClearColor(135, 135, 135, 0)
	glMatrixMode(GL_PROJECTION)
	glColor3f(0,0,0)

#Funcion que genera el cuadrado con lado L y centrado en el origen
def dibujarCuadrado():
	glClear(GL_COLOR_BUFFER_BIT)

	glBegin(GL_QUADS)
	glVertex2f(-0.35, 0.35)
	glVertex2f(0.35, 0.35)
	glVertex2f(0.35, -0.35)
	glVertex2f(-0.35, -0.35)
	glEnd()
	glFlush()
	#glutSwapBuffers();

#Funcion que captura las teclas presionadas y genera un evento
def keyPressed(*args):
	key = args[0]
	if key == "r" or key =="R":
		glColor3f(1.0, 0.0, 0.0)
	elif key == "g" or key == "G":
		glColor3f(0.0, 1.0, 0.0)
	elif key ==	"b" or key == "B":
		glColor3f(0.0, 0.0, 1.0)

#Funcion que me imprime la matriz actual
def imprimirMatriz():
	matriz = glGetFloatv(GL_PROJECTION_MATRIX)
	print matriz

def mouseEvent(botonMouse, estadoMouse, x, y):
	if botonMouse == GLUT_LEFT_BUTTON and estadoMouse == GLUT_DOWN: #Si se clickeo con el boton izquierdo del mouse Y ESTE ESTA PRESIONADO
		glColor3f(random(), random(), random())

def main():
	global window
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
	glutInitWindowSize(500,500)
	glutInitWindowPosition(200,200)

	#creando la ventana
	window = glutCreateWindow("Taller1 - Cuadrado")
	glutKeyboardFunc(keyPressed)
	glutMouseFunc(mouseEvent)
	glutDisplayFunc(dibujarCuadrado)
	glutIdleFunc(dibujarCuadrado)
	imprimirMatriz()
	initGL(500,500)
	glutMainLoop()

if __name__ == "__main__":
	main()
