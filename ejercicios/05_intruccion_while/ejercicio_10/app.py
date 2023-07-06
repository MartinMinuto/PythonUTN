import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Martin
apellido: Minuto

Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    La suma acumulada de los negativos
    La suma acumulada de los positivos
    Cantidad de números positivos ingresados
    Cantidad de números negativos ingresados
    Cantidad de ceros
    Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        numeros = []
        positivo = 0
        cantidad_positivos = 0
        negativo = 0
        cantidad_negativos = 0
        cantidad_cero = 0

        while True:
            numero = prompt(title="Ingresar número", prompt="Ingrese un número:")

            if numero is None:
                break
            
            numero = float(numero)
            numeros.append(numero)
        
            if(numero > 0):
                positivo += numero
                cantidad_positivos += 1
            elif(numero < 0):
                negativo += numero
                cantidad_negativos += 1
            else:
                cantidad_cero += 1

        diferencia = cantidad_positivos - cantidad_negativos

        alert(title="Resultados", message="La suma de los negativos es: {0} la suma de los positivos es: {1} la cantidad de numeros positivos es: {2} la cantidad de numero negativos es: {3} la cantidad de ceros es: {4} y la diferencia de positivos y negativos es: {5}".format(negativo, positivo, cantidad_positivos, cantidad_negativos, cantidad_cero, diferencia))




    
if __name__ == "__main__":
    app = App()
    app.mainloop()
