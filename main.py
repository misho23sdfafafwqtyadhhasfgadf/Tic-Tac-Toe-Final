import tkinter as tk
from tkinter import messagebox
class TicTacToe:
 def __init__(self, root):
 self.root = root
 self.root.title("Tic Tac Toe - Práctica Git")
 self.turno = "X"
 self.tablero = [""] * 9
 self.botones = []
 self.crear_interfaz()
 def crear_interfaz(self):
 # Crear la cuadrícula de 3x3
 for i in range(9):
 boton = tk.Button(self.root, text="", font=('Arial', 20),
 width=5, height=2,
 command=lambda i=i: self.marcar_casilla(i))
 boton.grid(row=i//3, column=i%3)
 self.botones.append(boton)
 def marcar_casilla(self, i):
 # Lógica básica de marcado
 if self.tablero[i] == "":
 self.tablero[i] = self.turno
 self.botones[i].config(text=self.turno)

 # Cambio de turno simple
 self.turno = "O" if self.turno == "X" else "X"

 # NOTA PARA ESTUDIANTES:
 # Aquí falta implementar la lógica para verificar ganador.
 # Esta debe ser desarrollada en la rama 'feature-logic'.
if __name__ == "__main__":
 root = tk.Window() if hasattr(tk, 'Window') else tk.Tk()
 juego = TicTacToe(root)
 root.mainloop()