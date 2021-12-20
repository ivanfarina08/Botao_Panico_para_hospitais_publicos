# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import *

import DAOServidor


class InterfaceVisualizarServidores:
    def exibeInterface(master):
        root = Toplevel(master)

        # Criação de containers

        root.title("Visualizar Servidores")

        root.fontePadrao = ("Arial", "12")
        root.primeiroContainer = Frame(root)
        root.primeiroContainer["pady"] = 15
        root.primeiroContainer["padx"] = 150
        root.primeiroContainer.pack()

        root.segundoContainer = Frame(root)
        root.segundoContainer["pady"] = 15
        root.segundoContainer.pack()

        root.terceiroContainer = Frame(root)
        root.terceiroContainer["pady"] = 10
        root.terceiroContainer.pack()

        # *********************************************************************************************

        # Título
        root.titulo = Label(root.primeiroContainer, text="Tabela Servidores")
        root.titulo["font"] = ("Arial", "15", "bold")
        root.titulo.pack()

        # *********************************************************************************************

        # Servidores

        servidores = DAOServidor.DAOServidor.imprime_servidores()
        for linha in servidores:
            valoresLinha = tk.Label(root.segundoContainer, text=linha)
            valoresLinha.pack()

        # *********************************************************************************************

        # botão sair
        root.sair = Button(root.terceiroContainer)
        root.sair["text"] = "Sair"
        root.sair["width"] = 12
        root.sair["command"] = lambda: root.destroy()
        root.sair.pack(side=LEFT)

        root.mainloop()


if __name__ == '__main__':
    InterfaceVisualizarServidores.exibeInterface()
