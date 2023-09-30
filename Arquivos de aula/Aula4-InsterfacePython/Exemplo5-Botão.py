from tkinter import *

tela = Tk()



#Criação de Caixa de texto
txt_nome = Entry(tela, width=20 , borderwidth=5, fg="blue", bg="white")
txt_nome.pack()

# txt_nome.insert(0, "Digite o seu nome")

##Criar uma função
def meu_click():
    lbl_hello= Label(tela, text="Bem Vindo "+ txt_nome.get())
    lbl_hello.pack()

    
btn_botao = Button(tela, text="Click", command=meu_click)
btn_botao.pack()

tela.mainloop()