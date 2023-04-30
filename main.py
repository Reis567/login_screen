from tkinter import *
from tkinter import Tk , ttk
from variaveis import co0 , co1 , co2 , co3 , co4

#Janela criada
janela = Tk()

janela.title("Login")
janela.geometry('310x300')
janela.configure(background=co1)
janela.resizable(width=False, height=False)


#First frame
frame_cima = Frame(janela, width=310, height=50, bg=co1, relief='flat')
frame_cima.grid(row=0, column=0 , pady=1, padx=0, sticky=NSEW)

#Second frame
frame_baixo = Frame(janela, width=310, height=250, bg=co1, relief='flat')
frame_baixo.grid(row=1, column=0 , pady=1, padx=0, sticky=NSEW)


#Frames Configuration

label_nome = Label(frame_cima, text='LOGIN', anchor=NE , font=('Ivy 25'), bg=co1, fg=co4)
label_nome.place(x=5, y=5)

label_linha = Label(frame_cima, text='',width=275, anchor=NW , font=('Ivy 1'), bg=co2, fg=co4)
label_linha.place(x=5, y=45)


janela.mainloop()