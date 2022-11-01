import os

from unittest import case
from src.utils.lambda_utils import LambdaUtils
from src.service.request_service import RequestService
from src.model.enum.tipo_consulta_enum import TipoConsultaEnum
from src.model.response.informacao_conteudo import InformacaoConteudo
from src.model.response.response_error import ResponseError


class IMDBService:

    def __init__(self) -> None:
        self.__url__ = os.getenv(LambdaUtils.get_url_base_api_imdb) 
        self.__api__key__ = os.getenv(LambdaUtils.get_api_key)

    def consultar_informacao(self, tipo_consulta: TipoConsultaEnum, valor_consulta: str):
        chave_consulta = 'i' if tipo_consulta.IDENTIFICADOR else 't'
    
        response = RequestService.get(url=self.__url__, 
                                      params=self.__gerar_query_parameters(chave_consulta, valor_consulta))
        
        print(response)
        pass

    def __gerar_query_parameters(self, chave_consulta: str, valor_consulta: str) -> dict:
        return {
            chave_consulta: valor_consulta,
            'apikey': self.__api__key__
        }