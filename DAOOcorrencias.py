from datetime import datetime

from CriarBanco import Ocorrencias


def consulta_Ocorrencia(valor):
    Ocorrencia = Ocorrencias.query.filter_by(id=valor).first()
    return Ocorrencia


class Ocorrencia():
    def insere_Ocorrencias(detalhes):
        busca_Ocorrencia = Ocorrencias(detalhes=detalhes, data_criacao=datetime.now(), data_alteracao=datetime.now())
        busca_Ocorrencia.save()
        return 1

    def imprime_Ocorrencias():
        busca_Ocorrencia = Ocorrencias.query.all()
        if busca_Ocorrencia:
            print(busca_Ocorrencia)
            return busca_Ocorrencia

    def altera_Ocorrencias(id, detalhes):
        busca_Ocorrencia = consulta_Ocorrencia(id)
        if busca_Ocorrencia:
            busca_Ocorrencia.detalhes = detalhes
            busca_Ocorrencia.data_alteracao = datetime.now()
            busca_Ocorrencia.save()
            return 1
        else:
            print('Ocorrencia não encontrado')
            return 0

    def exclui_Ocorrencias(valor):
        busca_Ocorrencia = consulta_Ocorrencia(valor)
        if busca_Ocorrencia:
            busca_Ocorrencia.delete()
            return 1
        else:
            print('Ocorrencia não encontrado')
            return 0

    if __name__ == '__main__':
        # insere_Ocorrencias("falta de material")
        # altera_Ocorrencias(1,"teste")
        # exclui_Ocorrencias(2)
        imprime_Ocorrencias()
