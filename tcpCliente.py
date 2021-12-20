from socket import *

from DAOLocalizacaoAtual import DAOLocalizacaoAtual
from DAOServidor import DAOServidor


# Conecta no servidor envia pedido de socorro
def conectaServidor(serverIP, serverPort, texto, clientSocket):
    try:
        clientSocket.connect((serverIP, serverPort))
        clientSocket.sendto(texto.encode('utf-8'), (serverIP, serverPort))
    except:
        print('Servidor offline: ', serverIP)
    finally:
        clientSocket.close()


class tcpCliente():
    def enviaPedidoSocorro():
        # Busca no banco todos os servidores
        for servidores in DAOServidor.imprime_servidores():
            serverIP = servidores.IP
            serverPort = 12000
            computador = DAOLocalizacaoAtual.imprime_localizacao()
            texto = computador.nome
            clientSocket = socket(AF_INET, SOCK_STREAM)
            conectaServidor(serverIP, serverPort, texto, clientSocket)

    if __name__ == '__main__':
        enviaPedidoSocorro()
