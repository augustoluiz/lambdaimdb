from dataclasses import dataclass
from dataclasses_json import dataclass_json, LetterCase


@dataclass_json(LetterCase.PASCAL)
@dataclass
class Rating:
    source: str
    value: str
