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
        self.crear_interfaz()

    def crear_interfaz(self):
        # Crear la cuadrícula de 3x3 con nuevos estilos
        for i in range(9):
            boton = tk.Button(self.root, text="", font=('Helvetica', 24, 'bold'), width=5, height=2,
                              bg="#3c3f41", fg="white", activebackground="#575a5e",
                              command=lambda i=i: self.marcar_casilla(i))
            boton.grid(row=i//3, column=i%3, padx=5, pady=5)
            self.botones.append(boton)
            
        # NUEVO CÓDIGO: Botón de Reinicio
        boton_reinicio = tk.Button(self.root, text="Reiniciar Juego", font=('Arial', 14),
                                   command=self.reiniciar_juego)
        boton_reinicio.grid(row=3, column=0, columnspan=3, pady=10)

    def marcar_casilla(self, i):
        # Lógica básica de marcado con colores
        if self.tablero[i] == "":
            self.tablero[i] = self.turno
            
            # Colores dinámicos: Rojo para X, Azul para O
            color = "#ff5555" if self.turno == "X" else "#5555ff"
            self.botones[i].config(text=self.turno, fg=color)
            
            # Cambio de turno simple
            self.turno = "O" if self.turno == "X" else "X"

    # NUEVO CÓDIGO: Función para limpiar el tablero
    def reiniciar_juego(self):
        self.turno = "X"
        self.tablero = [""] * 9
        for boton in self.botones:
            boton.config(text="", fg="white") # Resetea texto y color

if __name__ == "__main__":
    root = tk.Tk()
    juego = TicTacToe(root)
    root.mainloop()