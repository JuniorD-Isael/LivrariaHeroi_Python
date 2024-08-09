from typing import Protocol


class Alugavel(Protocol):

    def get_alugado(self) -> bool:
        ...

    def set_alugado(self, alugavel: bool) -> None:
        ...
