# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import *
from tkinter import messagebox

import DAOLocalizacoes


def cadastrarLocalizacoes(nome, root):
    retorno = DAOLocalizacoes.DAOLocalizacoes.insere_localizacao(nome)
    if retorno == 1:
        tk.messagebox.showinfo(parent=root, title="Cadastro", message="Salvo com sucesso")
    else:
        tk.messagebox.showinfo(parent=root, title="Cadastro", message="Localização já cadastrada")


class InterfaceCadastroLocalizacoes:
    def exibeInterface(master):
        root = Toplevel(master)
        # *********************************************************************************************
        # Inicio Containers

        root.geometry("500x250")
        root.title("Cadastrar localizações")

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
        root.titulo = Label(root.primeiroContainer, text="Cadastro de Localizações")
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

        # botão salvar
        root.salvar = Button(root.sextoContainer)
        root.salvar["text"] = "Salvar"
        root.salvar["width"] = 12
        root.salvar["command"] = lambda: cadastrarLocalizacoes(root.nome.get(), root)
        root.salvar.pack(padx=10)

        root.mainloop()


if __name__ == '__main__':
    InterfaceCadastroLocalizacoes.exibeInterface()
