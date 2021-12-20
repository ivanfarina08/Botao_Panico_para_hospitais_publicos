# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import *
from tkinter import messagebox

import DAOServidor


def alterarUsuario(txipAntigo, txip, txdescricao, root):
    retorno = DAOServidor.DAOServidor.altera_servidor(txipAntigo, txip, txdescricao)
    if retorno == 1:
        tk.messagebox.showinfo(parent=root, title="Alterar", message="Alterado com sucesso")
    else:
        tk.messagebox.showinfo(parent=root, title="Alterar", message="Servidor não encontrado")


class InterfaceAlterarServidor:
    def exibeInterface(master):
        root = Toplevel(master)
        # *********************************************************************************************
        # Inicio Containers

        root.geometry("600x400")
        root.title("Alterar Servidores")

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

        root.quartoContainer = Frame(root)
        root.quartoContainer["pady"] = 20
        root.quartoContainer["padx"] = 100
        root.quartoContainer.pack()

        root.quintoContainer = Frame(root)
        root.quintoContainer["pady"] = 20
        root.quintoContainer["padx"] = 100
        root.quintoContainer.pack()

        root.sextoContainer = Frame(root)
        root.sextoContainer["pady"] = 20
        root.sextoContainer["padx"] = 100
        root.sextoContainer.pack()

        root.setimoContainer = Frame(root)
        root.setimoContainer["pady"] = 30
        root.setimoContainer.pack()

        # Fim Containers

        # *********************************************************************************************

        # Título
        root.titulo = Label(root.primeiroContainer, text="Alterar servidores")
        root.titulo["font"] = ("Arial", "18", "bold")
        root.titulo.pack()

        # IP Antigo
        root.ipAntigoLabel = Label(root.terceiroContainer, text="            IP antigo   ", font=root.fontePadrao)
        root.ipAntigoLabel.pack(side=LEFT)

        root.ipAntigo = Entry(root.terceiroContainer)
        root.ipAntigo["width"] = 30
        root.ipAntigo["font"] = root.fontePadrao
        root.ipAntigo.pack()

        # IP novo
        root.ipLabel = Label(root.quintoContainer, text="             IP novo   ", font=root.fontePadrao)
        root.ipLabel.pack(side=LEFT)

        root.ip = Entry(root.quintoContainer)
        root.ip["width"] = 30
        root.ip["font"] = root.fontePadrao
        root.ip.pack()

        # Descricao novo
        root.descricaoLabel = Label(root.sextoContainer, text="Descrição nova   ", font=root.fontePadrao)
        root.descricaoLabel.pack(side=LEFT)

        root.descricao = Entry(root.sextoContainer)
        root.descricao["width"] = 30
        root.descricao["font"] = root.fontePadrao
        root.descricao.pack()

        # botão cancelar
        root.cancelar = Button(root.setimoContainer)
        root.cancelar["text"] = "Cancelar"
        root.cancelar["width"] = 12
        root.cancelar["command"] = lambda: root.destroy()
        root.cancelar.pack(side=LEFT, padx=10)

        # botão alterar
        root.alterar = Button(root.setimoContainer)
        root.alterar["text"] = "Alterar"
        root.alterar["width"] = 12
        root.alterar["command"] = lambda: alterarUsuario(root.ipAntigo.get(), root.ip.get(), root.descricao.get(), root)
        root.alterar.pack(padx=10)

        root.mainloop()


if __name__ == '__main__':
    InterfaceAlterarServidor.exibeInterface()
