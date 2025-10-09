import tkinter as tk
from tkinter import messagebox

class Fibonacci:
    def __init__(self, cantidad):
        self.cantidad = cantidad
        self.serie = []

    def generarSerie(self):
        a, b = 0, 1
        self.serie = []  # Reinicia la lista en cada ejecución
        for _ in range(self.cantidad):
            self.serie.append(a)
            a, b = b, a + b
        return self.serie


def calcular_fibonacci():
    try:
        cantidad = int(entry_cantidad.get())
        if cantidad <= 0
