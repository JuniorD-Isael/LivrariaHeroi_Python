from dataclasses import dataclass


@dataclass
class Pessoa:
    id: int
    nome: str
    cpf: str
    email: str
    telefone: str
    livros_alugados: int = 0
    is_admin: bool = False

    def __str__(self) -> str:
        return (f"ID: {self.id}, "
                f"\nNome: {self.nome}, "
                f"\nEmail: {self.email}, "
                f"\nTelefone: {self.telefone}")
