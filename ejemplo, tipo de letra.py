from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np

def f(x):
    return (x ** 2) 

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # --- Ejes X e Y ---
    glColor3f(0.6, 0.6, 0.6)
    glBegin(GL_LINES)
    # Eje X
    glVertex3f(-5, 0, 0)
    glVertex3f(5, 0, 0)
    # Eje Y
    glVertex3f(0, -5, 0)
    glVertex3f(0, 5, 0)
    glEnd()

    # --- Números en los ejes ---
    glColor3f(1, 1, 1)
    for i in range(-4, 5):
        if i != 0:
            # Eje X
            glRasterPos3f(i - 0.1, -0.3, 0)
            for ch in str(i):
                glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ord(ch))
            # Eje Y
            glRasterPos3f(0.2, i - 0.1, 0)
            for ch in str(i):
                glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ord(ch))

    # --- Parábola ---
    glColor3f(1, 1, 0)  # amarillo
    glLineWidth(1)  # línea delgada
    glBegin(GL_LINE_STRIP)

    x_vals = np.linspace(-4, 4, 200)
    for x in x_vals:
        y = f(x)
        glVertex3f(x, y, 0)

    glEnd()

    glFlush()

def init():
    glClearColor(0, 0, 0, 1)  # fondo negro
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-5, 5, -5, 5, -5, 5)
    glMatrixMode(GL_MODELVIEW)

# --- Ventana GLUT ---
glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(600, 600)
glutCreateWindow(b"Graficadora PyOpenGL - Parabola con Ejes Numerados")
init()
glutDisplayFunc(display)
glutMainLoop()
