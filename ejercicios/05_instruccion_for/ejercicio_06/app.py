import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Martin 
Minuto
Al presionar el botón Mostrar pedir un número. mostrar los números pares desde 
el 1 al número ingresado, y mostrar la cantidad de números pares encontrados.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        numero = int(prompt(title="Numero", prompt="Seleccione un numero"))
        numero_pares = []

        for i in range(1, numero + 1):
            if i % 2 == 0:
              numero_pares.append(i)

        cantidad_pares = len(numero_pares)

        print("Los numeros pares son {0} y la cantidad de numero pares son {1}".format(numero_pares, cantidad_pares))
        
    
if __name__ == "__main__":
    app = App()
    app.mainloop()