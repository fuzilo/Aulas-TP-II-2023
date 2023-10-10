
# base = float(input("Base do Triângulo (cm):"))
# alt = float(input("Altura do triângulo (cm):"))
# area = (base*alt)/2
# print(f"Área = {area:.2f} cm²")


import tkinter as tk

tela = tk.Tk()
tela.title = ("Cálculo de área de Triângulos")

tela.configure(background="#efefef")
tela.geometry("800x600")


lbl_base = tk.Label(tela, text="Digite a Base do Triângulo (cm):")


lbl_base = tk.Label(tela, text="Digite a Base do Triângulo (cm):")
txt_base = tk.Entry(tela, width=20, borderwidth=5)
txt_base.pack()

lbl_altura = tk.Label(tela, text="Digite a Altura do Triângulo (cm):")
txt_altura = tk.Entry(tela, width=20, borderwidth=5)
txt_altura.pack()




tela.mainloop()