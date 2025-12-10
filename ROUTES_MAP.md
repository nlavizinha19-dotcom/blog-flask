# 🗺️ MAPA DE NAVEGAÇÃO - BLOG FLASK

## 📍 Onde Encontrar Cada Funcionalidade

### 🏠 PÁGINA INICIAL
- **URL**: http://localhost:5000/
- **Template**: `app/templates/index.html`
- **Rota**: `app/main/routes.py` - `index()`
- **O que vê**: Posts recentes, posts destacados, busca, categorias

---

### 👤 USUÁRIOS - AUTENTICAÇÃO

#### Registrar
- **URL**: http://localhost:5000/register
- **Template**: `app/templates/users/register.html`
- **Rota**: `app/users/routes.py` - `register()`
- **Função**: Criar nova conta

#### Login
- **URL**: http://localhost:5000/login
- **Template**: `app/templates/users/login.html`
- **Rota**: `app/users/routes.py` - `login()`
- **Função**: Autenticar usuário

#### Logout
- **URL**: http://localhost:5000/logout
- **Rota**: `app/users/routes.py` - `logout()`
- **Função**: Sair da conta

#### Perfil
- **URL**: http://localhost:5000/profile/<username>
- **Template**: `app/templates/users/profile.html`
- **Rota**: `app/users/routes.py` - `profile()`
- **Função**: Ver posts do usuário

#### Editar Perfil
- **URL**: http://localhost:5000/profile/edit
- **Template**: `app/templates/users/edit_profile.html`
- **Rota**: `app/users/routes.py` - `edit_profile()`
- **Função**: Atualizar informações pessoais

---

### ✍️ POSTS

#### Novo Post
- **URL**: http://localhost:5000/post/new
- **Template**: `app/templates/posts/new_post.html`
- **Rota**: `app/posts/routes.py` - `new_post()`
- **Função**: Criar post
- **Requer**: Login

#### Visualizar Post
- **URL**: http://localhost:5000/post/<slug>
- **Template**: `app/templates/posts/view_post.html`
- **Rota**: `app/posts/routes.py` - `view_post()`
- **Função**: Ler artigo completo com comentários

#### Editar Post
- **URL**: http://localhost:5000/post/<slug>/edit
- **Rota**: `app/posts/routes.py` - `edit_post()`
- **Função**: Modificar post
- **Requer**: Ser autor ou admin

#### Deletar Post
- **URL**: http://localhost:5000/post/<slug>/delete
- **Rota**: `app/posts/routes.py` - `delete_post()`
- **Função**: Remover post
- **Requer**: Ser autor ou admin

---

### 📂 CATEGORIAS & TAGS

#### Listar Categorias
- **URL**: http://localhost:5000/categories
- **Template**: `app/templates/categories_tags/categories_list.html`
- **Rota**: `app/categories_tags/routes.py` - `categories_list()`
- **Função**: Ver todas as categorias

#### Ver Categoria
- **URL**: http://localhost:5000/category/<slug>
- **Template**: `app/templates/categories_tags/category.html`
- **Rota**: `app/categories_tags/routes.py` - `category()`
- **Função**: Ver posts de uma categoria

#### Ver Tag
- **URL**: http://localhost:5000/tag/<slug>
- **Template**: `app/templates/categories_tags/tag.html`
- **Rota**: `app/categories_tags/routes.py` - `tag()`
- **Função**: Ver posts com uma tag

#### Listar Tags
- **URL**: http://localhost:5000/tags
- **Template**: `app/templates/categories_tags/tags_list.html`
- **Rota**: `app/categories_tags/routes.py` - `tags_list()`
- **Função**: Ver todas as tags

---

### 💬 COMENTÁRIOS

#### Adicionar Comentário
- **URL**: http://localhost:5000/post/<slug>/comment/add
- **Rota**: `app/comments/routes.py` - `add_comment()`
- **Função**: Deixar comentário em post
- **Requer**: Login

#### Editar Comentário
- **URL**: http://localhost:5000/comment/<id>/edit
- **Rota**: `app/comments/routes.py` - `edit_comment()`
- **Função**: Modificar comentário
- **Requer**: Ser autor

#### Deletar Comentário
- **URL**: http://localhost:5000/comment/<id>/delete
- **Rota**: `app/comments/routes.py` - `delete_comment()`
- **Função**: Remover comentário
- **Requer**: Ser autor ou admin

---

### 🔍 BUSCA

#### Buscar Posts
- **URL**: http://localhost:5000/search?q=termo
- **Template**: `app/templates/search/search.html`
- **Rota**: `app/search/routes.py` - `search()`
- **Função**: Buscar posts por termo
- **Busca em**: Título, conteúdo, resumo

---

### 📊 ESTATÍSTICAS

#### Minhas Estatísticas
- **URL**: http://localhost:5000/stats/my-stats
- **Template**: `app/templates/stats/my_stats.html`
- **Rota**: `app/stats/routes.py` - `my_stats()`
- **Função**: Ver análise de meus posts
- **Requer**: Login

#### Estatísticas do Post
- **URL**: http://localhost:5000/stats/post/<post_id>/stats
- **Template**: `app/templates/stats/post_stats.html`
- **Rota**: `app/stats/routes.py` - `post_stats()`
- **Função**: Análise detalhada de um post
- **Requer**: Ser autor ou admin

---

### 📁 ARQUIVOS

#### Upload de Arquivo
- **URL**: http://localhost:5000/upload
- **Template**: `app/templates/files/upload.html`
- **Rota**: `app/files/routes.py` - `upload_file()`
- **Função**: Enviar arquivo
- **Requer**: Login

#### Meus Arquivos
- **URL**: http://localhost:5000/my-files
- **Template**: `app/templates/files/my_files.html`
- **Rota**: `app/files/routes.py` - `my_files()`
- **Função**: Listar meus uploads
- **Requer**: Login

#### Download
- **URL**: http://localhost:5000/download/<filename>
- **Rota**: `app/files/routes.py` - `download_file()`
- **Função**: Baixar arquivo
- **Requer**: Login

#### Deletar Arquivo
- **URL**: http://localhost:5000/delete/<filename>
- **Rota**: `app/files/routes.py` - `delete_file()`
- **Função**: Remover arquivo
- **Requer**: Login

---

### 🛡️ PAINEL ADMINISTRATIVO

#### Dashboard Admin
- **URL**: http://localhost:5000/admin/
- **Template**: `app/templates/admin/dashboard.html`
- **Rota**: `app/admin/routes.py` - `dashboard()`
- **Função**: Dashboard com estatísticas
- **Requer**: Admin
- **Mostra**: Total de posts, usuários, comentários, views

#### Gerenciar Posts
- **URL**: http://localhost:5000/admin/posts
- **Template**: `app/templates/admin/manage_posts.html`
- **Rota**: `app/admin/routes.py` - `manage_posts()`
- **Função**: CRUD de posts
- **Requer**: Admin

#### Gerenciar Usuários
- **URL**: http://localhost:5000/admin/users
- **Template**: `app/templates/admin/manage_users.html`
- **Rota**: `app/admin/routes.py` - `manage_users()`
- **Função**: Gerenciar usuários, dar admin
- **Requer**: Admin

#### Gerenciar Comentários
- **URL**: http://localhost:5000/admin/comments
- **Template**: `app/templates/admin/manage_comments.html`
- **Rota**: `app/admin/routes.py` - `manage_comments()`
- **Função**: Moderar comentários
- **Requer**: Admin

#### Gerenciar Categorias
- **URL**: http://localhost:5000/admin/categories
- **Template**: `app/templates/admin/manage_categories.html`
- **Rota**: `app/admin/routes.py` - `manage_categories()`
- **Função**: CRUD de categorias
- **Requer**: Admin

#### Gerenciar Tags
- **URL**: http://localhost:5000/admin/tags
- **Template**: `app/templates/admin/manage_tags.html`
- **Rota**: `app/admin/routes.py` - `manage_tags()`
- **Função**: CRUD de tags
- **Requer**: Admin

---

### 🎨 DESIGN & TEMAS

#### Listar Temas
- **URL**: http://localhost:5000/design/themes
- **Template**: `app/templates/design/list_themes.html`
- **Rota**: `app/design/routes.py` - `list_themes()`
- **Função**: Ver temas disponíveis

#### Ativar Tema
- **URL**: http://localhost:5000/design/theme/<id>/activate
- **Rota**: `app/design/routes.py` - `activate_theme()`
- **Função**: Ativar tema
- **Requer**: Admin

#### Customizador
- **URL**: http://localhost:5000/design/customizer
- **Template**: `app/templates/design/customizer.html`
- **Rota**: `app/design/routes.py` - `customizer()`
- **Função**: Personalizar cores
- **Requer**: Admin

---

## 🗂️ ESTRUTURA DE ARQUIVOS RESUMIDA

```
blog-flask/
│
├── 📄 DOCUMENTAÇÃO
│   ├── README.md              # Docs principal
│   ├── QUICKSTART.md          # Guia rápido
│   ├── DEVELOPMENT.md         # Roadmap
│   ├── SUMMARY.md             # Sumário
│   └── CHECKLIST.md           # Este arquivo
│
├── 🔧 CONFIGURAÇÃO
│   ├── config.py              # Configs da app
│   ├── requirements.txt        # Dependências
│   ├── .env.example            # Variáveis de ambiente
│   └── .gitignore              # Git ignore
│
├── 🚀 EXECUÇÃO
│   └── run.py                 # Script principal
│
└── 📁 app/
    ├── __init__.py            # Factory
    ├── models.py              # Modelos BD
    │
    ├── main/                  # Home
    │   ├── __init__.py
    │   └── routes.py
    │
    ├── users/                 # Auth
    │   ├── __init__.py
    │   └── routes.py
    │
    ├── posts/                 # Posts
    │   ├── __init__.py
    │   └── routes.py
    │
    ├── comments/              # Comentários
    │   ├── __init__.py
    │   └── routes.py
    │
    ├── categories_tags/       # Org. conteúdo
    │   ├── __init__.py
    │   └── routes.py
    │
    ├── admin/                 # Admin
    │   ├── __init__.py
    │   └── routes.py
    │
    ├── design/                # Temas
    │   ├── __init__.py
    │   └── routes.py
    │
    ├── search/                # Busca
    │   ├── __init__.py
    │   └── routes.py
    │
    ├── stats/                 # Stats
    │   ├── __init__.py
    │   └── routes.py
    │
    ├── files/                 # Arquivos
    │   ├── __init__.py
    │   └── routes.py
    │
    ├── templates/             # HTML
    │   ├── base.html
    │   ├── index.html
    │   ├── users/
    │   ├── posts/
    │   ├── admin/
    │   ├── design/
    │   ├── search/
    │   ├── stats/
    │   └── categories_tags/
    │
    └── static/                # Assets
        └── css/
            └── style.css
```

---

## 🔑 MODELO DE DADOS

```
User (1) ──→ (∞) Post
     │               │
     ├─→ (∞) Comment │
     │         ↓     │
     │       (1) ────┘
     │
     └─→ (∞) Statistics

Category (1) ←──→ (∞) Post (M2M)
Tag (1) ←──→ (∞) Post (M2M)

Post (1) ──→ (∞) Comment
     │
     └─→ (1) Category
     └─→ (∞) Tag

Comment (1) ──→ (∞) Comment (Self-referencing)

Theme (1) ──→ (1) Active Theme
```

---

## ⌨️ COMANDOS ÚTEIS

### Executar Aplicação
```bash
python run.py
```

### Shell Flask
```bash
python
>>> from app import create_app, db
>>> from app.models import *
>>> app = create_app()
```

### Criar Admin
```python
>>> with app.app_context():
...     user = User.query.filter_by(username='seu_user').first()
...     user.is_admin = True
...     db.session.commit()
```

---

## 🎯 RESUMO RÁPIDO

| O que Fazer | Onde Ir | Requer |
|---|---|---|
| Ver posts | / | Nada |
| Registrar | /register | Nada |
| Fazer login | /login | Nada |
| Novo post | /post/new | Login |
| Ver meus posts | /profile/seu_user | Login |
| Buscar | /search | Nada |
| Admin | /admin | Admin |
| Temas | /design/themes | Nada |

---

**Versão**: 1.0.0  
**Data**: Dezembro 2025  
**Status**: ✅ Completo
