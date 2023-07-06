import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Al presionar el botón Mostrar pedir un número. Informar si el número es PRIMO o no.
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
        numero_primo = True

        if numero_primo <= 0:
            numero_primo = False
        else:
            for i in range(2, numero):
                if numero % i == 0:
                    numero_primo = False
                    break

        if numero_primo:
            alert(title="Numero", message=f"El {numero} es primo")
        else:
            alert(title="Numero", message=f"El {numero} no es primo")

    
if __name__ == "__main__":
    app = App()
    app.mainloop()