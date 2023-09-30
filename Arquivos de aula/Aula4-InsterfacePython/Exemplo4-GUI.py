from tkinter import *
tela = Tk()
tela.title("Fatec Registro")

#dimensões de janela
largura = 800
altura = 300

#resolução do sitema(tela)
largura_screen = tela.winfo_screenwidth()
altura_screen = tela.winfo_screenheight()

#Definição do posicionamento
posx = largura_screen / 2 - largura/2
posy = altura_screen/2 - altura/2

#Visualização do tamanho de tela no terminal
print(largura_screen, altura_screen)

#definição do Geometry
tela.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))

tela.mainloop(0)
