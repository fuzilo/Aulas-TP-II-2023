#delta_s = float(input("Digite o deslocamento (em metros):"))

#delta_t = float(input("Digite o tempo(em segundos):"))

#velocidade = delta_s/delta_t
#print(f"Vm ={velocidade:.2f} m/s")
import tkinter as tk
tela = tk.Tk()
tela.title = ("Cálculo de área de Triângulos")
tela.configure(background="#efefef")
tela.geometry("640x480")

lbl_title = tk.Label(tela, text="Calculadora de Velocidade Média")
lbl_title.place(x=20, y=100)

lbl_deltaS = tk.Label(tela, text="Digite o deslocamento (em metros):")
lbl_deltaS.place(x=30, y=200)

txt_deltaS = tk.Entry(tela, width=20, borderwidth=5)
txt_deltaS.place(x=250, y= 200)

lbl_deltaT = tk.Label(tela, text="Digite o tempo (em segundos):")
lbl_deltaT.place(x=30, y=150)

txt_deltaT = tk.Entry(tela, width=20, borderwidth=5)
txt_deltaT.place(x=250, y=150)

velocidade =tk.StringVar()

def calcular():
    deltaS = float(txt_deltaS.get())
    deltaT = float(txt_deltaT.get())
    resultado = f"Vm = {deltaS/deltaT:.2f} m/s"
    velocidade.set(resultado)

btn_calc = tk.Button(tela, text="Calcular",command=calcular)
btn_calc.place(x=100, y=240)


lbl_final=tk.Label(tela, text="A Velocidade média equivale a:")
lbl_final.place(x=30, y= 270)
lbl_resultado = tk.Label(tela, textvariable=velocidade)
lbl_resultado.place(x=200, y=270)
                         




tela.mainloop()