import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe - Práctica Git")
        self.turno = "X"
        self.tablero = [""] * 9
        self.botones = []
        self.juego_activo = True # Variable para saber si el juego debe continuar
        self.crear_interfaz()

    def crear_interfaz(self):
        # Crear la cuadrícula de 3x3
        for i in range(9):
            boton = tk.Button(self.root, text="", font=('Arial', 20), width=5, height=2,
                              command=lambda i=i: self.marcar_casilla(i))
            boton.grid(row=i//3, column=i%3)
            self.botones.append(boton)

    def marcar_casilla(self, i):
        # Lógica de marcado y verificación
        if self.tablero[i] == "" and self.juego_activo:
            self.tablero[i] = self.turno
            self.botones[i].config(text=self.turno)
            
            # Verificar si con este movimiento alguien ganó
            if self.verificar_ganador():
                messagebox.showinfo("Fin del juego", f"¡El jugador {self.turno} ha ganado!")
                self.juego_activo = False
            # Verificar si ya no quedan espacios vacíos (Empate)
            elif "" not in self.tablero:
                messagebox.showinfo("Fin del juego", "¡Es un empate!")
                self.juego_activo = False
            else:
                # Si nadie ha ganado ni empatado, cambia el turno
                self.turno = "O" if self.turno == "X" else "X"

    def verificar_ganador(self):
        # Revisa filas, columnas y diagonales para buscar 3 iguales
        combinaciones = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Filas horizontales
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columnas verticales
            [0, 4, 8], [2, 4, 6]              # Diagonales
        ]
        for combo in combinaciones:
            if self.tablero[combo[0]] == self.tablero[combo[1]] == self.tablero[combo[2]] != "":
                return True
        return False

if __name__ == "__main__":
    root = tk.Tk()
    juego = TicTacToe(root)
    root.mainloop()