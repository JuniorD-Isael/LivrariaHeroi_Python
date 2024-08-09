# Aplicação Livraria Herói 📚🦸

Esta aplicação é uma API para uma livraria. O projeto foi desenvolvido utilizando a linguagem de programação Python.

## Estrutura do Projeto 🏗️

O projeto está estruturado da seguinte maneira:

```
src/
├── config/               # Configurações do projeto
│   └── admin_config.py   # Armazena a configuração do administrador 🔐
├── data/                 # Armazenamento e gerenciamento de dados
│   └── biblioteca.py     # Armazena dados dos usuários e dos livros 📖
├── entities/             # Entidades do projeto
│   ├── adm.py            # Representa administradores
│   ├── cliente.py        # Representa clientes
│   ├── pessoa.py         # Representa uma pessoa base
│   ├── livro.py          # Representa livros
│   └── aluguel.py        # Representa aluguéis
├── services/             # Serviços para manipular entidades
│   ├── usuario_service.py# Métodos para gerenciamento de usuários 👥
│   ├── livro_service.py  # Métodos para gerenciamento de livros 📚
│   └── aluguel_service.py# Métodos para gerenciamento de aluguéis 📚
├── controller/           # Controladores para interações do usuário
│   ├── usuario_controller.py # Gerencia interações com usuários 🎮
│   ├── livro_controller.py   # Gerencia interações com livros 🎮
│   ├── aluguel_controller.py # Gerencia interações com aluguéis 🎮
│   └── login_controller.py   # Gerencia o login 🎮
├── menu/                 # Menus personalizados para cada tipo de usuário
│   ├── admin_menu.py     # Menu para administradores 📜
│   └── user_menu.py      # Menu para usuários comuns 📜
├── interfaces/           # Interfaces que definem contratos para serviços
│   └── alugavel.py       # Define o protocolo para objetos alugáveis 📝
├── util/                 # Utilitários e ferramentas auxiliares
│   ├── id_generator.py   # Gera IDs únicos 🧰
│   └── scanner_util.py   # Ferramentas auxiliares de entrada 🧰
└── main.py               # Ponto de entrada principal da aplicação
```

## Funcionalidades 🚀

O projeto possui as seguintes funcionalidades:

- **Criação de usuários**: Através do método `criar_usuario` no módulo `usuario_service`, é possível criar novos usuários, sejam eles administradores ou clientes 👥.

- **Listagem de usuários**: O método `listar_usuarios` no módulo `usuario_service` permite listar todos os usuários cadastrados 👀.

- **Busca de usuários**: O método `buscar_usuario` no módulo `usuario_service` permite buscar um usuário pelo seu ID 🔍.

- **Deleção de usuários**: O método `deletar_usuario` no módulo `usuario_service` permite deletar um usuário pelo seu ID ❌.

- **Atualização de usuários**: O método `atualizar_usuario` no módulo `usuario_service` permite atualizar os dados de um usuário 🔄.

- **Validação de administradores**: O método `validar_adm` no módulo `usuario_service` permite validar se um usuário é um administrador através da senha de administrador 🔐.

- **Gerenciamento de livros**: O módulo `livro_service` permite criar, listar, buscar, atualizar e deletar livros 📚.

- **Gerenciamento de aluguéis**: O módulo `aluguel_service` permite alugar um livro, devolver um livro, listar todos os aluguéis e buscar um aluguel específico 📚.

- **Sistema de Login**: A aplicação possui um sistema de login básico, onde os detalhes do usuário são verificados para autenticação 🔐.

- **Menu Personalizado**: A aplicação possui um menu personalizado para cada tipo de usuário, seja comum ou admin. Esse menu só é chamado após a confirmação do login 📜.
