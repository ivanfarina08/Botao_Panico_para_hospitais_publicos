# -*- coding: utf-8 -*-

from tkinter import *

from InterfaceAlteraLocalizacoes import InterfaceAlteraLocalizacoes
from InterfaceAlterarServidor import InterfaceAlterarServidor
from InterfaceCadastroLocalizacoes import InterfaceCadastroLocalizacoes
from InterfaceCadastroServidor import InterfaceCadastroServidor
from InterfaceExcluiLocalizacoes import InterfaceExcluiLocalizacoes
from InterfaceExcluirServidor import InterfaceExcluirServidor
from InterfaceVisualizarLocalizacoes import InterfaceVisualizarLocalizacoes
from InterfaceVisualizarServidores import InterfaceVisualizarServidores


# Servidores

def cadastrarServidor(master):
    InterfaceCadastroServidor.exibeInterface(master)


def alterarServidor(master):
    InterfaceAlterarServidor.exibeInterface(master)


def excluirServidor(master):
    InterfaceExcluirServidor.exibeInterface(master)


def visualizaServidores(master):
    InterfaceVisualizarServidores.exibeInterface(master)


# Localizações

def cadastrarLocalizacao(master):
    InterfaceCadastroLocalizacoes.exibeInterface(master)


def alterarLocalizacao(master):
    InterfaceAlteraLocalizacoes.exibeInterface(master)


def excluirLocalizacao(master):
    InterfaceExcluiLocalizacoes.exibeInterface(master)


def visualizaLocalizacoes(master):
    InterfaceVisualizarLocalizacoes.exibeInterface(master)


class InterfacePaginaInicial:
    def exibeInterface(self=None):
        master = Tk()
        master.geometry("770x400")
        # *********************************************************************************************
        # Inicio Containers

        master.title("Bem vindo!")

        master.fontePadrao = ("Arial", "12")
        master.primeiroContainer = Frame(self)
        master.primeiroContainer["pady"] = 20
        master.primeiroContainer.pack()

        master.terceiroContainer = Frame(self)
        master.terceiroContainer["pady"] = 30
        master.terceiroContainer["padx"] = 100
        master.terceiroContainer.pack()

        master.quartoContainer = Frame(self)
        # root.quartoContainer["pady"] = 20
        master.quartoContainer["padx"] = 100
        master.quartoContainer.pack()

        master.quintoContainer = Frame(self)
        master.quintoContainer["pady"] = 20
        master.quintoContainer["padx"] = 100
        master.quintoContainer.pack()

        master.sextoContainer = Frame(self)
        # root.sextoContainer["pady"] = 20
        master.sextoContainer["padx"] = 100
        master.sextoContainer.pack()

        master.setimoContainer = Frame(self)
        master.setimoContainer["pady"] = 20
        master.setimoContainer["padx"] = 100
        master.setimoContainer.pack()

        # Fim Containers

        # *********************************************************************************************

        # Título
        master.titulo = Label(master.primeiroContainer, text="Bem vindo!")
        master.titulo["font"] = ("Arial", "20", "bold")
        master.titulo.pack()

        # Título 2
        master.titulo = Label(master.primeiroContainer, text="Escolha uma das opções abaixo")
        master.titulo["font"] = ("Arial", "13", "bold")
        master.titulo.pack()

        # Servidores
        master.servidoresLabel = Label(master.terceiroContainer, text="  Servidores", font=master.fontePadrao)
        # root.servidoresLabel["font"] = ("Arial", "13", "underline")
        master.servidoresLabel.pack(side=LEFT, padx=85)

        # Localizações
        master.LocalizacoesLabel = Label(master.terceiroContainer, text="Localizações", font=master.fontePadrao)
        # root.LocalizacoesLabel["font"] = ("Arial", "13", "underline")
        master.LocalizacoesLabel.pack(padx=90)

        # Servidores botão Cadastrar
        master.Scadastrar = Button(master.quartoContainer)
        master.Scadastrar["text"] = "Cadastrar"
        master.Scadastrar["width"] = 12
        master.Scadastrar["command"] = lambda: cadastrarServidor(master)
        master.Scadastrar.pack(side=LEFT, padx=70)

        # Localizações botão Cadastrar
        master.Lcadastrar = Button(master.quartoContainer)
        master.Lcadastrar["text"] = "Cadastrar"
        master.Lcadastrar["width"] = 12
        master.Lcadastrar["command"] = lambda: cadastrarLocalizacao(master)
        master.Lcadastrar.pack(padx=70)

        # Servidores botão Alterar
        master.Salterar = Button(master.quintoContainer)
        master.Salterar["text"] = "Alterar"
        master.Salterar["width"] = 12
        master.Salterar["command"] = lambda: alterarServidor(master)
        master.Salterar.pack(side=LEFT, padx=70)

        # Localizações botão Alterar
        master.Lalterar = Button(master.quintoContainer)
        master.Lalterar["text"] = "Alterar"
        master.Lalterar["width"] = 12
        master.Lalterar["command"] = lambda: alterarLocalizacao(master)
        master.Lalterar.pack(padx=70)

        # Servidores botão Excluir
        master.Sexcluir = Button(master.sextoContainer)
        master.Sexcluir["text"] = "Excluir"
        master.Sexcluir["width"] = 12
        master.Sexcluir["command"] = lambda: excluirServidor(master)
        master.Sexcluir.pack(side=LEFT, padx=70)

        # Localizações botão Excluir
        master.Lexcluir = Button(master.sextoContainer)
        master.Lexcluir["text"] = "Excluir"
        master.Lexcluir["width"] = 12
        master.Lexcluir["command"] = lambda: excluirLocalizacao(master)
        master.Lexcluir.pack(padx=70)

        # Servidores botão Visualizar
        master.Svisualizar = Button(master.setimoContainer)
        master.Svisualizar["text"] = "Visualizar"
        master.Svisualizar["width"] = 12
        master.Svisualizar["command"] = lambda: visualizaServidores(master)
        master.Svisualizar.pack(side=LEFT, padx=70)

        # Localizações botão Visualizar
        master.Lvisualizar = Button(master.setimoContainer)
        master.Lvisualizar["text"] = "Visualizar"
        master.Lvisualizar["width"] = 12
        master.Lvisualizar["command"] = lambda: visualizaLocalizacoes(master)
        master.Lvisualizar.pack(padx=70)

        master.mainloop()


if __name__ == '__main__':
    InterfacePaginaInicial.exibeInterface()
