from math import pi
import tkinter as tk



tela = tk.Tk()
tela.title = ("Cálculo de área de Triângulos")

tela.configure(background="#efefef")
tela.geometry("640x480")




lbl_base = tk.Label(tela, text="Calculadora de área para Triângulos")
lbl_base.place(x=20, y=100)



lbl_base = tk.Label(tela, text="Digite a Base do Triângulo (cm):")
lbl_base.place(x=30, y=200)

txt_base = tk.Entry(tela, width=20, borderwidth=5)
txt_base.place(x=250, y= 200)

lbl_altura = tk.Label(tela, text="Digite a Altura do Triângulo (cm):")
lbl_altura.place(x=30, y=150)

txt_altura = tk.Entry(tela, width=20, borderwidth=5)
txt_altura.place(x=250, y=150)

area =tk.StringVar()

def calcular():
    raio = float(txt_raio.get())
    area = pi*raio **2
    

    altura = float(txt_altura.get())
    base = float(txt_base.get())
    area.set(base*altura/2)

btn_area = tk.Button(tela, text="Calcular",command=calcular)
btn_area.place(x=100, y=240)


lbl_final=tk.Label(tela, text="A área do triângulo equivale a:")
lbl_final.place(x=30, y= 270)
lbl_resultado = tk.Label(tela, textvariable=area)
lbl_resultado.place(x=200, y=270)
                         




tela.mainloop()