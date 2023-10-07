#Exemplo Somar

#Estrutura Fundamental do Programa TKInter
#1º Importar a biblioteca
#2º Criação da GUI
#3º Adicionar componentes(widget)na janela(GUI)
#4º Evento Loop
import tkinter as tk

#função
def somar_numeros():
    num1 = float(txt_num1.get())
    num2 = float(txt_num2.get())
    resultado.set(num1+num2)

#Configuração da Tela

tela = tk.Tk()
tela.title("Soma de Números")    

#Widgets(Exibição) / Label
lbl_numero1 = tk.Label(tela, text="Numero 1:")
lbl_numero1.place(x=10, y=10)

lbl_numero2 = tk.Label(tela, text="Numero 2:")
lbl_numero2.place(x=10, y=40)

lbl_resultado = tk.Label(tela, text="Resultado:")
lbl_resultado.place(x=10, y=70)

#Widgets(Entrada Dados)/Caixa de texto
txt_num1= tk.Entry(tela)
txt_num1.place(x=100, y=10)

txt_num2= tk.Entry(tela)
txt_num2.place(x=100, y=40)

#widgets (Botão)
btn_somar = tk.Button(tela, text="Somar", command=somar_numeros)
btn_somar.place(x=100, y=100)

#Para Exibição de conteudo em formato String(Label)
resultado=tk.StringVar()

#Exibir Resultado
#Para Exibir o Conteudo da Variável Resultado, Utilize na label a propriedade textvariable

lbl_resultado = tk.Label(tela, textvariable=resultado) 
lbl_resultado.place(x=100, y=70)

tela.mainloop()