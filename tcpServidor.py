from socket import *

from InterfacePedidoSocorro import InterfacePedidoSocorro

quant = 0

def atribuiValor():
    global quant
    quant += 1
    return quant


class tcpServidor():
    def receberMensagem():
        # Configura Socket
        serverPort = 12000
        serverSocket = socket(AF_INET, SOCK_STREAM)
        serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        serverSocket.bind(('', serverPort))
        serverSocket.listen(1)
        print('Servido pronto para receber chamadas')
        while True:
            # Aguarda recebimento da mensagem
            connectionSocket, addr = serverSocket.accept()
            fraseRecebida = connectionSocket.recv(1024)
            print('Socorro!! ', fraseRecebida.decode("utf-8"))
            InterfacePedidoSocorro.exibeMensagemTela(fraseRecebida.decode("utf-8"))


if __name__ == '__main__':
    tcpServidor.receberMensagem()
