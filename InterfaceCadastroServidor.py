# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import *
from tkinter import messagebox

import DAOServidor


def inserirUsuario(txip, txdescricao, root):
    retorno = DAOServidor.DAOServidor.insere_servidor(txip, txdescricao)
    if retorno == 1:
        tk.messagebox.showinfo(parent=root, title="Cadastro", message="Salvo com sucesso")
    else:
        tk.messagebox.showinfo(parent=root, title="Cadastro", message="Servidor já cadastrado")


class InterfaceCadastroServidor:
    def exibeInterface(master):
        root = Toplevel(master)
        # *********************************************************************************************
        # Inicio Containers

        root.geometry("500x350")
        root.title("Cadastrar Servidores")

        root.fontePadrao = ("Arial", "12")
        root.primeiroContainer = Frame(root)
        root.primeiroContainer["pady"] = 30
        root.primeiroContainer.pack()

        root.segundoContainer = Frame(root)
        root.segundoContainer["pady"] = 20
        root.segundoContainer["padx"] = 100
        root.segundoContainer.pack()

        root.terceiroContainer = Frame(root)
        root.terceiroContainer["pady"] = 20
        root.terceiroContainer["padx"] = 100
        root.terceiroContainer.pack()

        root.sextoContainer = Frame(root)
        root.sextoContainer["pady"] = 30
        root.sextoContainer.pack()

        # Fim Containers

        # *********************************************************************************************

        # Título
        root.titulo = Label(root.primeiroContainer, text="Cadastro de servidores")
        root.titulo["font"] = ("Arial", "15", "bold")
        root.titulo.pack()

        # IP
        root.ipLabel = Label(root.segundoContainer, text="             IP   ", font=root.fontePadrao)
        root.ipLabel.pack(side=LEFT)

        root.ip = Entry(root.segundoContainer)
        root.ip["width"] = 30
        root.ip["font"] = root.fontePadrao
        root.ip.pack()

        # Descricao
        root.descricaoLabel = Label(root.terceiroContainer, text="Descrição   ", font=root.fontePadrao)
        root.descricaoLabel.pack(side=LEFT)

        root.descricao = Entry(root.terceiroContainer)
        root.descricao["width"] = 30
        root.descricao["font"] = root.fontePadrao
        root.descricao.pack()

        # botão cancelar
        root.cancelar = Button(root.sextoContainer)
        root.cancelar["text"] = "Cancelar"
        root.cancelar["width"] = 12
        root.cancelar["command"] = lambda: root.destroy()
        root.cancelar.pack(side=LEFT, padx=10)

        # botão salvar
        root.salvar = Button(root.sextoContainer)
        root.salvar["text"] = "Salvar"
        root.salvar["width"] = 12
        root.salvar["command"] = lambda: inserirUsuario(root.ip.get(), root.descricao.get(), root)
        root.salvar.pack(padx=10)

        root.mainloop()


if __name__ == '__main__':
    InterfaceCadastroServidor.exibeInterface()
