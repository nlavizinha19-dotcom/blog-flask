# 🚀 Blog Flask - Sistema de Blog Completo

Uma aplicação web completa de blog construída com **Flask**, oferecendo todas as funcionalidades necessárias para publicação de conteúdo, gerenciamento de comunidade e análise.

## 📋 Funcionalidades Implementadas

### ✅ Principais Features
- **📝 Publicação de Posts** - Criar, editar e deletar artigos
- **📂 Categorias e Tags** - Organizar conteúdo por categorias e tags
- **🏠 Página Inicial Dinâmica** - Exibição de posts recentes e destacados
- **💬 Comentários** - Sistema de comentários nos posts
- **👥 Autenticação de Usuários** - Registro, login e gerenciamento de perfil
- **🛡️ Painel de Administração** - Dashboard completo para admins
- **🎨 Personalização do Design** - Temas e customização de cores
- **🔍 Otimização para Buscas** - Sistema de busca integrado
- **📊 Estatísticas** - Análise de visualizações e dados
- **📁 Gerenciamento de Arquivos** - Upload e gerenciamento de arquivos
- **✨ Sistema de Moderação** - Aprovação de comentários

## 📁 Estrutura do Projeto

```
blog-flask/
├── app/
│   ├── __init__.py              # Factory e configuração
│   ├── models.py                # Modelos de dados (User, Post, Comment, etc)
│   ├── main/                    # Blueprints principal
│   ├── users/                   # Autenticação e perfil
│   ├── posts/                   # Publicação e gerenciamento
│   ├── categories_tags/         # Organização de conteúdo
│   ├── comments/                # Sistema de comentários
│   ├── admin/                   # Painel administrativo
│   ├── design/                  # Personalização de temas
│   ├── search/                  # Busca de posts
│   ├── stats/                   # Estatísticas
│   ├── files/                   # Gerenciamento de arquivos
│   ├── templates/               # Templates HTML
│   └── static/                  # CSS, JS, imagens
├── config.py                    # Configurações da aplicação
├── run.py                       # Arquivo de inicialização
├── requirements.txt             # Dependências Python
└── .env.example                 # Exemplo de variáveis de ambiente
```

## 🛠️ Tecnologias Utilizadas

- **Flask** - Framework web
- **SQLAlchemy** - ORM para banco de dados
- **Flask-Login** - Autenticação de usuários
- **SQLite** - Banco de dados (padrão)
- **Bootstrap 5** - Frontend framework
- **Jinja2** - Template engine

## 📦 Instalação

### 1. Clonar o repositório
```bash
git clone https://github.com/nlavizinha19-dotcom/blog-flask.git
cd blog-flask
```

### 2. Criar ambiente virtual
```bash
python -m venv venv
```

### 3. Ativar ambiente virtual

**Windows (PowerShell):**
```bash
.\venv\Scripts\Activate.ps1
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

### 4. Instalar dependências
```bash
pip install -r requirements.txt
```

### 5. Configurar variáveis de ambiente
```bash
cp .env.example .env
```

Edite o arquivo `.env` conforme necessário:
```
FLASK_APP=run.py
FLASK_ENV=development
SECRET_KEY=sua-chave-secreta-aqui
DATABASE_URL=sqlite:///blog.db
```

### 6. Inicializar banco de dados
```bash
python
>>> from app import create_app, db
>>> from app.models import *
>>> app = create_app()
>>> with app.app_context():
...     db.create_all()
>>> exit()
```

### 7. Executar aplicação
```bash
python run.py
```

A aplicação estará disponível em `http://localhost:5000`

## 🔐 Criando Primeiro Usuário Admin

1. Registre um usuário normal pelo site
2. Abra o banco de dados e atualize o usuário:
```bash
python
>>> from app import create_app, db
>>> from app.models import User
>>> app = create_app()
>>> with app.app_context():
...     user = User.query.filter_by(username='seu_usuario').first()
...     user.is_admin = True
...     db.session.commit()
>>> exit()
```

## 🚀 Próximos Passos - Funcionalidades a Desenvolver

### Parte 2 - Extensões
- [ ] Sistema de plugins/extensões
- [ ] Marketplace de temas
- [ ] Integração com redes sociais

### Parte 3 - Monetização
- [ ] Sistema de ads
- [ ] Integração com Stripe/PayPal
- [ ] Programa de afiliados

### Parte 4 - Compartilhamento
- [ ] Botões de compartilhamento social
- [ ] Sistema de newsletter
- [ ] RSS feed

### Parte 5 - Otimizações
- [ ] Cache (Redis)
- [ ] CDN para assets
- [ ] Compressão de imagens
- [ ] SEO avançado

## 📚 Uso Principal

### Criar um Post
1. Faça login
2. Clique em "Novo Post" na navbar
3. Preencha título, conteúdo e metadados
4. Publique ou salve como rascunho

### Gerenciar Conteúdo
1. Acesse o Admin (se for admin)
2. Dashboard mostra estatísticas
3. Manage Posts/Users/Comments para moderação

### Visualizar Estatísticas
- Clique em "Minhas Estatísticas" na navbar
- Veja posts mais visualizados
- Analise trends dos últimos 30 dias

## 🐛 Troubleshooting

**Erro de "module not found":**
```bash
pip install -r requirements.txt
```

**Banco de dados corrompido:**
```bash
rm blog.db
python run.py
```

**Porta 5000 já em uso:**
```bash
python run.py --port 5001
```

## 📝 Licença

Este projeto está sob licença MIT.

## 👤 Autor

Desenvolvido como um projeto educacional de blog em Flask.

---

**Versão Atual:** 1.0.0  
**Última Atualização:** Dezembro 2025
