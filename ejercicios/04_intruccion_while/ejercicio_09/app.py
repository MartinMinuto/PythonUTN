import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Martin
apellido: Minuto

Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario quiera 
hasta que presione el botón Cancelar (en el prompt). 
Luego determinar el máximo y el mínimo 
e informarlos en los cuadros de textos txt_maximo y txt_minimo respectivamente

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
        
        self.txt_minimo = customtkinter.CTkEntry(master=self, placeholder_text="Mínimo")
        self.txt_minimo.grid(row=0, padx=20, pady=20)

        self.txt_maximo = customtkinter.CTkEntry(master=self, placeholder_text="Máximo")
        self.txt_maximo.grid(row=1, padx=20, pady=20)

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        flag = True

        while True:
            numero = prompt(title="Ingresar número", prompt="Ingrese un número:")
            
            if numero is None:
                break
            elif numero == "0":
                alert(title="Titulo", message="Se ingreso 0")
                break
            elif numero == "":
                alert(title="Titulo", message="No se ingresaron numeros")
                break

            numero = float(numero)
            if(flag == True):
                mayor = numero
                menor = numero
                flag = False
            else:
                if(numero > mayor):
                    mayor = numero
                elif(numero < menor):
                    menor = numero

        if(numero != ""):
            self.txt_minimo.delete(0,100000)
            self.txt_minimo.insert(0, str(menor))

            self.txt_maximo.delete(0,100000)
            self.txt_maximo.insert(0, str(mayor))
        elif(numero == "0" or 0):
            self.txt_minimo.delete(0,100000)
            self.txt_maximo.delete(0,100000)
        elif(numero == ""):
            self.txt_minimo.delete(0,100000)
            self.txt_maximo.delete(0,100000)


    
if __name__ == "__main__":
    app = App()
    app.mainloop()
