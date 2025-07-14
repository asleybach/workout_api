from typing import Annotated, Optional
from pydantic import Field, PositiveFloat
from workout_api import centro_treinamento
from workout_api.categorias.schemas import CategoriaIn
from workout_api.centro_treinamento.schemas import CentroTreinamentoAtleta

from workout_api.contrib.schemas import BaseSchema, OutMixin


class Atleta(BaseSchema):
    nome: Annotated[str, Field(description='Nome do atleta', example='Joao', max_length=50)]
    cpf: Annotated[str, Field(description='CPF do atleta', example='12345678900', max_length=11)]
    idade: Annotated[int, Field(description='Idade do atleta', example=25)]
    peso: Annotated[PositiveFloat, Field(description='Peso do atleta', example=75.5)]
    altura: Annotated[PositiveFloat, Field(description='Altura do atleta', example=1.70)]
    sexo: Annotated[str, Field(description='Sexo do atleta', example='M', max_length=1)]
    categoria: Annotated[CategoriaIn, Field(description='Categoria do atleta')]
    centro_treinamento: Annotated[CentroTreinamentoAtleta, Field(description='Centro de treinamento do atleta')]


class AtletaIn(Atleta):
    pass


class AtletaOut(Atleta, OutMixin):
    id: Annotated[str, Field(description='Identificador do atleta', example='123e4567-e89b-12d3-a456-426614174000')]
    nome: Annotated[str, Field(description='Nome do atleta', example='Joao', max_length=50)]
    centro_treinamento: Annotated[CentroTreinamentoAtleta, Field(description='Centro de treinamento do atleta')]
    categoria: Annotated[CategoriaIn, Field(description='Categoria do atleta')]
    created_at: Annotated[str, Field(description='Data de criação do atleta', example='2023-10-01T12:00:00Z')]
    updated_at: Annotated[Optional[str], Field(description='Data de atualização do atleta', example='2023-10-02T12:00:00Z')]

class AtletaUpdate(BaseSchema):
    nome: Annotated[Optional[str], Field(None, description='Nome do atleta', example='Joao', max_length=50)]
    idade: Annotated[Optional[int], Field(None, description='Idade do atleta', example=25)]