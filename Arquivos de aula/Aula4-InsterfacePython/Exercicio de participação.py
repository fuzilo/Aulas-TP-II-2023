#Criar uma tela para cadastrar 5 Clientes
import tkinter as tk

tela = tk.Tk()
tela.title("Cadastrar Clientes")

tela.configure(background="#efefef")
tela.geometry("800x600")

tela.resizable(True, True)
tela.maxsize(width= 960 , height= 720)

tela.minsize(width= 640, height=480)

txt_nome = tk.Entry(tela, width=20,borderwidth=5 )
txt_nome.pack()

# txt_cpf = tk.Entry(tela, width=20,borderwidth=5 ).place(x=10, y=30)
# txt_cpf.pack()

# txt_telefone = tk.Entry(tela, width=20,borderwidth=5 ).place(x=10, y=50)
# txt_telefone.pack()

def cadastrar():
    lbl_nome = tk.Label(tela, text=txt_nome.get())
    lbl_nome.pack()


btn_botao = tk.Button(tela, text="Cadastrar", command=cadastrar)
btn_botao.pack()

tela.mainloop()