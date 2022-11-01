from dataclasses import dataclass
from dataclasses_json import dataclass_json
from dataclasses_json import LetterCase

from src.model.response.rating import Rating


@dataclass_json(letter_case=LetterCase.PASCAL)
@dataclass
class InformacaoConteudo:
    title: str
    year: str
    rated: str
    released: str
    runtime: str
    genre: str
    director: str
    writer: str
    actors: str
    plot: str
    language: str
    country: str
    awards: str
    poster: str
    ratings: (Rating)
    metascore: str
    imdb_rating: str
    imdb_votes: str
    imdb_id: str
    type: str
    dvd: str
    box_office: str
    production: str
    website: str
    response: str
