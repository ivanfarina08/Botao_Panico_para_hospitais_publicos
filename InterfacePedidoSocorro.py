import tkinter as tk
from tkinter import *


class InterfacePedidoSocorro:
    def exibeMensagemTela(mensagem, master=None):
        root = Tk()
        root.attributes('-topmost', True)

        root.geometry("400x150")
        root.title("Pedido de Socorro")

        root.primeiroContainer = Frame(master)
        root.primeiroContainer["pady"] = 30
        root.primeiroContainer["padx"] = 100
        root.primeiroContainer.pack()

        root.segundoContainer = Frame(master)
        root.segundoContainer["pady"] = 30
        root.segundoContainer["padx"] = 50
        root.segundoContainer.pack()

        # Configuração da tela
        root.fontePadrao = ("Arial", "12")

        # Mensagem recebida do cliente
        mensagemSocorro = 'Socorro!!\n\n' + mensagem
        mensagemCliente = tk.Label(root.primeiroContainer, text=mensagemSocorro, font=("Arial", "14", "bold"))
        mensagemCliente.pack()

        root.mainloop()


if __name__ == '__main__':
    InterfacePedidoSocorro.exibeMensagemTela('teste')
