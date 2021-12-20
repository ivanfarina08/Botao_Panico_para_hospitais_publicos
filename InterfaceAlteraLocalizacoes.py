# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import *
from tkinter import messagebox

import DAOLocalizacoes


def alterarLocalizacoes(nomeAntigo, nomeNovo, root):
    retorno = DAOLocalizacoes.DAOLocalizacoes.altera_localizacao(nomeAntigo, nomeNovo)
    if retorno == 1:
        tk.messagebox.showinfo(parent=root, title="Alterar", message="Alterado com sucesso")
    else:
        tk.messagebox.showinfo(parent=root, title="Alterar", message="Localização não encontrada")


class InterfaceAlteraLocalizacoes:
    def exibeInterface(master):
        root = Toplevel(master)
        # *********************************************************************************************
        # Inicio Containers

        root.geometry("500x330")
        root.title("Alterar localizações")

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
        root.titulo = Label(root.primeiroContainer, text="Alterar Localizações")
        root.titulo["font"] = ("Arial", "15", "bold")
        root.titulo.pack()

        # nome antigo
        root.nomeAntigoLabel = Label(root.segundoContainer, text="Nome antigo   ", font=root.fontePadrao)
        root.nomeAntigoLabel.pack(side=LEFT)

        root.nomeAntigo = Entry(root.segundoContainer)
        root.nomeAntigo["width"] = 30
        root.nomeAntigo["font"] = root.fontePadrao
        root.nomeAntigo.pack()

        # nome novo
        root.nomeNovoLabel = Label(root.terceiroContainer, text="  Nome novo   ", font=root.fontePadrao)
        root.nomeNovoLabel.pack(side=LEFT)

        root.nomeNovo = Entry(root.terceiroContainer)
        root.nomeNovo["width"] = 30
        root.nomeNovo["font"] = root.fontePadrao
        root.nomeNovo.pack()

        # botão cancelar
        root.cancelar = Button(root.sextoContainer)
        root.cancelar["text"] = "Cancelar"
        root.cancelar["width"] = 12
        root.cancelar["command"] = lambda: root.destroy()
        root.cancelar.pack(side=LEFT, padx=10)

        # botão alterar
        root.salvar = Button(root.sextoContainer)
        root.salvar["text"] = "Salvar"
        root.salvar["width"] = 12
        root.salvar["command"] = lambda: alterarLocalizacoes(root.nomeAntigo.get(), root.nomeNovo.get(), root)
        root.salvar.pack(padx=10)

        root.mainloop()


if __name__ == '__main__':
    InterfaceAlteraLocalizacoes.exibeInterface()
