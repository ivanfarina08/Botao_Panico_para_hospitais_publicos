# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import *
from tkinter import messagebox

import DAOLocalizacaoAtual


def alterarLocalizacaoAtual(localizacao):
    DAOLocalizacaoAtual.DAOLocalizacaoAtual.altera_localizacao(localizacao)
    tk.messagebox.showinfo("Alterar", "Alterado com sucesso")


class InterfaceAlteraLocalizacaoAtual:
    def exibeInterface(master=None):
        root = Tk()
        # *********************************************************************************************
        # Inicio Containers

        root.geometry("500x250")
        root.title("Localização atual")

        root.fontePadrao = ("Arial", "12")
        root.primeiroContainer = Frame(master)
        root.primeiroContainer["pady"] = 30
        root.primeiroContainer.pack()

        root.segundoContainer = Frame(master)
        root.segundoContainer["pady"] = 20
        root.segundoContainer["padx"] = 100
        root.segundoContainer.pack()

        root.sextoContainer = Frame(master)
        root.sextoContainer["pady"] = 30
        root.sextoContainer.pack()

        # Fim Containers

        # *********************************************************************************************

        # Título
        root.titulo = Label(root.primeiroContainer, text="Alterar localização atual")
        root.titulo["font"] = ("Arial", "15", "bold")
        root.titulo.pack()

        # nome
        root.nomeLabel = Label(root.segundoContainer, text="Nome   ", font=root.fontePadrao)
        root.nomeLabel.pack(side=LEFT)

        root.nome = Entry(root.segundoContainer)
        root.nome["width"] = 30
        root.nome["font"] = root.fontePadrao
        root.nome.pack()

        # botão cancelar
        root.cancelar = Button(root.sextoContainer)
        root.cancelar["text"] = "Cancelar"
        root.cancelar["width"] = 12
        root.cancelar["command"] = quit
        root.cancelar.pack(side=LEFT, padx=10)

        # botão alterar
        root.alterar = Button(root.sextoContainer)
        root.alterar["text"] = "Alterar"
        root.alterar["width"] = 12
        root.alterar["command"] = lambda: alterarLocalizacaoAtual(root.nome.get())
        root.alterar.pack(padx=10)

        root.mainloop()


if __name__ == '__main__':
    InterfaceAlteraLocalizacaoAtual.exibeInterface()
