from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from src.entities.livro import Livro
from src.entities.pessoa import Pessoa


@dataclass
class Aluguel:
    """
    Classe que representa um aluguel de um livro,
    incluindo o livro alugado, a pessoa que alugou e as datas de aluguel e devolução.
    """
    id: int
    data_do_aluguel: datetime
    data_da_devolucao: Optional[datetime]
    livro: Livro
    pessoa: Pessoa

    def __str__(self):
        """
        Retorna uma representação em string detalhada do aluguel.
        """
        return (f"Id: {self.id} "
                f"\nData do Aluguel: {self.data_do_aluguel} "
                f"\nData da devolução: {self.data_da_devolucao or 'Ainda não devolvido'} "
                f"\nCliente: {self.pessoa} "
                f"\nLivro: {self.livro} "
                f"\n--------------------------\n")
