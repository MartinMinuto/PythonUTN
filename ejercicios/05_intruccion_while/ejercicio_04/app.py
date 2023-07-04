import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
Enunciado:
Al presionar el botón ‘Validar número’, mediante prompt solicitar al usuario que ingrese un número. 
Se deberá validar que se encuentre entre 0 y 9 inclusive. En caso no coincidir con el rango, 
volverlo a solicitar hasta que la condición se cumpla
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_validar_numero = customtkinter.CTkButton(master=self, text="Ingresar", command=self.btn_validar_numero_on_click)
        self.btn_validar_numero.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_validar_numero_on_click(self):
        flag_continuar = True
        while(flag_continuar):
            numero = prompt(title="Numero", prompt="Coloca tu numero")
            numero_int = int(numero)
            if(numero_int == 1):
                flag_continuar = False
            elif(numero_int == 2):
                flag_continuar = False
            elif(numero_int == 3):
                flag_continuar = False
            elif(numero_int == 4):
                flag_continuar = False
            elif(numero_int == 5):
                flag_continuar = False
            elif(numero_int == 6):
                flag_continuar = False
            elif(numero_int == 7):
                flag_continuar = False
            elif(numero_int == 8):
                flag_continuar = False
            elif(numero_int == 9):
                flag_continuar = False
            elif(numero_int == 0):
                flag_continuar = False


if __name__ == "__main__":
    app = App()
    app.mainloop()