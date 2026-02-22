import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe - Práctica Git")
        # Color de fondo oscuro para la ventana
        self.root.configure(bg="#2b2b2b") 
        self.turno = "X"
        self.tablero = [""] * 9
        self.botones = []
        self.juego_activo = True # Controla si el juego sigue en curso
        self.crear_interfaz()

    def crear_interfaz(self):
        # Crear la cuadrícula de 3x3 con estilos
        for i in range(9):
            boton = tk.Button(self.root, text="", font=('Helvetica', 24, 'bold'), width=5, height=2,
                              bg="#3c3f41", fg="white", activebackground="#575a5e",
                              command=lambda i=i: self.marcar_casilla(i))
            boton.grid(row=i//3, column=i%3, padx=5, pady=5)
            self.botones.append(boton)
            
        # Botón de Reinicio
        boton_reinicio = tk.Button(self.root, text="Reiniciar Juego", font=('Arial', 14),
                                   command=self.reiniciar_juego)
        boton_reinicio.grid(row=3, column=0, columnspan=3, pady=10)

    def marcar_casilla(self, i):
        # Lógica de marcado con colores y verificación de victoria
        if self.tablero[i] == "" and self.juego_activo:
            self.tablero[i] = self.turno
            
            # Colores dinámicos: Rojo para X, Azul para O
            color = "#ff5555" if self.turno == "X" else "#5555ff"
            self.botones[i].config(text=self.turno, fg=color)
            
            # Verificar si alguien ganó
            if self.verificar_ganador():
                messagebox.showinfo("Fin del juego", f"¡El jugador {self.turno} ha ganado!")
                self.juego_activo = False
            # Verificar empate
            elif "" not in self.tablero:
                messagebox.showinfo("Fin del juego", "¡Es un empate!")
                self.juego_activo = False
            else:
                # Cambio de turno simple
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

    def reiniciar_juego(self):
        # Limpia todo para volver a jugar
        self.turno = "X"
        self.tablero = [""] * 9
        self.juego_activo = True
        for boton in self.botones:
            boton.config(text="", fg="white") # Resetea texto y color

if __name__ == "__main__":
    root = tk.Tk()
    juego = TicTacToe(root)
    root.mainloop()