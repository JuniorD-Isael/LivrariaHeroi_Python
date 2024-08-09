from typing import Dict
from src.entities.livro import Livro
from src.entities.pessoa import Pessoa
from src.entities.aluguel import Aluguel
from src.util.singleton import SingletonMeta


class Biblioteca(metaclass=SingletonMeta):
    livros: Dict[int, Livro]
    usuarios: Dict[int, Pessoa]
    alugueis: Dict[int, Aluguel]

    def __init__(self):
        self.livos = {}
        self.usuarios = {}
        self.alugueis = {}

    def get_livro(self) -> Dict[int, Livro]:
        return self.livros

    def get_usuario(self) -> Dict[int, Pessoa]:
        return self.usuarios

    def get_aluguel(self) -> Dict[int, Aluguel]:
        return self.alugueis
