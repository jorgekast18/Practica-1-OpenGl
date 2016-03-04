import sys
from OpenGL.GLUT import *
from OpenGL.GL import *
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
#3.1.1
#Programa que genera un cubo centrado en el origen con l = 0.8 de color cyan.

def init():
   glClearColor(135, 135, 135, 0)
   glColor3f(0.0, 1.0, 1.0)

def dibujarCubo():
   glClear (GL_COLOR_BUFFER_BIT)
   glLoadIdentity ()

# -----Transformaciones de vista, se le da un estilo a la escena
   #punto de vista
   gluLookAt(3.0, 3.0, 6.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
   glScalef(2.0, 2.0, 2.0)
   glutSolidCube(0.8)
   glFlush()

def reshape (w, h):
   glViewport (0, 0, w, h)
   glMatrixMode (GL_PROJECTION)
   glLoadIdentity ()
   glFrustum (-1.0, 1.0, -1.0, 1.0, 1.5, 20.0)
   glMatrixMode (GL_MODELVIEW)

def keyPressed(*args):
  key = args[0]
  if key == "r" or key =="R":
    glColor3f(0.5, 0.0, 0.0)
  elif key == "g" or key == "G":
    glColor3f(0.0, 0.5, 0.0)
  elif key == "b" or key == "B":
    glColor3f(0.0, 0.0, 0.5)

def mouseEvent(botonMouse, estadoMouse, x, y):
    if botonMouse == GLUT_LEFT_BUTTON and estadoMouse == GLUT_DOWN:
        glColor3f(random(), random(), random())

#Funcion que me imprime la matriz actual
def imprimirMatriz():
  matriz = glGetFloatv(GL_PROJECTION_MATRIX)
  print matriz

def main():
  glutInit(sys.argv)
  glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB)
  glutInitWindowSize (500, 500)
  glutInitWindowPosition (100, 100)
  glutCreateWindow ("Taller1 - Cubo")

  init ()
  glutDisplayFunc(dibujarCubo)
  glutIdleFunc(dibujarCubo)
  glutKeyboardFunc(keyPressed)
  glutMouseFunc(mouseEvent)
  glutReshapeFunc(reshape)
  imprimirMatriz()
  glutMainLoop()

if __name__ == '__main__':
    main()