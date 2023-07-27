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
        contador_edad = 0
        contador_jr = 0
        contador_ssr = 0
        contador_sr = 0
        contador_m = 0
        contador_f = 0
        contador_nb = 0
        contador_phyton = 0
        contador_js = 0
        contador_net = 0
        cantidad_postulantes = 2

        for i in range(cantidad_postulantes):
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
                    if(edad <= 25 and edad <= 40):
                        contador_edad += 1
            flag_genero = True
            while(flag_genero):
                genero = prompt(title="Genero", prompt="Ingresar Genero (M,F o NB)")
                match(genero):
                    case "M":
                        flag_genero = False
                        contador_m += 1
                    case "F":
                        flag_genero = False
                        contador_f += 1
                    case "NB":
                        flag_genero = False
                        contador_nb += 1
                    case _: 
                        alert("Error", "Eso no parece ser un Genero")
            flag_tecnologia = True
            while(flag_tecnologia):
                tecnologia = prompt(title="Genero", prompt="Ingresar Tecnologia (PYTHON - JS - ASP.NET)")       
                match(tecnologia):
                    case "PYTHON":
                        flag_tecnologia = False
                        contador_phyton += 1
                    case "JS" :
                        flag_tecnologia = False
                        contador_js += 1
                    case "ASP.NET":
                        flag_tecnologia = False
                        contador_net += 1
                    case _: 
                        alert("Error", "Eso no parece una tecnologia")
            flag_puesto = True
            while(flag_puesto):           
                puesto = prompt(title="Genero", prompt="Ingresar puesto (Jr - Ssr - Sr)")     
                match(puesto):
                    case "Jr":
                        flag_puesto = False
                        contador_jr += 1
                    case "Ssr":
                        flag_puesto = False
                        contador_ssr += 1
                    case "Sr":
                        flag_puesto = False
                        contador_sr += 1
                    case _: 
                        alert("Error", "Eso no parece ser un puesto")


        total_m = ((contador_m * 100) / cantidad_postulantes)
        tota_f = ((contador_f * 100) / cantidad_postulantes)
        total_nb = ((contador_nb * 100) / cantidad_postulantes)

        print(f"los valores son %{total_m}, %{tota_f} y %{total_nb}")

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
