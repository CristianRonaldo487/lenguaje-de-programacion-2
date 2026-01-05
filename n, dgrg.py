from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def inicializar():
    """Configura el entorno OpenGL"""
    glClearColor(1.0, 1.0, 0.0, 1.0)  # Fondo negro
    glPointSize(4)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-10, 10, -4, 4, -1, 1)  # Vista ortográfica 2D

def dibujar_N():
    """Dibuja la letra N con líneas"""
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)  # Color rojo

    glLineWidth(5)
    glBegin(GL_LINES)
    
    # Lado izquierdo de la N
    glVertex2f(-2, -3)
    glVertex2f(-2,  3)

    # Diagonal de la N
    glVertex2f(-2,  3)
    glVertex2f( 2, -3)

    # Lado derecho de la N
    glVertex2f(2, -3)
    glVertex2f(2,  3)

    glEnd()
    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindñowSize(600, 600)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Letra N en OpenGL")
    inicializar()
    glutDisplayFunc(dibujar_N)
    glutMainLoop()

if __name__ == "__main__":
    main()
