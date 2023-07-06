import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
from datetime import time
import customtkinter


'''
nombre: Martin
apellido: Minuto

Luego de presionar el botón 'Iniciar', se inhabilita el botón durante 3(tres) segundos
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=1, pady=10, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        self.btn_mostrar.configure(state="disabled")
        self.btn_mostrar.after(3000, self.activar_boton)
        print("Hola")

    def activar_boton(self):
        self.btn_mostrar.configure(state="normal")
        
            

if __name__ == "__main__":
    app = App()
    app.mainloop()