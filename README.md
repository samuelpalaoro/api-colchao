API de Colchões - Portal de Reviews e Comparações 🛌








Este projeto é um portal completo para reviews e marketing de afiliados de colchões, construído com Django e Django REST Framework.
O diferencial do sistema é um motor de geração de conteúdo dinâmico, que cria páginas de comparação ricas e otimizadas para SEO automaticamente.

O objetivo é entregar valor real ao usuário com análises detalhadas e comparações lado a lado, enquanto oferece uma plataforma escalável e de baixa manutenção para o administrador.

✨ Principais Funcionalidades

API RESTful: Gerenciamento completo de Marcas, Tipos de Colchão e Produtos.

Motor de Comparação Dinâmica: Gera páginas "todos contra todos" automaticamente.

Automação com Django Signals: Novos produtos geram comparações automaticamente com todos os existentes, sem duplicatas.

Comandos Customizados: Permite popular o banco com todas as combinações de comparações de produtos já existentes.

Templates Responsivos: Detalhados, informativos e adaptáveis a qualquer tela.

Foco em SEO Programático: Criação de muitas páginas interligadas e relevantes para aumentar o ranking nos buscadores.

🛠️ Tecnologias Utilizadas

Backend: Python, Django

API: Django REST Framework (DRF)

Banco de Dados: SQLite 3 (desenvolvimento)

Frontend: Django Templates, HTML5, CSS3

🚀 Instalação e Configuração
1. Clone o Repositório
git clone [URL-DO-SEU-REPOSITORIO-GIT]
cd [NOME-DA-PASTA-DO-PROJETO]

2. Crie e Ative um Ambiente Virtual
# Linux/macOS
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
.\venv\Scripts\activate

3. Crie o arquivo requirements.txt
pip freeze > requirements.txt

4. Instale as Dependências
pip install -r requirements.txt

5. Aplique as Migrações
python manage.py migrate

6. Crie um Superusuário
python manage.py createsuperuser


Acesse o painel administrativo em /admin.

▶️ Rodando a Aplicação
python manage.py runserver


Site: http://127.0.0.1:8000

Admin: http://127.0.0.1:8000/admin

⚙️ Uso e Funcionalidades Chave
Cadastro de Produtos

Toda a gestão de Marcas, Tipos e Produtos é feita pelo Painel de Administração do Django.
Preencha todos os campos detalhados para alimentar o sistema.

Geração de Comparações

Automática (Novos Produtos):
Django Signals criam comparações automaticamente com todos os produtos existentes.

Manual (Produtos Existentes):
Para gerar comparações de produtos já cadastrados:

python manage.py create_all_comparisons


O comando cria apenas as combinações que ainda não existem, evitando duplicatas.

📄 Licença

Este projeto está sob a Licença MIT. Consulte o arquivo LICENSE para mais detalhes.
