from CriarBanco import Localização_atual


class DAOLocalizacaoAtual():
    def imprime_localizacao():
        localizacao = Localização_atual.query.first()
        # print(localizacao)
        return localizacao

    def altera_localizacao(valor):
        localizacao = Localização_atual.query.first()
        localizacao.nome = valor
        localizacao.save()
        print('Alterado para: ', localizacao)

    if __name__ == '__main__':
        # insere_localizacao()
        imprime_localizacao()
        # altera_localizacao('Consultorio 2')
        # imprime_localizacoes()
