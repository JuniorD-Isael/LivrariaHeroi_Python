from .pessoa import Pessoa
from dataclasses import dataclass


@dataclass
class Cliente(Pessoa):

    def __str__(self):
        base_str = super().__str__()
        return f"{base_str}"
