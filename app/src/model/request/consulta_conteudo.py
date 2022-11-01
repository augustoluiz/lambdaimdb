from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class ConsultaConteudo:
    tipo_consulta: int
    id: str
    titulo: str
