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
            boton = tk.Button(self.root, text="", font=('Arial', 20), width=5, height=2,
                              command=lambda i=i: self.marcar_casilla(i))
            boton.grid(row=i//3, column=i%3)
            self.botones.append(boton)
            
        # NUEVO CÓDIGO: Botón de Reinicio
        boton_reinicio = tk.Button(self.root, text="Reiniciar Juego", font=('Arial', 14),
                                   command=self.reiniciar_juego)
        boton_reinicio.grid(row=3, column=0, columnspan=3, pady=10)

    def marcar_casilla(self, i):
        # Lógica básica de marcado
        if self.tablero[i] == "":
            self.tablero[i] = self.turno
            self.botones[i].config(text=self.turno)
            
            # Cambio de turno simple
            self.turno = "O" if self.turno == "X" else "X"

    # NUEVO CÓDIGO: Función para limpiar el tablero
    def reiniciar_juego(self):
        self.turno = "X"
        self.tablero = [""] * 9
        for boton in self.botones:
            boton.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    juego = TicTacToe(root)
    root.mainloop()