from .pessoa import Pessoa
from dataclasses import dataclass


@dataclass
class Adm(Pessoa):
    is_admin: bool = True

    def __str__(self):
        base_str = super().__str__()
        return f"{base_str}\nAdmin: {self.is_admin}"
