from unittest import case
from src.service.request_service import RequestService
from src.model.enum.tipo_consulta_enum import TipoConsultaEnum
from src.model.response.informacao_conteudo import InformacaoConteudo
from src.model.response.response_error import ResponseError


class IMDBService:

    def __init__(self) -> None:
        pass

    def consultar_informacao(self, tipo_consulta: TipoConsultaEnum, parametro: str):
        if(tipo_consulta.IDENTIFICADOR):
            pass
        elif(tipo_consulta.TITULO):
            pass
        else:
            pass

        pass