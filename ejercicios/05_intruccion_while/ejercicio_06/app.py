import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar 5 números mediante prompt. 
Calcular la suma acumulada y el promedio de los números ingresados. 
Luego informar los resultados en las cajas de texto txt_suma_acumulada y txt_promedio

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
        
        self.txt_suma_acumulada = customtkinter.CTkEntry(master=self, placeholder_text="Suma acumulada")
        self.txt_suma_acumulada.grid(row=0, padx=20, pady=20)

        self.txt_promedio = customtkinter.CTkEntry(master=self, placeholder_text="Promedio")
        self.txt_promedio.grid(row=1, padx=20, pady=20)

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        flag_continuar = True
        while(flag_continuar):
            nota1 = int(prompt(title="Primera nota", prompt="Ingrese la nota"))
            nota2 = int(prompt(title="Segunda nota", prompt="Ingrese la nota"))
            nota3 = int(prompt(title="Tercera nota", prompt="Ingrese la nota"))
            nota4 = int(prompt(title="Cuarta nota", prompt="Ingrese la nota"))
            nota5 = int(prompt(title="Quinta nota", prompt="Ingrese la nota"))
            suma = nota1 + nota2 + nota3 + nota4 + nota5
            promedio = suma / 5
            self.txt_suma_acumulada.insert(0, suma)
            self.txt_promedio.insert(0, promedio)
            flag_continuar = False


    
if __name__ == "__main__":
    app = App()
    app.mainloop()
