from CriarBanco import Servidores


def consulta_servidor(valor):
    servidor = Servidores.query.filter_by(IP=valor).first()
    return servidor


class DAOServidor():
    def insere_servidor(ip, descricao):
        servidor = Servidores(IP=ip, descricao=descricao)
        if consulta_servidor(servidor.IP):
            print('Servidor já cadastrado')
            return 0
        else:
            print(servidor)
            servidor.save()
            return 1

    def imprime_servidores():
        servidor = Servidores.query.all()
        if servidor:
            print(servidor)
            return servidor

    def imprime_servidor(valor):
        servidor = consulta_servidor(valor)
        if servidor:
            print(servidor.descricao, ' - ', servidor.IP)
        else:
            print('Servidor não encontrado')

    def altera_servidor(ipAntigo, ipAtual, descricaoAtual):
        servidor = consulta_servidor(ipAntigo)
        if servidor:
            servidor.IP = ipAtual
            servidor.descricao = descricaoAtual
            servidor.save()
            return 1
        else:
            print('Servidor não encontrado')
            return 0

    def exclui_servidor(valor):
        servidor = consulta_servidor(valor)
        if servidor:
            servidor.delete()
            return 1
        else:
            print('Servidor não encontrado')
            return 0

    def excluir_tudo():
        servidor = Servidores.query.all()
        for s in servidor:
            s.delete()

    def quantidadeServidores():
        print(Servidores.query.count())
        return Servidores.query.count()

    if __name__ == '__main__':
        # insere_servidor('localhost','Computador 1')
        # imprime_servidores()
        # quantidadeServidores()
        # imprime_servidor('teste')
        # altera_servidor('127.0.0.1','127.0.0.1','Ivan')
        imprime_servidores()
        # exclui_servidor('12')
        # excluir_tudo()
