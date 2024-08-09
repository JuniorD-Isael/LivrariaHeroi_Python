from dataclasses import dataclass
from src.interfaces.alugavel import Alugavel


@dataclass
class Livro(Alugavel):
    id: int
    titulo: str
    autor: str
    ano: int
    alugado: bool = False

    def get_alugado(self) -> bool:
        return self.alugado

    def set_alugado(self, alugado: bool) -> None:
        self.alugado = alugado

    def __str__(self):
        return (f"Id: {self.id}"
                f"\nTitulo: {self.titulo}"
                f"\nAutor: {self.autor}"
                f"\nAno: {self.ano}"
                f"\nAlugado: {self.alugado}"
                f"\n--------------------------\n")
