import tkinter as tk


tela = tk.Tk()
tela.title = ("Reajuste Salarial")

tela.configure(background="#efefef")
tela.geometry("640x480")

lbl_titulo = tk.Label(tela, text="Calculadora de Reajuste Salarial")
lbl_titulo.place(x=20, y=100)

lbl_Salbase = tk.Label(tela, text="Digite o Salário Atual:")
lbl_Salbase.place(x=30, y=150)

txt_Salbase = tk.Entry(tela, width=20, borderwidth=5)
txt_Salbase.place(x=250, y= 150)

lbl_aumento = tk.Label(tela, text="Digite porcentagem de reajuste (%)")
lbl_aumento.place(x=30, y=200)

txt_aumento = tk.Entry(tela, width=20, borderwidth=5)
txt_aumento.place(x=250, y=200)

result =tk.StringVar()
#result = tk.Variable()

def calcular():
    salbase = float(txt_Salbase.get())
    aumento = float(txt_aumento.get())
    result.set(salbase*(1+aumento/100))
    lbl_final=tk.Label(tela, text="Parabéns Você Ganhou um Aumento")
    lbl_final.place(x=30, y= 270)
    lbl_resultado = tk.Label(tela, textvariable=result)
    lbl_resultado.place(x=200, y=290)
    

btn_area = tk.Button(tela, text="Calcular",command=calcular)
btn_area.place(x=100, y=240)



                         




tela.mainloop()