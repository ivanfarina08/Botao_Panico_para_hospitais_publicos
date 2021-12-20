from sqlalchemy import create_engine, Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('sqlite:///BancoPanico.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


class Servidores(Base):
    __tablename__ = 'servidores'
    IP = Column(String(18), primary_key=True, autoincrement=False)
    descricao = Column(String(40), index=True)

    def __repr__(self):
        return '{} - {}'.format(self.descricao, self.IP)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()


class Todas_localizações(Base):
    __tablename__ = 'todas_localizações'
    nome = Column(String(80), primary_key=True, autoincrement=False)

    def __repr__(self):
        return '{}'.format(self.nome)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()


class Localização_atual(Base):
    __tablename__ = 'localização_atual'
    nome = Column(String(80), primary_key=True, autoincrement=False)

    def __repr__(self):
        return '{}'.format(self.nome)

    def save(self):
        db_session.add(self)
        db_session.commit()


class Ocorrencias(Base):
    __tablename__ = 'Ocorrencias'
    id = Column(Integer, primary_key=True, autoincrement=True)
    detalhes = Column(String(200), index=True)
    data_criacao = Column(DateTime(timezone=True))
    data_alteracao = Column(DateTime(timezone=True))

    def __repr__(self):
        return '{} - {} - {} - {}'.format(self.id, self.detalhes, self.data_criacao, self.data_alteracao)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()


def init_db():
    Base.metadata.create_all(bind=engine)


def insereTodasLocalizacoes():
    localizacao = Todas_localizações(nome='Consultorio 1')
    localizacao.save()


def insereLocalizacaoAtual():
    localizacao = Localização_atual(nome='Consultorio 1')
    localizacao.save()


if __name__ == '__main__':
    init_db()
    insereTodasLocalizacoes()
    insereLocalizacaoAtual()
