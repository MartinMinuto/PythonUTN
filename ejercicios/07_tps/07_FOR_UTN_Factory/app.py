'''
UTN Software Factory está en la búsqueda de programadores para incorporar a su equipo de 
trabajo. En las próximas semanas se realizará un exhaustivo proceso de selección. Para ello se 
ingresarán los siguientes datos de los 10 postulantes para luego establecer distintas métricas 
necesarias para tomar decisiones a la hora de la selección:

Nombre
Edad (mayor de edad)
Género (F-M-NB)
Tecnología (PYTHON - JS - ASP.NET)
Puesto (Jr - Ssr - Sr)

Informar por pantalla:
a. Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS 
cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr.
b. Nombre del postulante Jr con menor edad.
c. Promedio de edades por género.
d. Tecnologia con mas postulantes (solo hay una).
e. Porcentaje de postulantes de cada genero.

Todos los datos se ingresan por prompt y los resultados se muestran por consola (print)

'''
import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        contador_NB = 0
        contador_edad = 0
        contador_JS = 0
        contador_ASP = 0
        contador_Ssr = 0
        suma_punto_a = 0


        for i in range(1):
            flag_nombre = True
            while(flag_nombre):
                nombre = prompt(title="Nombre", prompt="Ingresar nombre")
                if(nombre is None or nombre == ""):
                    alert("Error", "Eso no parece un nombre")
                elif(nombre.isnumeric()):
                    alert("Error", "Eso no parece un nombre")
                else:
                    flag_nombre = False
            flag_edad = True
            while(flag_edad):
                edad = prompt(title="Edad", prompt="Ingresar edad")
                if(edad is None or edad == "" or edad < "18"):
                    alert("Error", "Eso no parece una edad")
                elif(not edad.isnumeric()):
                    alert("Error", "Eso no parece una edad")
                else:
                    flag_edad = False
                    edad = int(edad)
                    if(edad < 25 and edad < 40):
                        contador_edad += 1
            flag_genero = True
            while(flag_genero):
                genero = prompt(title="Genero", prompt="Ingresar Genero (M,F O NB)")
                match(genero):
                    case "M" | "F":
                        flag_genero = False
                    case "NB":
                        contador_NB += 1
                        flag_genero = False
                    case _: 
                        alert("Error", "Eso no parece ser un Genero")
            flag_tecnologia = True
            while(flag_tecnologia):
                tecnologia = prompt(title="Genero", prompt="Ingresar Tecnologia (PYTHON - JS - ASP.NET)")       
                match(tecnologia):
                    case "PYTHON" | "JS" | "ASP.NET":
                        flag_tecnologia = False
                    case "JS":
                        contador_JS += 1
                        flag_tecnologia = False
                    case "ASP.NET":
                        contador_ASP += 1
                        flag_tecnologia = False
                    case _: 
                        alert("Error", "Eso no parece una tecnologia")
            flag_puesto = True
            while(flag_puesto):           
                puesto = prompt(title="Genero", prompt="Ingresar puesto (Jr - Ssr - Sr)")     
                match(puesto):
                    case "Jr" | "Sr":
                        flag_puesto = False
                    case "Ssr":
                        contador_Ssr += 1
                        flag_puesto = False
                    case _: 
                        alert("Error", "Eso no parece ser un puesto")

        if(contador_NB == 1 and contador_edad == 1 and contador_Ssr == 1):
            if(contador_ASP == 1):
                suma_punto_a += 1
            elif(contador_JS == 1):
                suma_punto_a += 1
        print(suma_punto_a)


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
