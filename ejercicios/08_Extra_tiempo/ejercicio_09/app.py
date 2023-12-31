import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import time
import customtkinter


'''
nombre: Martin
apellido: Minuto

Luego de presionar el botón 'Iniciar',se disparara ; un temporizador de una función que haga visible los tres botones ocultos. 
Se deberá calcular e informar la cantidad de segundos transcurridos desde que estos botones se hicieron visibles hasta el momento 
que el usuario logró pulsar todos los botones.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=1, pady=10, columnspan=2, sticky="nsew")

        self.btn_oculto_1 = customtkinter.CTkButton(master=self, text="Boton Oculto 1", command=self.btn_oculto_1_on_click)
        self.btn_oculto_2 = customtkinter.CTkButton(master=self, text="Boton Oculto 2", command=self.btn_oculto_2_on_click)
        self.btn_oculto_3 = customtkinter.CTkButton(master=self, text="Boton Oculto 3", command=self.btn_oculto_3_on_click)

        self.flag_btn_1 = False
        self.flag_btn_2 = False
        self.flag_btn_3 = False

        self.tiempo_inicial = 0

    def btn_mostrar_on_click(self):
        self.start_time = time.time()
        self.btn_mostrar.after(0, self.activar_boton_oculto)
        
    
    def btn_oculto_1_on_click(self):
        self.flag_btn_1 = True
        self.btn_check_all_press()

    def btn_oculto_2_on_click(self):
        self.flag_btn_2 = True
        self.btn_check_all_press()

    def btn_oculto_3_on_click(self):
        self.flag_btn_3 = True
        self.btn_check_all_press
    
    def btn_check_all_press(self):
        if self.flag_btn_1 and self.flag_btn_2 and self.flag_btn_3:
            tiempo_trascurido = time.time() - self.tiempo_inicial
            print("Tiempo trascurido {0} segundos".format(tiempo_trascurido))
            
    def activar_boton_oculto(self):
        self.btn_oculto_1.grid()
        self.btn_oculto_2.grid()
        self.btn_oculto_3.grid()
        

if __name__ == "__main__":
    app = App()
    app.mainloop()