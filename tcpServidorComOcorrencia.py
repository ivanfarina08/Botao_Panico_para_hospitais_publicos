from socket import *

from InterfacePedidoSocorroComReport import InterfacePedidoSocorroComReport


class tcpServidorComReport():
    # *********************************************************************************************

    # Recebe parametros para comunicação com o cliente

    def receberMensagem():
        serverPort = 12000
        serverSocket = socket(AF_INET, SOCK_STREAM)
        serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        serverSocket.bind(('', serverPort))

        serverSocket.listen(1)
        print('Servido pronto para receber chamadas')

        while True:
            # Receber mensagem
            connectionSocket, addr = serverSocket.accept()

            fraseRecebida = connectionSocket.recv(1024)

            print('Socorro!! ', fraseRecebida.decode("utf-8"))

            InterfacePedidoSocorroComReport.exibeMensagemTela(fraseRecebida.decode("utf-8"))


if __name__ == '__main__':
    tcpServidorComReport.receberMensagem()
