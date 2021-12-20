# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import *
from tkinter import messagebox
from DAOOcorrencias import Ocorrencia


def alterarOcorrencia(txid, txdetalhes, root):
    retorno = Ocorrencia.altera_Ocorrencias(txid, txdetalhes)
    if retorno == 1:
        tk.messagebox.showinfo(parent=root, title="Alterar", message="Alterado com sucesso")
    else:
        tk.messagebox.showinfo(parent=root, title="Alterar", message="Reporte não encontrado")


class InterfaceAlterarReporte:
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
        root.titulo = Label(root.primeiroContainer, text="Alterar Ocorrência")
        root.titulo["font"] = ("Arial", "18", "bold")
        root.titulo.pack()

        # id
        root.id = Label(root.segundoContainer, text="            Id       ", font=root.fontePadrao)
        root.id.pack(side=LEFT)

        root.id = Entry(root.segundoContainer)
        root.id["width"] = 30
        root.id["font"] = root.fontePadrao
        root.id.pack()

        # detalhes novo
        root.detalhesLabel = Label(root.terceiroContainer, text="Descrição   ", font=root.fontePadrao)
        root.detalhesLabel.pack(side=LEFT)

        root.detalhes = Entry(root.terceiroContainer)
        root.detalhes["width"] = 30
        root.detalhes["font"] = root.fontePadrao
        root.detalhes.pack()

        # botão cancelar
        root.cancelar = Button(root.quartoContainer)
        root.cancelar["text"] = "Cancelar"
        root.cancelar["width"] = 12
        root.cancelar["command"] = lambda: root.destroy()
        root.cancelar.pack(side=LEFT, padx=10)

        # botão alterar
        root.alterar = Button(root.quartoContainer)
        root.alterar["text"] = "Alterar"
        root.alterar["width"] = 12
        root.alterar["command"] = lambda: alterarOcorrencia(root.id.get(), root.detalhes.get(), root)
        root.alterar.pack(padx=10)

        root.mainloop()


if __name__ == '__main__':
    InterfaceAlterarReporte.exibeInterface()
