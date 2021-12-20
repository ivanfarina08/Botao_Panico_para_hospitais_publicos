from CriarBanco import ReportarPedidoSocorro


def consulta_reporte(valor):
    reporte = ReportarPedidoSocorro.query.filter_by(id=valor).first()
    return reporte


class DAOReportarSocorro():
    def insere_reportePedidoSocorro(descricao):
        reporte = ReportarPedidoSocorro(descricao=descricao)
        reporte.save()
        return 1

    def imprime_reportePedidoSocorro():
        reporte = ReportarPedidoSocorro.query.all()
        if reporte:
            print(reporte)
            return reporte

    def altera_reportePedidoSocorro(idAntigo, idNovo, descricao):
        reporte = consulta_reporte(idAntigo)
        if reporte:
            reporte.id = idNovo
            reporte.descricao = descricao
            reporte.save()
            return 1
        else:
            print('Reporte não encontrado')
            return 0

    def exclui_reportePedidoSocorro(valor):
        reporte = consulta_reporte(valor)
        if reporte:
            reporte.delete()
            return 1
        else:
            print('Reporte não encontrado')
            return 0

    if __name__ == '__main__':
        insere_reportePedidoSocorro("falta de material")
        # altera_reportePedidoSocorro(1,1,"teste")
        # exclui_reportePedidoSocorro(1)
        imprime_reportePedidoSocorro()
