# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import *
from tkinter import messagebox

import DAOLocalizacoes


def excluirLocalizacoes(nome, root):
    retorno = DAOLocalizacoes.DAOLocalizacoes.exclui_localizacao(nome)
    if retorno == 1:
        tk.messagebox.showinfo(parent=root, title="Excluir", message="Excluído com sucesso")
    else:
        tk.messagebox.showinfo(parent=root, title="Excluir", message="Localização não encontrada")


class InterfaceExcluiLocalizacoes:
    def exibeInterface(master):
        root = Toplevel(master)
        # *********************************************************************************************
        # Inicio Containers

        root.geometry("500x250")
        root.title("Excluir localizações")

        root.fontePadrao = ("Arial", "12")
        root.primeiroContainer = Frame(root)
        root.primeiroContainer["pady"] = 30
        root.primeiroContainer.pack()

        root.segundoContainer = Frame(root)
        root.segundoContainer["pady"] = 20
        root.segundoContainer["padx"] = 100
        root.segundoContainer.pack()

        root.sextoContainer = Frame(root)
        root.sextoContainer["pady"] = 30
        root.sextoContainer.pack()

        # Fim Containers

        # *********************************************************************************************

        # Título
        root.titulo = Label(root.primeiroContainer, text="Excluir localizações")
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
        root.cancelar["command"] = lambda: root.destroy()
        root.cancelar.pack(side=LEFT, padx=10)

        # botão excluir
        root.excluir = Button(root.sextoContainer)
        root.excluir["text"] = "Excluir"
        root.excluir["width"] = 12
        root.excluir["command"] = lambda: excluirLocalizacoes(root.nome.get(), root)
        root.excluir.pack(padx=10)

        root.mainloop()


if __name__ == '__main__':
    InterfaceExcluiLocalizacoes.exibeInterface()
