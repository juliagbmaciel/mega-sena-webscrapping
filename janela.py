from tkinter import *
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from read import retorna_banco, cursor
from collections import Counter

janela = Tk()

anos = []
num = []


class Aplicacao:
    def __init__(self):
        self.janela = janela
        self.anos = [2022, 2021, 2020, 2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011, 2010, 2009, 2008, 2007,
                     2006, 2005, 2004, 2003, 2002, 2001, 2000, 1999, 1998, 1997, 1996]
        self.tela()
        self.frames()
        self.botoes()
        self.labels()
        self.input()
        self.lista_frame2()
        self.select_list()
        janela.mainloop()

    def tela(self):
        self.janela.title('MEGA SENA')
        self.janela.geometry('700x500')
        self.janela.configure(background='#E4D0D0')
        self.janela.resizable(True, True)
        self.janela.maxsize(width=700, height=700)
        self.janela.minsize(width=700, height=700)

    def frames(self):
        self.frame_0 = Frame(self.janela, bg='#D5B4B4', )
        self.frame_0.place(relx=0.03, rely=0.03, relwidth=0.94, relheight=0.08)

        self.frame_1 = Frame(self.frame_0, bg='#fff')
        self.frame_1.place(relx=0.06, rely=0.25, relwidth=0.09, relheight=0.43)

        self.frame_2 = Frame(self.janela, bg='#D5B4B4')
        self.frame_2.place(relx=0.03, rely=0.13, relwidth=0.94, relheight=0.30)

    def botoes(self):
        self.btBuscar = Button(self.frame_0, text='Buscar', bg='#F5EBEB', command=self.selecionar_opcao)
        self.btBuscar.place(relx=0.18, rely=0.25, relwidth=0.09, relheight=0.43)

    def labels(self):
        fonte = ('Arial', 10, 'bold')
        self.lbAno = Label(self.frame_0, text='ANO', font=fonte, fg='white', background='#867070')
        self.lbAno.place(relx=0.010, rely=0.25, relwidth=0.05, relheight=0.43)

    def input(self):

        self.combobox = ttk.Combobox(self.frame_1,
                                     values=self.anos, state="readonly", width=4, font=('sans-serif', 12))
        print(dict(self.combobox))
        self.combobox.place(rely=10, width=0.7, height=0.9)
        self.combobox.grid(column=0, row=1)
        self.combobox.current(1)

    def selecionar_opcao(self):
        self.ano = self.combobox.get()
        print(self.ano)
        self.listaCli.delete(*self.listaCli.get_children())
        cursor.execute(f"Select * from resultados where ano_sorteio = '{self.ano}'")
        linhas = cursor.fetchall()
        for i in linhas:
            self.listaCli.insert(parent='', index=0, values=i)
        self.graphic()

    def lista_frame2(self):
        self.listaCli = ttk.Treeview(self.frame_2, height=3,
                                     columns=('col1',
                                              'col2',
                                              'col3',
                                              'col4',
                                              'col5',
                                              'col6',
                                              'col7',
                                              'col8',
                                              'col9'))

        self.listaCli.heading('#0', text='')
        self.listaCli.heading('#1', text='ANO')
        self.listaCli.heading('#2', text='SORTEIO')
        self.listaCli.heading('#3', text='NUMERO 1')
        self.listaCli.heading('#4', text='NUMERO 2')
        self.listaCli.heading('#5', text='NUMERO 3')
        self.listaCli.heading('#6', text='NUMERO 4')
        self.listaCli.heading('#7', text='NUMERO 5')
        self.listaCli.heading('#8', text='NUMERO 6')

        self.listaCli.column('#0', width=5)
        self.listaCli.column('#1', width=50)
        self.listaCli.column('#2', width=80)
        self.listaCli.column('#3', width=80)
        self.listaCli.column('#4', width=80)
        self.listaCli.column('#5', width=80)
        self.listaCli.column('#6', width=80)
        self.listaCli.column('#7', width=80)
        self.listaCli.column('#8', width=80)
        self.listaCli.column('#9', width=80)

        self.listaCli.place(relx=0.01, rely=0.08,
                            relwidth=0.96, relheight=0.85)

        # Barra de Rolagem
        self.scroolLista = Scrollbar(self.frame_2, orient='vertical')
        self.listaCli.configure(yscrollcommand=self.scroolLista.set)
        self.scroolLista.place(relx=0.94, rely=0.08, relwidth=0.04, relheight=0.85)

    def qualquer(self):
        print(" ")

    def select_list(self, valor=" "):
        self.listaCli.delete(*self.listaCli.get_children())
        for i in retorna_banco():
            self.listaCli.insert(parent='', index=0, values=i)
            anos.append(i[0])
            num.append(i[2])

    def graphic(self):
        numeros = []
        mais_frequentes = []
        frequencia_num = []
        bar_labels = self.ano
        bar_colors = []
        figura = plt.Figure(figsize=(6, 4), dpi=60)
        ax = figura.add_subplot(111)
        canva = FigureCanvasTkAgg(figura, self.janela)
        canva.get_tk_widget().place(relx=0.03, rely=0.5, relwidth=0.94, relheight=0.3)
        for i in range(len(anos)):
            bar_colors.append("tab:pink")
        cursor.execute(f"SELECT num1, num2, num3, num4, num5, num6 FROM resultados where ano_sorteio = '{self.ano}';")
        linhas = cursor.fetchall()
        for j in range(6):
            for i in linhas:
                numeros.append(i[j])
        c = Counter(numeros)
        frequencia = c.most_common(6)
        for j in range(1):
            for i in frequencia:
                mais_frequentes.append(i[j])
                frequencia_num.append(i[j + 1])
        print(frequencia)
        ax.bar(mais_frequentes, frequencia_num, label=bar_labels, color=bar_colors)

        ax.set_ylabel('Quantas vezes o número apareceu')
        ax.set_title(f'Media dos 10 números mais incidentes do ano de {self.ano}')


jan = Aplicacao()
jan.tela()
