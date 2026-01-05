from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def inicializar():
    """Configura el entorno OpenGL"""
    glClearColor(0.0, 0.0, 0.0, 1.0) # Fondo gris oscuro
    glPointSize(2)                  # Tamaño de los puntos
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-10,10,-4,4,1,1) # Vista ortográfica 2D

def dibujar_triangulo():
    """Dibuja 3 puntos formando un triángulo"""
    glClear(GL_COLOR_BUFFER_BIT)

    #glColor3f(0.0, 1.0, 0.0) # Color amarillo
    glBegin(GL_LINE_STRIP)

    # Tres vértices del triángulo
    glVertex2f(0.-2, 0.-3)    # Vértice superior
    glVertex2f(-0.-2, 0.3)  # Vértice inferior izquierdo
    
    glEnd()
    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Triangulo de puntos en OpenGL")
    inicializar()
    glutDisplayFunc(dibujar_triangulo)
    glutMainLoop()

if __name__ == "__main__":
    main()

