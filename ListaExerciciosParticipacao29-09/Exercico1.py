#estatura = float(input("Digite a sua estatura (em Metros):"))
#estatura = estatura *100
#print(f"Sua estatura é de {estatura} cm.")
import tkinter as tk

tela = tk.Tk()
tela.title = ("Cálculo de área de Triângulos")

tela.configure(background="#efefef")
tela.geometry("640x480")


lbl_title = tk.Label(tela, text="Conversor de Altura")
lbl_title.place(x=20, y=100)


lbl_estatura = tk.Label(tela, text="Digite a sua estatura (em metros):")
lbl_estatura.place(x=30, y=200)

txt_estatura = tk.Entry(tela, width=20, borderwidth=5)
txt_estatura.place(x=250, y= 200)

resultado =tk.StringVar()

def calcular():
    estatura = float(txt_estatura.get()) * 100
    resultado.set(f"A área sua estatura é de: {estatura:.2f} cm")

    

btn_area = tk.Button(tela, text="Calcular",command=calcular)
btn_area.place(x=100, y=240)



lbl_resultado = tk.Label(tela, textvariable=resultado)
lbl_resultado.place(x=30, y=270)
                         




tela.mainloop()