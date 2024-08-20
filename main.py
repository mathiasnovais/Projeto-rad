from tkinter.ttk import *
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd


# importando pillow
import PIL.Image
from PIL import ImageTk, Image

# tk calendario
from tkcalendar import Calendar, DateEntry
from datetime import date

#importando view
from view import *

# cores
co0 = "#2e2d2b" # Preta
co1 = "#feffff" # Branca
co2 = "#e5e5e5" # grey
co3 = "#00a095" # Verde
co4 = "#403d3d" # letra
co6 = "#003452" # azul
co7 = "#ef5350" # vermelha

co6 = "#038cfc" # azul
co8 = "#263238" # + verde
co9 = "#e9edf5" # + verde

# Criando janela
janela = Tk()
janela.title("")
janela.geometry('850x620')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

style = Style(janela)
style.theme_use("clam")


# Criando Frames
frame_logo = Frame(janela, width=850, height=52, bg=co6)
frame_logo.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=1, columnspan=1, ipadx=680)

frame_dados = Frame(janela, width=850, height=65, bg=co1)
frame_dados.grid(row=2, column=0, pady=0, padx=0, sticky=NSEW)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=3, columnspan=1, ipadx=680)

frame_detalhes = Frame(janela, width=850, height=200, bg=co1)
frame_detalhes.grid(row=4, column=0, pady=0, padx=10, sticky=NSEW)

frame_tabela = Frame(janela, width=850, height=200, bg=co1)
frame_tabela.grid(row=5, column=0, pady=0, padx=10, sticky=NSEW)


# Trabalhando no frame logo --------------------------------------------
app_lg = Image.open('logo.png')
app_lg = app_lg.resize((50,50))
app_lg = ImageTk.PhotoImage(app_lg)
app_logo = Label(frame_logo, image=app_lg, text="Cadastro de Alunos", width=850, compound=LEFT, relief=RAISED, anchor=NW, font=('Ivy 15 bold'), bg=co6, fg=co1)
app_logo.place(x=0, y=0)

# funcao para cadastrar alunos
def alunos():
        
    # funcao novo aluno
        def novo_aluno():

            # funcao para escolher imagem
            global imagem, imagem_string, l_imagem
            
            nome = e_nome.get()
            email = e_email.get()
            telefone = e_tel.get()
            sexo = c_sexo.get()
            data = data_nascimento.get()
            cpf = e_cpf.get()
            curso = c_turma.get()
            imagem = imagem_string

            lista = [nome, email, telefone, sexo, imagem, data, cpf, curso]

            #verificando caso algum campo esteja vazio ou não
            for i in lista:
                if i=='':
                    messagebox.showerror('Erro', 'Preencha todos os campos')
                    return
                
            # inserindo os dados no banco de dados
            criar_alunos(lista)

            # mostrando a mensagem de sucesso
            messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso')
            
            #limpando os campos de entrada 
            e_nome.delete(0, END)
            e_email.delete(0, END)
            c_sexo.delete(0, END)
            data_nascimento.delete(0, END)
            e_cpf.delete(0, END)
            c_turma.delete(0, END)

            # monstrando os valores na tabela
            mostrar_alunos()
    
    #funcao atualizar aluno
        def update_aluno():
            # funcao para escolher imagem
            global imagem, imagem_string, l_imagem
            
            try:
                tree_itens = tree_aluno.focus()
                tree_dicionario = tree_aluno.item(tree_itens)
                tree_lista = tree_dicionario['values']

                valor_id = tree_lista[0]

                #limpando os campos de entrada 
                e_nome.delete(0, END)
                e_email.delete(0, END)
                e_tel.delete(0, END)
                c_sexo.delete(0, END)
                data_nascimento.delete(0, END)
                e_cpf.delete(0, END)
                c_turma.delete(0, END)

                #inserindo os valores nos campos de entrada
                e_nome.insert(0, tree_lista[1])
                e_email.insert(0, tree_lista[2])
                e_tel.insert(0, tree_lista[3])
                c_sexo.insert(0, tree_lista[4])
                data_nascimento.insert(0, tree_lista[6])
                e_cpf.insert(0, tree_lista[7])
                c_turma.insert(0, tree_lista[8])

                imagem = tree_lista[5]
                imagem_string = imagem

                imagem = Image.open(imagem)
                imagem = imagem.resize((130,130))
                imagem = ImageTk.PhotoImage(imagem)
                l_imagem = Label(frame_detalhes, image=imagem, bg=co1, fg=co4)
                l_imagem.place(x=300, y=10)

                def update():
                        
                    # funcao para escolher imagem
                    global imagem, imagem_string, l_imagem
                        
                    nome = e_nome.get()
                    email = e_email.get()
                    telefone = e_tel.get()
                    sexo = c_sexo.get()
                    data = data_nascimento.get()
                    cpf = e_cpf.get()
                    curso = c_turma.get()
                    imagem = imagem_string

                    lista = [nome, email, telefone, sexo, imagem, data, cpf, curso, valor_id]

                    #verificando caso algum campo esteja vazio ou não
                    for i in lista:
                        if i=='':
                            messagebox.showerror('Erro', 'Preencha todos os campos')
                            return
                            
                    # atualizando os dados no banco de dados
                    atualizar_alunos(lista)

                    # mostrando a mensagem de sucesso
                    messagebox.showinfo('Sucesso', 'Os dados foram atualizados com sucesso')
                        
                    #limpando os campos de entrada 
                    e_nome.delete(0, END)
                    e_email.delete(0, END)
                    c_sexo.delete(0, END)
                    data_nascimento.delete(0, END)
                    e_cpf.delete(0, END)
                    c_turma.delete(0, END)

                    # monstrando os valores na tabela
                    mostrar_alunos()

                    # destruindo botao apos salvar
                    botao_update.destroy()



                botao_update = Button(frame_detalhes,command=update ,anchor=CENTER, text="Salvar atualização".upper(), width=9, overrelief=RIDGE, font=('ivy 7 bold'), bg=co3, fg=co1)
                botao_update.place(x=727, y=130)
            
            except IndentationError:
                messagebox.showerror('Erro', 'Seleciona um dos alunos na tabela')


        #funcao deletar aluno
        def delete_aluno():
            try:
                tree_itens = tree.focus()
                tree_dicionario = tree.item(tree_itens)
                tree_lista = tree_dicionario['values']

                valor_id = tree_lista[0]

                #Deletar os dados no banco de dados
                deletar_aluno([valor_id])

                # mostrando a mensagem de sucesso
                messagebox.showinfo("Sucesso", 'Aluno deletado com sucesso')

                #mostrando os valores na tabela 
                mostrar_alunos()

            except IndexError:
                messagebox.showerror('Erro', 'Seleciona um aluno na tabela')




    # criando campos de entrada
        l_nome = Label(frame_detalhes, text="Nome *", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
        l_nome.place(x=4, y=10)
        e_nome = Entry(frame_detalhes, width=45, justify='left', relief='solid')
        e_nome.place(x=7, y=40)
        
        l_email = Label(frame_detalhes, text="Email *", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
        l_email.place(x=4, y=70)
        e_email = Entry(frame_detalhes, width=45, justify='left', relief='solid')
        e_email.place(x=7, y=100)    
        
        l_tel = Label(frame_detalhes, text="Telefone *", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
        l_tel.place(x=4, y=130)
        e_tel = Entry(frame_detalhes, width=20, justify='left', relief='solid')
        e_tel.place(x=7, y=160)
        
        # Seleção de Genero        
        l_sexo = Label(frame_detalhes, text="Gênero *", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
        l_sexo.place(x=190, y=130)
        c_sexo = ttk.Combobox(frame_detalhes, width=12, font=('Ivy 8 bold'))
        c_sexo['values'] = ('Masculino', 'Feminino', 'Outro')
        c_sexo.place(x=190, y=160)
        
        l_data_nascimento = Label(frame_detalhes, text="Data de Nascimento *", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
        l_data_nascimento.place(x=446, y=10)
        data_nascimento = DateEntry(frame_detalhes, widht=18, background='darkblue', foreground='white', borderwidth=2, year=2024)
        data_nascimento.place(x=450, y=40)        
        
        l_cpf = Label(frame_detalhes, text="CPF *", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
        l_cpf.place(x=446, y=70)
        e_cpf = Entry(frame_detalhes, width=20, justify='left', relief='solid')
        e_cpf.place(x=450, y=100)    
        
        # Pegando as Turmas
        turmas = ver_cursos()
        turma = []
        
        for i in turmas:
            turma.append(i[1])
            
        l_turma = Label(frame_detalhes, text="Turma *", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
        l_turma.place(x=446, y=130)    
        c_turma = ttk.Combobox(frame_detalhes, width=20, font=('Ivy 8 bold'))
        c_turma['values'] = (turma)
        c_turma.place(x=450, y=160)


        # funcao para escolher imagem
        global imagem, imagem_string, l_imagem

        def escolher_imagem():
            global imagem, imagem_string, l_imagem

            imagem = fd.askopenfilename()
            imagem_string = imagem
   

            imagem = Image.open(imagem)
            imagem = imagem.resize((130,130))
            imagem = ImageTk.PhotoImage(imagem)
            l_imagem = Label(frame_detalhes, image=imagem, bg=co1, fg=co4)
            l_imagem.place(x=300, y=10)

            botao_carregar['text'] = 'Trocar de foto'

        botao_carregar = Button(frame_detalhes, command=escolher_imagem, text="Carregar Foto".upper(), width=20, compound=CENTER, anchor=CENTER, overrelief=RIDGE, font=('Ivy 7'), bg=co1, fg=co0)
        botao_carregar.place(x=300, y=160)

        # linha separatoria -------------------------------------------------
        l_linha = Label(frame_detalhes, relief=GROOVE, text='h', width=1, height=100, anchor=NW, font=('Ivy 1'), bg=co0, fg=co0)
        l_linha.place(x=610, y=10)
        l_linha = Label(frame_detalhes, relief=GROOVE, text='h', width=1, height=100, anchor=NW, font=('Ivy 1'), bg=co1, fg=co0)
        l_linha.place(x=608, y=10)

        # Procurar aluno ----------------------------------------------------

        l_nome = Label(frame_detalhes, text="Procurar Aluno [ Entra o nome ]", heigh=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
        l_nome.place(x=627, y=10)
        e_nome_procurar = Entry(frame_detalhes, width=17, justify='center', relief="solid", font=('Ivy 10'))
        e_nome_procurar.place(x=630, y=35)

        botao_procurar = Button(frame_detalhes, anchor=CENTER, text="Procurar", width=9, overrelief=RIDGE, font=('ivy 7 bold'), bg=co1, fg=co0)
        botao_procurar.place(x=757, y=35)

        # Botoes --------------------------------------

        botao_salvar = Button(frame_detalhes,command=novo_aluno ,anchor=CENTER, text="Salvar".upper(), width=9, overrelief=RIDGE, font=('ivy 7 bold'), bg=co3, fg=co1)
        botao_salvar.place(x=627, y=110)

        botao_atualizar = Button(frame_detalhes, command=update_aluno,anchor=CENTER, text="Atualizar".upper(), width=9, overrelief=RIDGE, font=('ivy 7 bold'),bg=co6, fg=co1)
        botao_atualizar.place(x=627, y=135)

        botao_deletar = Button(frame_detalhes, command=delete_aluno,anchor=CENTER, text="Deletar".upper(), width=9, overrelief=RIDGE, font=('ivy 7 bold'), bg=co7, fg=co1)
        botao_deletar.place(x=627, y=160)

        botao_ver = Button(frame_detalhes, anchor=CENTER, text="Ver".upper(), width=9, overrelief=RIDGE, font=('ivy 7 bold'), bg=co1, fg=co0)
        botao_ver.place(x=727, y=160)
        
        
        def mostrar_alunos():
            app_nome = Label(frame_tabela, text="Tabela de estudantes", height=1,pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
            app_nome.grid(row=0, column=0, padx=0, pady=10, sticky=NSEW)
            
            
            list_header = ['id','Nome','email',  'Telefone','gênero', 'imagem', 'Data', 'CPF','Curso']
            
            df_list = ver_alunos()
                
            global tree_aluno
                
            tree_aluno = ttk.Treeview(frame_tabela, selectmode="extended",columns=list_header, show="headings")
            
            
            vsb = ttk.Scrollbar(frame_tabela, orient="vertical", command=tree_aluno.yview)
            
            hsb = ttk.Scrollbar(frame_tabela, orient="horizontal", command=tree_aluno.xview)
            
            tree_aluno.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
            tree_aluno.grid(column=0, row=1, sticky='nsew')
            vsb.grid(column=1, row=1, sticky='ns')
            hsb.grid(column=0, row=2, sticky='ew')
            frame_tabela.grid_rowconfigure(0, weight=12)
                
            hd=["nw","nw","nw","center","center","center","center","center","center"]
            h=[40,150,150,70,70,70,80,80,100]
            n=0
                
            for col in list_header:
                tree_aluno.heading(col, text=col.title(), anchor=NW)
                
                tree_aluno.column(col, width=h[n],anchor=hd[n])
                    
                n+=1
                    
            for item in df_list:
                tree_aluno.insert('', 'end', values=item)
                    
        mostrar_alunos()




        



#funcao para adicionar Cursos e Turmas
def adicionar():
    # Criando frames para tabela
    frame_tabela_curso = Frame(frame_tabela, width=300, height=200, bg=co1)
    frame_tabela_curso.grid(row=0, column=0, pady=0, padx=10, sticky=NSEW)

    frame_tabela_linha = Frame(frame_tabela, width=30, height=200, bg=co1)
    frame_tabela_linha.grid(row=0, column=1, pady=0, padx=10, sticky=NSEW)

    frame_tabela_turma = Frame(frame_tabela, width=300, height=200, bg=co1)
    frame_tabela_turma.grid(row=0, column=2, pady=0, padx=10, sticky=NSEW)
    
    # Detalhes do Curso ----------------------------------------------------
    
    #funcao novo curso
    def novo_curso():
        nome = e_nome_curso.get()
        duracao = e_duracao.get()
        preco = e_preco.get()

        lista = [nome, duracao, preco]

        # Verificando se os valores estao vazios ou nao
        for i in lista:
            if i=="":
                messagebox.showerror('Erro', 'Preencha todos os campos')
                return
            
        # inserindo os dados
        criar_curso(lista)

        # mostrando mensagem de sucesso
        messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso')
        
        e_nome_curso.delete(0, END)
        e_duracao.delete(0, END)
        e_preco.delete(0, END)

        #mostrando os valores na tabela
        mostrar_cursos()


     #funcao atualizar curso
    
    #funcao atualizr curso
    def update_curso():
        try:
            tree_itens = tree_curso.focus()
            tree_dicionario = tree_curso.item(tree_itens)
            tree_lista = tree_dicionario['values']

            valor_id = tree_lista[0]

            #inserindo os valores nas entries
            nome = e_nome_curso.insert(0, tree_lista[1])
            duracao = e_duracao.insert(0, tree_lista[2])
            preco = e_preco.insert(0, tree_lista[3])
            
            #funcao atualizar
            def update():

                e_nome_curso.get()
                e_duracao.get()
                e_preco.get()
                lista = [nome, duracao, preco, valor_id]
                
                # Verificando se os valores estao vazios ou nao
                for i in lista:
                    if i=="":
                        messagebox.showerror('Erro', 'Preencha todos os campos')
                        return
                    
                # inserindo os dados
                atualizar_cursos(lista)
                # mostrando mensagem de sucesso
                messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso')
                
                e_nome_curso.delete(0, END)
                e_duracao.delete(0, END)
                e_preco.delete(0, END)
                
                #mostrando os valores na tabela
                mostrar_cursos()

                #destruindo botao salvar apos salvar os dados
                botao_salvar.destroy()
                
            botao_salvar = Button(frame_detalhes, command=update ,anchor=CENTER, text='Salvar atualização'.upper(), overrelief=RIDGE, font=('Ivy 7 bold'), bg=co3, fg=co1)
            botao_salvar.place(x=227, y=130)
            
        except IndexError:
                messagebox.showerror('Erro', 'Seleciona um dos cursos na tabela')

    #funcao deletar curso
    def delete_curso():
        try:
            tree_itens = tree_curso.focus()
            tree_dicionario = tree_curso.item(tree_itens)
            tree_lista = tree_dicionario['values']

            valor_id = tree_lista[0]

            #deletar os dados no banco de dados
            deletar_curso([valor_id])
            
            messagebox.showinfo('Sucesso', 'Os dados foram deletados com sucesso')
            mostrar_cursos()


        except IndexError:
                messagebox.showerror('Erro', 'Seleciona um dos cursos na tabela')
            




    l_nome = Label(frame_detalhes, text="Nome do curso *", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_nome.place(x=4, y=10)
    e_nome_curso = Entry(frame_detalhes, width=35, justify='left', relief='solid')
    e_nome_curso.place(x=7, y=40)

    l_duracao = Label(frame_detalhes, text="Duração *", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_duracao.place(x=4, y=70)
    e_duracao = Entry(frame_detalhes, width=20, justify='left', relief="solid")
    e_duracao.place(x=7, y=100)

    l_preco = Label(frame_detalhes, text="Preço *", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_preco.place(x=4, y=130)
    e_preco = Entry(frame_detalhes, width=10, justify='left', relief="solid")
    e_preco.place(x=7, y=160)

    botao_carregar = Button(frame_detalhes, command=novo_curso ,anchor=CENTER, text='Salvar'.upper(), width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co3, fg=co1)
    botao_carregar.place(x=107, y=160)
    
    botao_atualizar = Button(frame_detalhes, command=update_curso ,anchor=CENTER, text="Atualizar".upper(), width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co6, fg=co1)
    botao_atualizar.place(x=187, y=160)

    botao_deletar = Button(frame_detalhes, command=delete_curso,anchor=CENTER, text="Deletar".upper(), width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co7, fg=co1)
    botao_deletar.place(x=267, y=160)


    # Tabela Cursos
    def mostrar_cursos():
        app_nome = Label(frame_tabela_curso, text="Tabela de Cursos", height=1, pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
        app_nome.grid(row=0, column=0, padx=0, pady=10, sticky=NSEW)

        list_header = ['ID', 'Curso', 'Duração', 'Preço']

        df_list = ver_cursos()

        global tree_curso

        tree_curso = ttk.Treeview(frame_tabela_curso, selectmode='extended', columns=list_header, show="headings")

        vsb = ttk.Scrollbar(frame_tabela_curso, orient="vertical", command=tree_curso.yview)

        hsb = ttk.Scrollbar(frame_tabela_curso, orient="horizontal", command=tree_curso.xview)

        tree_curso.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        tree_curso.grid(column=0, row=1, sticky='nsew')
        vsb.grid(column=1, row=1, sticky='ns')
        hsb.grid(column=0, row=2, sticky='ew')
        frame_tabela_curso.grid_rowconfigure(0, weight=12)

        hd=["nw", "nw", "e", "e"]
        h=[30,150,80,60]
        n=0

        for col in list_header:
            tree_curso.heading(col, text=col.title(), anchor=NW)
            tree_curso.column(col, width=h[n], anchor=hd[n])

            n+=1
        
        for item in df_list:
            tree_curso.insert('', 'end', values=item)

    mostrar_cursos()
    
    # linha separatoria -------------------------------------------------
    l_linha = Label(frame_detalhes, relief=GROOVE, text='h', width=1, height=100, anchor=NW, font=('Ivy 1'), bg=co0, fg=co0)
    l_linha.place(x=374, y=10)
    l_linha = Label(frame_detalhes, relief=GROOVE, text='h', width=1, height=100, anchor=NW, font=('Ivy 1'), bg=co1, fg=co0)
    l_linha.place(x=372, y=10)
    
    # linha separatoria  tabela -----------------------------------------
    l_linha = Label(frame_tabela_linha, relief=GROOVE, text='h', width=1, height=140, anchor=NW, font=('Ivy 1'), bg=co0, fg=co0)
    l_linha.place(x=6, y=10)
    l_linha = Label(frame_tabela_linha, relief=GROOVE, text='h', width=1, height=140, anchor=NW, font=('Ivy 1'), bg=co1, fg=co0)
    l_linha.place(x=4, y=10)


    # Detalhes da Turma -------------------------------------------------
    
    
    #nova turma --------------------------------------------
    def novo_turma():
        nome = e_nome_turma.get()
        curso = c_curso.get()
        data = data_inicio.get()

        lista = [nome, curso, data]
        
        # Verificando se os valores estao vazios ou nao
        
        for i in lista:
            if i=="":
                messagebox.showerror('Erro', 'Preencha todos os campos')
                return
            
        # inserindo os dados
        criar_turma(lista)
        
        # mostrando mensagem de sucesso
        messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso')
        
        e_nome_turma.delete(0, END)
        c_curso.delete(0, END)
        data_inicio.delete(0, END)

        #mostrando os valores na tabela
        mostrar_turmas()

        #funcao atualizr turma
    def update_turma():
        try:
            tree_itens = tree_turma.focus()
            tree_dicionario = tree_turma.item(tree_itens)
            tree_lista = tree_dicionario['values']

            valor_id = tree_lista[0]

            #inserindo os valores nas entries
            e_nome_turma.insert(0, tree_lista[1])
            c_curso.insert(0, tree_lista[2])
            data_inicio.insert(0, tree_lista[3])
            
            #funcao atualizar
            def update():

                nome = e_nome_turma.get()
                curso = c_curso.get()
                data =  data_inicio.get()
                lista = [nome, curso, data, valor_id]
                
                # Verificando se os valores estao vazios ou nao
                for i in lista:
                    if i=="":
                        messagebox.showerror('Erro', 'Preencha todos os campos')
                        return
                    
                # inserindo os dados
                atualizar_turma(lista)
                # mostrando mensagem de sucesso
                messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso')
                
                e_nome_turma.delete(0, END)
                c_curso.delete(0, END)
                data_inicio.delete(0, END)
                
                #mostrando os valores na tabela
                mostrar_turmas()

                #destruindo botao salvar apos salvar os dados
                botao_salvar.destroy()
                
            botao_salvar = Button(frame_detalhes, command=update ,anchor=CENTER, text='Salvar atualização'.upper(), overrelief=RIDGE, font=('Ivy 7 bold'), bg=co3, fg=co1)
            botao_salvar.place(x=407, y=130)
            
        except IndexError:
                messagebox.showerror('Erro', 'Seleciona um dos cursos na tabela')

        #funcao deletar curso
    
    def delete_turma():
        try:
            tree_itens = tree_turma.focus()
            tree_dicionario = tree_turma.item(tree_itens)
            tree_lista = tree_dicionario['values']

            valor_id = tree_lista[0]

            #deletar os dados no banco de dados
            deletar_turma([valor_id])
            
            messagebox.showinfo('Sucesso', 'Os dados foram deletados com sucesso')
            mostrar_turmas()


        except IndexError:
                messagebox.showerror('Erro', 'Seleciona um dos cursos na tabela')
 
    
    
    
    l_nome = Label(frame_detalhes, text="Nome da Turma *", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_nome.place(x=404, y=10)
    e_nome_turma = Entry(frame_detalhes, width=35, justify='left', relief="solid")
    e_nome_turma.place(x=407, y=40)

    l_turma = Label(frame_detalhes, text="Curso *", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_turma.place(x=404, y=70)

    # Pegando os cursos
    cursos = ver_cursos()
    curso = []

    for i in cursos:
        curso.append(i[1])
    
    c_curso = ttk.Combobox(frame_detalhes, width=20, font=('Ivy 8 bold'))
    c_curso['values'] = (curso)
    c_curso.place(x=407, y=100)

    l_data_inicio = Label(frame_detalhes, text="Data de inicio *", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_data_inicio.place(x=406, y=130)
    data_inicio = DateEntry(frame_detalhes, widht=10, background='darkblue', foreground='white', borderwidth=2, year=2024)
    data_inicio.place(x=407, y=160)
    
    botao_carregar = Button(frame_detalhes, command=novo_turma ,anchor=CENTER, text='Salvar'.upper(), width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co3, fg=co1)
    botao_carregar.place(x=507, y=160)
    
    botao_atualizar = Button(frame_detalhes, command=update_turma,anchor=CENTER, text="Atualizar".upper(), width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co6, fg=co1)
    botao_atualizar.place(x=587, y=160)

    botao_deletar = Button(frame_detalhes, command=delete_turma ,anchor=CENTER, text="Deletar".upper(), width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co7, fg=co1)
    botao_deletar.place(x=667, y=160)


        # Tabela Turmas
    def mostrar_turmas():
        app_nome = Label(frame_tabela_turma, text="Tabela de Turmas", height=1, pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
        app_nome.grid(row=0, column=0, padx=0, pady=10, sticky=NSEW)

        list_header = ['ID', 'Nome da Turma', 'Curso', 'Início']

        df_list = ver_turmas()

        global tree_turma

        tree_turma = ttk.Treeview(frame_tabela_turma, selectmode='extended', columns=list_header, show="headings")

        vsb = ttk.Scrollbar(frame_tabela_turma, orient="vertical", command=tree_turma.yview)

        hsb = ttk.Scrollbar(frame_tabela_turma, orient="horizontal", command=tree_turma.xview)

        tree_turma.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        tree_turma.grid(column=0, row=1, sticky='nsew')
        vsb.grid(column=1, row=1, sticky='ns')
        hsb.grid(column=0, row=2, sticky='ew')
        frame_tabela_turma.grid_rowconfigure(0, weight=12)

        hd=["nw", "nw", "e", "e"]
        h=[30,130,150,80]
        n=0

        for col in list_header:
            tree_turma.heading(col, text=col.title(), anchor=NW)
            tree_turma.column(col, width=h[n], anchor=hd[n])

            n+=1
        
        for item in df_list:
            tree_turma.insert('', 'end', values=item)

    mostrar_turmas()





    # Funcao para salvar
    def salvar():
        print('Salvar')



# Funcao de controle -------------------------

def control(i):
    # cadastro de aluno
    if i == 'cadastro':
        for widget in frame_detalhes.winfo_children():
            widget.destroy()
        
        for widget in frame_tabela.winfo_children():
            widget.destroy()

        # chamando a funcao alunos
        alunos()

    if i == 'adicionar':
        for widget in frame_detalhes.winfo_children():
            widget.destroy()

        for widget in frame_tabela.winfo_children():
            widget.destroy()
        
        # chamando funcao adicionar
        adicionar()

    if i == 'salvar':
        for widget in frame_detalhes.winfo_children():
            widget.destroy()

        for widget in frame_tabela.winfo_children():
            widget.destroy()

        # chamando a funcao salvar
        salvar()




# criando botoes

app_img_cadastro = Image.open('adicionar.png')
app_img_cadastro = app_img_cadastro.resize((18,18))
app_img_cadastro = ImageTk.PhotoImage(app_img_cadastro)
app_cadastro = Button(frame_dados, command=lambda:control('cadastro'), image=app_img_cadastro, text="Cadastro", width=100, compound=LEFT, overrelief=RIDGE, font=('Ivy 11'), bg=co1, fg=co0)
app_cadastro.place(x=10, y=30)

app_img_adicionar = Image.open('adicionar.png')
app_img_adicionar = app_img_adicionar.resize((18,18))
app_img_adicionar = ImageTk.PhotoImage(app_img_adicionar)
app_adicionar = Button(frame_dados, command=lambda:control('adicionar'), image=app_img_adicionar, text="Adicionar", width=100, compound=LEFT, overrelief=RIDGE, font=('Ivy 11'), bg=co1, fg=co0)
app_adicionar.place(x=123, y=30)

app_img_salvar = Image.open('salvar.png')
app_img_salvar = app_img_salvar.resize((18,18))
app_img_salvar = ImageTk.PhotoImage(app_img_salvar)
app_salvar = Button(frame_dados, command=lambda:control('salvar'), image=app_img_salvar, text="Salvar", width=100, compound=LEFT, overrelief=RIDGE, font=('Ivy 11'), bg=co1, fg=co0)
app_salvar.place(x=236, y=30)



alunos()
janela.mainloop()
