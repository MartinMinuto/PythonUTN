import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
from datetime import time
import customtkinter


'''
nombre: Martin
apellido: Minuto

Enunciado:
Al presionar el botón INICIAR se debe mostrar un mensaje de bienvenida "Bienvenidos a la UTN FRA" cada 3 segundos. 

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=1, pady=10, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):
        self.mostrar_mensaje()

    def mostrar_mensaje(self):
        self.after(3000, self.mostrar_mensaje)
        print("Bienvenidos a la UTN FRA")
        
        

if __name__ == "__main__":
    app = App()
    app.mainloop()