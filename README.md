# 📝 To-Do List

## 📌 Descrição
Este projeto é uma aplicação web de **lista de tarefas (To-Do List)** desenvolvida com o framework **Django**.  
O sistema permite que os usuários criem, visualizem, editem e excluam tarefas de forma simples e organizada.  
O objetivo é oferecer uma interface intuitiva e prática para o gerenciamento do dia a dia.

---

## 🛠️ Ferramentas Utilizadas
- **Django 5.2.7**
- **HTML5 / CSS3**
- **Bootstrap** (para estilização responsiva)
- **SQLite3** (banco de dados padrão do Django)
- **Git e GitHub** (para controle de versão)

---

## 👥 Responsabilidades da Dupla
| Integrante | Responsabilidades |
|-------------|-------------------|
| **Carlos Eduardo** | Implementação do backend com Django, criação dos modelos e rotas, configuração do banco de dados. |
| **Ana Carolina** | Desenvolvimento do frontend com Bootstrap e testes de usabilidade. |

---

## 🚀 Como Executar o Projeto

Para rodar o projeto localmente, siga os passos abaixo no terminal:

# 1. Clonar o repositório
git clone https://github.com/cadugoncalvesb/todo.git

# 2. Acessar a pasta do projeto
cd todo

# 3. Criar e ativar o ambiente virtual
python -m venv venv
# No Windows
venv\Scripts\activate
# No Linux/Mac
source venv/bin/activate

# 4. Instalar o Django
pip install django

# 5. Instalar as dependências
pip install -r requirements.txt

# 6. Criar migrações a partir dos modelos
python manage.py makemigrations

# 7. Aplicar as migrações no banco de dados
python manage.py migrate

# 8. Executar o servidor
python manage.py runserver
