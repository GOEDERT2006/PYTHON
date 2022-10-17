import tkinter as tk
from tkinter import *
from tkinter import font
from turtle import update
from tkcalendar import Calendar, DateEntry
from tkinter import ttk
from view import *
from tkinter import messagebox

co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#038cfc"   # azul
co7 = "#ef5350"   # vermelha
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # sky blue

janela = Tk()
janela.title("LOCADORA")
janela.geometry('1043x453')
janela.configure(background=co9)
janela.resizable(width=FALSE, height=FALSE)


frame_cima = Frame(janela, width=310, height=50, bg=co2, relief='flat')
frame_cima.grid(row=0, column=0)

frame_baixo = Frame(janela, width=310, height=403, bg=co1, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NSEW, padx=0,pady=1)

frame_direita = Frame(janela, width=588, height=403, bg=co1, relief='flat')
frame_direita.grid(row=0, column=1, rowspan=2, padx=1, sticky=NSEW)

app_nome = Label(frame_cima, text='     Cadastro de Clientes', anchor=NW,font=('Ivy 15 bold'), bg=co2, fg=co0, relief='flat')
app_nome.place(x=10, y=20)


global tree

def inserir():
    nome = e_nome.get()
    cpf = e_cpf.get()
    endereco = e_endereco.get()
    email = e_email.get()
    telefone = e_telefone.get()
    datanascimento = e_datanascimento.get()
    

    lista = [nome, cpf, endereco, email, telefone, datanascimento]

    if nome == '':
        messagebox.showerror('ERRO','O NOME NAO PODE SER VAZIO!!!')
    else:
        inserir_info(lista)
        messagebox.showinfo('SUCESSO','DADOS INSERIDOS COM SUCESS0!!!')

        e_nome.delete(0,'end')
        e_cpf.delete(0,'end')
        e_endereco.delete(0,'end')
        e_email.delete(0,'end')
        e_telefone.delete(0,'end')
        e_datanascimento.delete(0,'end')

    for widget in frame_direita.winfo_children():
        widget.destroy()

    mostrar()            




def atualizar():
    try:

    

        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        tree_lista = treev_dicionario['values']

        valor_id = tree_lista[0]

        e_nome.delete(0,'end')
        e_cpf.delete(0,'end')
        e_endereco.delete(0,'end')
        e_email.delete(0,'end')
        e_telefone.delete(0,'end')
        e_datanascimento.delete(0,'end')

        e_nome.insert(0,tree_lista[1])
        e_cpf.insert(0,tree_lista[2])
        e_endereco.insert(0,tree_lista[3])
        e_email.insert(0,tree_lista[4])
        e_telefone.insert(0,tree_lista[5])
        e_datanascimento.insert(0,tree_lista[6])


        
        def update():
            nome = e_nome.get()
            cpf = e_cpf.get()
            endereco = e_endereco.get()
            email = e_email.get()
            telefone = e_telefone.get()
            datanascimento = e_datanascimento.get()

            lista = [nome, cpf, endereco, email, telefone, datanascimento, valor_id]

            if nome == '':
                messagebox.showerror('ERRO','O NOME NAO PODE SER VAZIO!!!')
            else:
                atualizar_info(lista)
                messagebox.showinfo('SUCESSO','DADOS ATUALIZADOS COM SUCESS0!!!')

                e_nome.delete(0,'end')
                e_cpf.delete(0,'end')
                e_endereco.delete(0,'end')
                e_email.delete(0,'end')
                e_telefone.delete(0,'end')
                e_datanascimento.delete(0,'end')

            for widget in frame_direita.winfo_children():
                widget.destroy()


            mostrar()    

        b_confirmar = Button(frame_baixo, command=update, text='Confirmar ',width=10,font=('Ivy 7 bold'), bg=co6, fg=co1, relief='raised', overrelief='ridge')
        b_confirmar.place(x=100, y=350)    

        
    except IndexError:
        messagebox.showerror('ERRO','SELECIONE UM DOS DADOS NA TABELA!!!')

def deletar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        tree_lista = treev_dicionario['values']

        valor_id = [tree_lista[0]]

        deletar_info(valor_id)
        messagebox.showinfo('SUCESSO','DADOS DELETADOS DA TABELA')

        for widget in frame_direita.winfo_children():
            widget.destroy()

        mostrar()

    except IndexError:
        messagebox.showerror('ERRO','SELECIONE UM DADO NA TABELA')

l_nome = Label(frame_baixo, text='Nome *', anchor=NW,font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_nome.place(x=10, y=20)
e_nome = Entry(frame_baixo, width=45,justify='left',relief='solid')
e_nome.place(x=15, y=40)

l_cpf = Label(frame_baixo, text='CPF *', anchor=NW,font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_cpf.place(x=10, y=60)
e_cpf = Entry(frame_baixo, width=45,justify='left',relief='solid')
e_cpf.place(x=15, y=80)

l_endereco = Label(frame_baixo, text='Endereço *', anchor=NW,font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_endereco.place(x=10, y=100)
e_endereco = Entry(frame_baixo, width=45,justify='left',relief='solid')
e_endereco.place(x=15, y=120)

l_email = Label(frame_baixo, text='Email *', anchor=NW,font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_email.place(x=10, y=140)
e_email = Entry(frame_baixo, width=45,justify='left',relief='solid')
e_email.place(x=15, y=160)

l_telefone = Label(frame_baixo, text='Telefone *', anchor=NW,font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_telefone.place(x=10, y=180)
e_telefone = Entry(frame_baixo, width=45,justify='left',relief='solid')
e_telefone.place(x=15, y=200)

l_datanascimento = Label(frame_baixo, text='Data Nascimento *', anchor=NW,font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_datanascimento.place(x=10, y=220)
e_datanascimento = Entry(frame_baixo, width=45,justify='left',relief='solid')
e_datanascimento.place(x=15, y=240)



l_cal = Label(frame_baixo, text='Data Consulta *', anchor=NW,font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_cal.place(x=10, y=260)
e_cal = DateEntry(frame_baixo, width=12,background='darkblue', foreground='white',borderwidth=2)
e_cal.place(x=15, y=280)

b_inserir = Button(frame_baixo, command=inserir, text='Inserir ', anchor=NW,font=('Ivy 9 bold'), bg=co2, fg=co1, relief='raised', overrelief='ridge')
b_inserir.place(x=15, y=310)

b_atualizar = Button(frame_baixo, command=atualizar, text='Atualizar ', anchor=NW,font=('Ivy 9 bold'), bg=co6, fg=co1, relief='raised', overrelief='ridge')
b_atualizar.place(x=100, y=310)

b_deletar = Button(frame_baixo, command=deletar, text='Deletar ', anchor=NW,font=('Ivy 9 bold'), bg=co7, fg=co1, relief='raised', overrelief='ridge')
b_deletar.place(x=200, y=310)



def mostrar():

    global tree
    



    lista = mostrar_info()
            


    # lista para cabecario
    tabela_head = ['ID','Nome','CPF', 'Endereco','Email', 'Telefone', 'Data Nascimento']

    df_list = lista


    # criando a tabela
    tree = ttk.Treeview(frame_direita, selectmode="extended", columns=tabela_head, show="headings")

    # vertical scrollbar
    vsb = ttk.Scrollbar(frame_direita, orient="vertical", command=tree.yview)

    # horizontal scrollbar
    hsb = ttk.Scrollbar( frame_direita, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    frame_direita.grid_rowconfigure(0, weight=12)


    hd=["nw","nw","nw","nw","nw","center","center"]
    h=[30,170,140,100,120,50,100]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        # adjust the column's width to the header string
        tree.column(col, width=h[n],anchor=hd[n])
        
        n+=1

    for item in lista:
        tree.insert('', 'end', values=item)

mostrar()
janela.mainloop()