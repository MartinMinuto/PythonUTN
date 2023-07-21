'''
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por consola (print)

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
        edad_sumador = 0
        contador_edad = 0
        cantidad_votos = 0
        cantidad_de_candidatos = 0
        flag_votos = True

        Continuar = question("Titulo", "Desea comenzar?")
        while(Continuar):
            nombre = prompt("Titulo", prompt="Nombre del candidato")

            if(nombre is None):
                alert("Error", message="No se puede registrar el nombre")
                break
            if(not nombre.isalpha() or nombre == ""):
                alert("Error", message="No se puede registrar el nombre")
                break

            edad = prompt("Titulo", prompt="Edad")

            if(edad is None):
                alert("Error", message="No se puede registrar la edad")
                break
            if(not edad.isnumeric or edad == ""):
                alert("Error", message="No se puede registrar la edad")
                break
            edad = int(edad)
            if(edad < 24):
                alert("Error", message="No se puede registrar la edad")
                break
            else:
                edad_sumador += edad
                contador_edad += 1

            votos = prompt("Titulo", prompt="Cantidad de votos")

            if(votos is None):
                alert("Error", message="No se puede registrar los votos")
                break
            if(not votos.isnumeric or votos == ""):
                alert("Error", message="No se puede registrar los votos")
                break
            votos = int(votos)
            if(votos < 0):
                alert("Error", message="No se puede registrar los votos")
                break
            elif(flag_votos):
                votos_mas_cantidad = 0
                votos_menor_cantidad = 0
                nombre_mas_votos = nombre
                nombre_menos_votos = nombre
                edad_menor = edad
                flag_votos = False
            elif(votos_mas_cantidad > votos):
                votos_mas_cantidad = 0
                votos_mas_cantidad += votos
                nombre_mas_votos = nombre
            elif(votos_menor_cantidad < votos):
                votos_menor_cantidad = 0
                votos_menor_cantidad += votos
                nombre_menos_votos = nombre
                edad_menor = edad

            cantidad_votos += votos
            cantidad_de_candidatos += 1

            Seguir = question(title="Continuar", message="Desea seguir?")

            if(Seguir == False):
                break

        if(Continuar == False or nombre is None or edad is None or votos is None):
            print("No se resgitraron datos")
        else:
            print(f"Persona con mas votos {nombre_mas_votos}")
            print(f"Nombre del candidato con menos votos {nombre_menos_votos}")
            print(f"La edad de {nombre_menos_votos} que tiene menos votos es {edad_menor}")
            print(f"Promedio de edad de los candidatos {edad_sumador / contador_edad}")
            print(f"Cantidad total de votos {cantidad_votos}")
            




if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
