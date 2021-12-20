import time
import tkinter as tk
from tkinter import *
from tkinter import messagebox

from DAOOcorrencias import Ocorrencia


def reportar(detalhes):
    if detalhes:
        Ocorrencia.insere_Ocorrencias(detalhes)
        tk.messagebox.showinfo(title="Reporte", message="Salvo com sucesso")
    else:
        tk.messagebox.showinfo(title="Reporte", message="Reporte vazio")


class InterfacePedidoSocorroComReport:
    def exibeMensagemTela(mensagem, master=None):
        root = Tk()
        root.attributes('-topmost', True)

        root.geometry("550x400")
        root.title("Pedido de Socorro")

        root.primeiroContainer = Frame(master)
        root.primeiroContainer["pady"] = 30
        root.primeiroContainer["padx"] = 100
        root.primeiroContainer.pack()

        root.segundoContainer = Frame(master)
        root.segundoContainer["pady"] = 30
        root.segundoContainer["padx"] = 50
        root.segundoContainer.pack()

        root.terceiroContainer = Frame(master)
        root.terceiroContainer["pady"] = 30
        root.terceiroContainer["padx"] = 50
        root.terceiroContainer.pack()

        root.quartoContainer = Frame(master)
        root.quartoContainer["pady"] = 30
        root.quartoContainer["padx"] = 50
        root.quartoContainer.pack()

        # Configuração da tela
        root.fontePadrao = ("Arial", "12")

        # Mensagem recebida do cliente
        mensagemSocorro = 'Socorro!!\n\n' + mensagem
        mensagemCliente = tk.Label(root.primeiroContainer, text=mensagemSocorro, font=("Arial", "14", "bold"))
        mensagemCliente.pack()

        # nome
        root.detalhesLabel = Label(root.terceiroContainer, text="Descrição   ", font=root.fontePadrao)
        root.detalhesLabel.pack(side=LEFT)

        root.detalhes = Text(root.terceiroContainer)
        root.detalhes["width"] = 30
        root.detalhes["height"] = 5
        root.detalhes["font"] = root.fontePadrao
        root.detalhes.pack()

        # Reportar pedido
        # botão cancelar
        root.cancelar = Button(root.quartoContainer)
        root.cancelar["text"] = "Cancelar"
        root.cancelar["width"] = 12
        root.cancelar["command"] = lambda: quit()
        root.cancelar.pack(side=LEFT, padx=10)

        # botão salvar
        root.reportar = Button(root.quartoContainer)
        root.reportar["text"] = "Reportar"
        root.reportar["width"] = 12
        root.reportar["command"] = lambda: reportar(root.detalhes.get("1.0", 'end-1c'))
        root.reportar.pack(padx=10)

        root.mainloop()


if __name__ == '__main__':
    InterfacePedidoSocorroComReport.exibeMensagemTela('teste')
