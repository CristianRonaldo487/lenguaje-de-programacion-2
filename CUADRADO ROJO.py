from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def inicializar():
    """Configura el entorno OpenGL"""
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Fondo negro
    glPointSize(2)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0)  # Vista ortográfica 2D

def dibujar_cuadrado():
    """Dibuja un cuadrado rojo"""
    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(1.0, 0.0, 0.0)  # Color rojo (R=1, G=0, B=0)
    glBegin(GL_QUADS)
    # Cuatro vértices del cuadrado
    glVertex2f(-0.5, -0.5)  # Inferior izquierdo
    glVertex2f( 0.5, -0.5)  # Inferior derecho
    glVertex2f( 0.5,  0.5)  # Superior derecho
    glVertex2f(-0.5,  0.5)  # Superior izquierdo
    glEnd()

    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Cuadrado rojo en OpenGL")
    inicializar()
    glutDisplayFunc(dibujar_cuadrado)
    glutMainLoop()

if __name__ == "__main__":
    main()
