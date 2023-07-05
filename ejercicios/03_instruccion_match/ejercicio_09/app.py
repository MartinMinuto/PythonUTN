import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
nombre: Martin
apellido: Minuto

Una agencia de viajes cobra $15.000 por cada estadía como base. 
Luego para calcular las tarifas total realiza el siguiente cálculo, 
en función de la estación del año y del destino elegido:
    Si es invierno: 
        Bariloche tiene un aumento del 20% 
        Cataratas y Córdoba tienen un descuento del 10%
        Mar del plata tiene un descuento del 20%
    Si es Verano:
        Bariloche tiene un descuento del 20%
        Cataratas y Cordoba tienen un aumento del 10%
        Mar del plata tiene un aumento del 20%
    Si es Primavera u Otoño:
        Bariloche tiene un aumento del 10%
        Cataratas tiene un aumento del 10%
        Mar del plata tiene un aumento del 10%
        Córdoba tiene precio sin descuento

'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.label_estaciones = customtkinter.CTkLabel(master=self, text="Estaciones")
        self.label_estaciones.grid(row=0, column=0, padx=20, pady=10)
        estaciones = ['Verano', 'Otoño', 'Invierno', 'Primavera']
        self.combobox_estaciones = customtkinter.CTkComboBox(master=self, values=estaciones)
        self.combobox_estaciones.grid(row=1, column=0, padx=20, pady=(10, 10))

        
        self.label_destinos = customtkinter.CTkLabel(master=self, text="Destinos")
        self.label_destinos.grid(row=2, column=0, padx=20, pady=10)
        destinos = ['Bariloche', 'Mar del plata', 'Cataratas', 'Cordoba']
        self.combobox_destino = customtkinter.CTkComboBox(master=self, values=destinos)
        self.combobox_destino.grid(row=3, column=0, padx=20, pady=(10, 10))

        
        self.btn_informar = customtkinter.CTkButton(master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=4, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_informar_on_click(self):
        precio = int(15000)
        precio_aumento20 = precio * 1.20
        precio_aumento10 = precio * 1.10
        precio_descuento20 = precio * 0.80
        precio_descuento10 = precio * 0.90
        estacion = self.combobox_estaciones.get()
        destino = self.combobox_destino.get()
        match(estacion):
            case "Invierno":
                if(destino == "Bariloche"):
                    alert(title="Precio", message="El precio es ${0}".format(precio_aumento20))
                elif(destino == "Cataratas"):
                    alert(title="Precio", message="El precio es ${0}".format(precio_descuento10))
                elif(destino == "Cordoba"):
                    alert(title="Precio", message="El precio es ${0}".format(precio_descuento10))
                elif(destino == "Mar del plata"):
                    alert(title="Precio", message="El precio es ${0}".format(precio_descuento20))
            case "Verano":
                if(destino == "Bariloche"):
                    alert(title="Precio", message="El precio es ${0}".format(precio_descuento20))
                elif(destino == "Cataratas"):
                    alert(title="Precio", message="El precio es ${0}".format(precio_aumento10))
                elif(destino == "Cordoba"):
                    alert(title="Precio", message="El precio es ${0}".format(precio_aumento10))
                elif(destino == "Mar del plata"):
                    alert(title="Precio", message="El precio es ${0}".format(precio_aumento20))
            case "Otoño" | "Primavera":
                if(destino == "Bariloche"):
                    alert(title="Precio", message="El precio es ${0}".format(precio_aumento10))
                elif(destino == "Cataratas"):
                    alert(title="Precio", message="El precio es ${0}".format(precio_aumento10))
                elif(destino == "Cordoba"):
                    alert(title="Precio", message="El precio es ${0}".format(precio))
                elif(destino == "Mar del plata"):
                    alert(title="Precio", message="El precio es ${0}".format(precio_aumento10))
            
            
    
if __name__ == "__main__":
    app = App()
    app.mainloop()