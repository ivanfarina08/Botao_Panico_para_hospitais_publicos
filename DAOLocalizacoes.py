from CriarBanco import Todas_localizações


def consulta_localizacao(nome):
    localizacao = Todas_localizações.query.filter_by(nome=nome).first()
    return localizacao


class DAOLocalizacoes():
    def insere_localizacao(valor):
        localizacao = Todas_localizações(nome=valor)
        if consulta_localizacao(localizacao.nome):
            print('localizacao já cadastrada')
            return 0
        else:
            print(valor)
            localizacao.save()
            return 1

    def imprime_localizacoes():
        localizacao = Todas_localizações.query.all()
        if localizacao:
            print(localizacao)
            return localizacao

    def imprime_localizacao(valor):
        localizacao = consulta_localizacao(valor)
        if localizacao:
            print(localizacao.nome)
        else:
            print('localizacao não encontrado')

    def altera_localizacao(valorAntigo, valorNovo):
        localizacao = consulta_localizacao(valorAntigo)
        if localizacao:
            localizacao.nome = valorNovo
            localizacao.save()
            return 1
        else:
            print('localizacao não encontrado')
            return 0

    def exclui_localizacao(valor):
        localizacao = consulta_localizacao(valor)
        if localizacao:
            localizacao.delete()
            return 1
        else:
            print('localizacao não encontrado')
            return 0

    if __name__ == '__main__':
        # insere_localizacao('teste')
        imprime_localizacoes()
        # imprime_localizacao('Consultorio 1')
        # altera_localizacao('Consultorio 1')
        # imprime_localizacoes()
        exclui_localizacao('teste')
