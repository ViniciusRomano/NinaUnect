# -*- coding: utf-8 -*-
try:
    from Tkinter import *
    from ttk import *
except ImportError:  # Python 3
    from tkinter import *
    from tkinter.ttk import *

from timeNow import timeNow  # classe para retornar o horário e data online
import tkMessageBox
import requests
from bd_nina import *
from Permanencia import *

from requests.exceptions import ConnectionError

class App(Frame):


    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.bd = DB()
        self.bd.createTableFuncionario()
        self.bd.createTablePermanencia()
        self.CreateUI()
        self.grid(sticky=(N, S, W, E))
        self.todas_permanencias = [] # lista de alunos
        if(self.internet_verify()):
            self.msg_error()
            Frame.quit()

    def msg_error(self):
        tkMessageBox.showerror(
            "Connection Error", "Sem acesso a internet. Por favor, verifique sua conexão.")

    def msg_errorRa(self):
        tkMessageBox.showerror(
            "RA inválido", "RA incorreto ou não cadastrado no sistema")

    def msg_insert(self):
        tkMessageBox.showinfo(
            "Permanência realizada", "Permanência efetuada com sucesso.")

    def internet_verify(self):
        try:
            _ = requests.get('http://www.google.com/', timeout=5)
            if(_.status_code == 200):
                return False
        except requests.ConnectionError:
            print("No internet connection available.")
        return True

    def reload(self):
        self.treeview.delete(*self.treeview.get_children())  # limpa a tabela
        for perm in self.todas_permanencias:  # insere as informacoes que estao na lista
            self.treeview.insert('', 'end', text=perm.ra, values=(perm.hEntrada, perm.hSaida, perm.status))

    def insert(self, event=None):
        # procura pra ver se o funcionario esta na sala.
        number_list = -1
        found = False
        for perm in self.todas_permanencias:
            number_list = number_list + 1
            if (perm.ra == self.e.get()) and (perm.hSaida == ''):
                found = True
                break

        if(found):
            # modificando status e horario de saida
            try:
                self.todas_permanencias[number_list].hSaida = timeNow().getTime()
                self.todas_permanencias[number_list].status = 'OK'

                DB.insertPermanencia(self.bd,self.todas_permanencias[number_list])

                self.msg_insert()
                self.reload()

            except ConnectionError as err:
                self.msg_error()
        else:
            # criando uma permanência
            try:
                p = Permanencia(self.e.get(), timeNow().getDate(), timeNow().getTime(), '', 'Pendente', '')
                if self.bd.selectFuncionario(p.ra) == None:
                    raise ValueError('no RA')
                self.todas_permanencias.append(p)
                self.msg_insert()
                self.reload()
            except (ConnectionError, ValueError) as err:
                if 'no RA' in err:
                    self.msg_errorRa()
                else:
                    self.msg_error()

    def CreateUI(self):
        tv = Treeview(self, height=20)
        tv['columns'] = ('starttime', 'endtime', 'status')
        tv.heading("#0", text='R.A', anchor='c')
        tv.column("#0", anchor="c")
        tv.heading('starttime', text='Start Time')
        tv.column('starttime', anchor='center', width=100)
        tv.heading('endtime', text='End Time')
        tv.column('endtime', anchor='center', width=100)
        tv.heading('status', text='Status')
        tv.column('status', anchor='center', width=100)
        tv.grid(row=1, column=0, columnspan=5, padx=5, pady=5)
        self.e = Entry(self)
        self.e.grid(row=0, column=2, pady=20)
        self.e.bind('<Return>', self.insert)
        self.e.focus_set()
        label = Label(self, text="Insira o RA", font="bold 10")
        label.grid(row=0, column=1)
        bt = Button(self, text='Ok', command=self.insert)
        bt.grid(row=0, column=3)
        self.treeview = tv


def main():
    root = Tk()
    root.wm_title('Nina Unect')
    App(root)
    root.mainloop()

if __name__ == '__main__':
    main()
