#importação da biblioteca
from tkinter import *
tela = Tk()
# Titulo na barra de Tarefas
tela.title("Fatec Registro")
#Configuração da cor de tela
tela.configure(background='#efefef')
#Configuração do tamanho da tela
tela.geometry("800x600")

#configuração de limite de tela
tela.resizable(True,True)
tela.maxsize(width=800, height=600)

tela.minsize(width=500, height=300)

#Adicionar componete
lbl_teste = Label(tela, text="TESTE"). place(x=10, y=10)
#lbl_teste e o nome de identificação interno da label
# label e o tipo do componente















tela.mainloop()

