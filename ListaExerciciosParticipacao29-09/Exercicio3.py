from math import pi
import tkinter as tk



tela = tk.Tk()
tela.title = ("Cálculo de área de Triângulos")

tela.configure(background="#efefef")
tela.geometry("640x480")




lbl_base = tk.Label(tela, text="Calculadora de área de Círculos")
lbl_base.place(x=20, y=100)



lbl_base = tk.Label(tela, text="Digite o Raio do Círculo (cm):")
lbl_base.place(x=30, y=200)

txt_raio = tk.Entry(tela, width=20, borderwidth=5)
txt_raio.place(x=250, y= 200)


area =tk.StringVar()

def calcular():
    raio = float(txt_raio.get())
    area_calculada = (pi*raio **2)
    area.set(f"A área do Cículo equivale a : {area_calculada:.2f} cm²")

    

btn_area = tk.Button(tela, text="Calcular",command=calcular)
btn_area.place(x=100, y=240)



lbl_resultado = tk.Label(tela, textvariable=area)
lbl_resultado.place(x=30, y=270)
                         




tela.mainloop()