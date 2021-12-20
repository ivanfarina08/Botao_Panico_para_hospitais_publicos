# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import *
from tkinter import messagebox
from DAOOcorrencias import Ocorrencia


def excluirReporte(txid, root):
    retorno = Ocorrencia.exclui_Ocorrencias(txid)
    if retorno == 1:
        tk.messagebox.showinfo(parent=root, title="Excluir", message="Excluído com sucesso")
    else:
        tk.messagebox.showinfo(parent=root, title="Excluir", message="Reporte não encontrado")


class InterfaceExcluirReporte:
    def exibeInterface(master):
        root = Toplevel(master)
        # *********************************************************************************************
        # Inicio Containers

        root.geometry("500x250")
        root.title("Excluir servidores")

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
        root.titulo = Label(root.primeiroContainer, text="Excluir Reporte")
        root.titulo["font"] = ("Arial", "15", "bold")
        root.titulo.pack()

        # id
        root.idLabel = Label(root.segundoContainer, text="Id   ", font=root.fontePadrao)
        root.idLabel.pack(side=LEFT)

        root.id = Entry(root.segundoContainer)
        root.id["width"] = 30
        root.id["font"] = root.fontePadrao
        root.id.pack()

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
        root.excluir["command"] = lambda: excluirReporte(root.id.get(), root)
        root.excluir.pack(padx=10)

        root.mainloop()


if __name__ == '__main__':
    InterfaceExcluirReporte.exibeInterface()
