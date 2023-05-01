from tkinter import *
from tkinter import Tk , ttk, messagebox
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

##Cabeçalho
label_nome = Label(frame_cima, text='LOGIN', anchor=NE , font=('Ivy 25'), bg=co1, fg=co4)
label_nome.place(x=5, y=5)

label_linha = Label(frame_cima, text='',width=275, anchor=NW , font=('Ivy 1'), bg=co2, fg=co4)
label_linha.place(x=5, y=45)



##Corpo da tela
label_nome = Label(frame_baixo, text='Nome *', anchor=NW , font=('Ivy 10'), bg=co1, fg=co4)
label_nome.place(x=10, y=20)

entry_nome = Entry(frame_baixo, width=25, justify='left', font=('',15), highlightthickness=1, relief='solid')
entry_nome.place(x=14, y=50)

label_pass = Label(frame_baixo, text='Senha *', anchor=NW , font=('Ivy 10'), bg=co1, fg=co4)
label_pass.place(x=10, y=100)

entry_pass = Entry(frame_baixo, width=25, justify='left', font=('',15), highlightthickness=1, relief='solid')
entry_pass.place(x=14, y=130)

credenciais = ['joao', '12345678']

def verificar_senha():
    nome = entry_nome.get()
    senha = entry_pass.get()

    if nome == 'admin' and senha == 'admin':
        messagebox.showinfo('login','Bem vindo admin')
    elif credenciais[0] == nome and credenciais[1] == senha:
        messagebox.showinfo('login','Bem vindo de volta'+credenciais[0])
    else:
        messagebox.showwarning('Error','Verifique o nome e a senha')

###Botão
button_confirm = Button(frame_baixo,command=verificar_senha,  text='Entrar',width=34,height=2 , font=('Ivy 10'), bg=co2, fg=co1, relief=RAISED, overrelief= RIDGE, )
button_confirm.place(x=15, y=190) 





janela.mainloop()