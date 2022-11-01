import json
from pathlib import Path

from src.service.imdb_service import IMDBService
from src.model.request.consulta_conteudo import ConsultaConteudo
from src.model.enum.tipo_consulta_enum import TipoConsultaEnum


def lambda_handler(event, context):
    service = IMDBService()

    request = ConsultaConteudo(**json.dump(event))
    
    tipo_consulta = TipoConsultaEnum(request.tipo_consulta)
    service.consultar_informacao(tipo_consulta=tipo_consulta, valor_consulta=request.valor_consulta)

    return {
        "statusCode": 200,
        "body": {
            'id': 123
        }
    }
