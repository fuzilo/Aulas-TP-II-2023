from tkinter import *
tela = Tk()
tela.title("Fatec Registro")
tela.geometry("700x600")
tela.maxsize(width=800 ,height= 700)
tela.minsize(width=500, height=300)

lbl_nome = Label(tela, text="Nome", font="Arial 20 bold italic", fg="green").place (x=10, y=10)

lbl_cpf = Label(tela, text="CPF", font="Times 15 italic", fg="black").place(x=10, y=50)

tela.mainloop()

