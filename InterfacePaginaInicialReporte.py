# -*- coding: utf-8 -*-

from tkinter import *

from InterfaceAlterarOcorrencia import InterfaceAlterarReporte
from InterfaceExcluirOcorrencia import InterfaceExcluirReporte
from InterfaceVisualizarOcorrencia import InterfaceVisualizarReporte


def alterarReporte(master):
    InterfaceAlterarReporte.exibeInterface(master)


def excluirReporte(master):
    InterfaceExcluirReporte.exibeInterface(master)


def visualizaReporte(master):
    InterfaceVisualizarReporte.exibeInterface(master)


class InterfacePaginaInicial:
    def exibeInterface(self=None):
        master = Tk()
        master.geometry("700x350")
        # *********************************************************************************************
        # Inicio Containers

        master.title("Bem vindo!")

        master.fontePadrao = ("Arial", "12")
        master.primeiroContainer = Frame(self)
        master.primeiroContainer["pady"] = 20
        master.primeiroContainer.pack()

        master.segundoContainer = Frame(self)
        master.segundoContainer["pady"] = 30
        master.segundoContainer["padx"] = 100
        master.segundoContainer.pack()

        master.terceiroContainer = Frame(self)
        # master.terceiroContainer["pady"] = 30
        master.terceiroContainer["padx"] = 100
        master.terceiroContainer.pack()

        master.quartoContainer = Frame(self)
        master.quartoContainer["pady"] = 30
        master.quartoContainer["padx"] = 100
        master.quartoContainer.pack()

        # Fim Containers

        # *********************************************************************************************

        # Título
        master.titulo = Label(master.primeiroContainer, text="Bem vindo ao gerenciamento de Reportes!")
        master.titulo["font"] = ("Arial", "20", "bold")
        master.titulo.pack()

        # Título 2
        master.titulo = Label(master.primeiroContainer, text="Escolha uma das opções abaixo")
        master.titulo["font"] = ("Arial", "13", "bold")
        master.titulo.pack()

        # Servidores botão Alterar
        master.alterar = Button(master.segundoContainer)
        master.alterar["text"] = "Alterar"
        master.alterar["width"] = 12
        master.alterar["command"] = lambda: alterarReporte(master)
        master.alterar.pack(side=LEFT, padx=70)

        # Servidores botão Excluir
        master.excluir = Button(master.terceiroContainer)
        master.excluir["text"] = "Excluir"
        master.excluir["width"] = 12
        master.excluir["command"] = lambda: excluirReporte(master)
        master.excluir.pack(side=LEFT, padx=70)

        # Localizações botão Visualizar
        master.visualizar = Button(master.quartoContainer)
        master.visualizar["text"] = "Visualizar"
        master.visualizar["width"] = 12
        master.visualizar["command"] = lambda: visualizaReporte(master)
        master.visualizar.pack(padx=70)

        master.mainloop()


if __name__ == '__main__':
    InterfacePaginaInicial.exibeInterface()
