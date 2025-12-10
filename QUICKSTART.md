# 🚀 GUIA RÁPIDO - COMEÇAR COM O BLOG FLASK

## ⚡ Início Rápido (5 minutos)

### 1️⃣ Preparar o Ambiente

```powershell
# Navegue até a pasta do projeto
cd c:\Users\User\Documents\natiele\blog-flask

# Crie um ambiente virtual
python -m venv venv

# Ative o ambiente virtual
.\venv\Scripts\Activate.ps1
```

### 2️⃣ Instalar Dependências

```powershell
pip install -r requirements.txt
```

### 3️⃣ Executar a Aplicação

```powershell
python run.py
```

A aplicação estará disponível em: **http://localhost:5000**

---

## 📝 Primeiro Uso

### Criar Conta de Usuário

1. Acesse http://localhost:5000
2. Clique em **"Registrar"** no menu superior
3. Preencha os dados:
   - Usuário: `seu_usuario`
   - Email: `seu_email@exemplo.com`
   - Senha: `sua_senha`
4. Clique em **"Registrar"**

### Fazer Login

1. Clique em **"Login"**
2. Digite seu usuário e senha
3. Clique em **"Entrar"**

### Criar Seu Primeiro Post

1. Após login, clique em **"Novo Post"** na navbar
2. Preencha:
   - **Título**: ex. "Meu Primeiro Post"
   - **Resumo**: Uma descrição curta
   - **Conteúdo**: O artigo completo
3. Selecione **"Publicar agora"**
4. Clique em **"Criar Post"**

---

## 🛠️ Funcionalidades Principais

### 🏠 Página Inicial
- Ver todos os posts publicados
- Posts em destaque
- Busca de posts
- Filtrar por categorias

### 📝 Posts
- Criar, editar e deletar posts
- Publicar ou salvar como rascunho
- Adicionar categorias e tags
- Upload de imagens em destaque

### 💬 Comentários
- Deixar comentários em posts
- Editar seus comentários
- Deletar comentários
- Sistema de respostas (em desenvolvimento)

### 👥 Usuários
- Criar conta
- Fazer login/logout
- Editar perfil
- Ver perfil de outros usuários

### 🛡️ Painel Admin

Para usar o painel admin:

1. **Tornar seu usuário admin** (via banco de dados):
```python
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

2. Acesse **http://localhost:5000/admin**
3. Você verá o dashboard com:
   - Estatísticas
   - Gerenciar posts, usuários, comentários
   - Gerenciar categorias e tags
   - Customizador de temas

---

## 📁 Estrutura de Pastas

```
blog-flask/
├── app/                          # Código principal
│   ├── main/                     # Página inicial
│   ├── users/                    # Autenticação
│   ├── posts/                    # Publicação
│   ├── comments/                 # Comentários
│   ├── categories_tags/          # Organização
│   ├── admin/                    # Admin
│   ├── design/                   # Temas
│   ├── search/                   # Busca
│   ├── stats/                    # Estatísticas
│   ├── files/                    # Arquivos
│   ├── templates/                # HTML
│   └── static/                   # CSS, JS, imagens
├── config.py                     # Configurações
├── run.py                        # Executar app
├── requirements.txt              # Dependências
├── README.md                     # Documentação
└── DEVELOPMENT.md                # Guia de desenvolvimento
```

---

## 🔑 Variáveis de Ambiente

Edite `.env` para customizar:

```
FLASK_APP=run.py
FLASK_ENV=development
SECRET_KEY=sua-chave-secreta-aqui
DATABASE_URL=sqlite:///blog.db
```

---

## 🐛 Problemas Comuns

### "ModuleNotFoundError: No module named 'flask'"

**Solução:**
```powershell
pip install -r requirements.txt
```

### "Port 5000 already in use"

**Solução:**
```powershell
# Usar outra porta
python run.py --port 5001
```

### "Database is locked"

**Solução:**
```powershell
# Deletar banco de dados e recriar
rm blog.db
python run.py
```

---

## 📚 Próximos Passos

Após explorar a aplicação:

1. Leia `README.md` para documentação completa
2. Leia `DEVELOPMENT.md` para próximas funcionalidades
3. Customize cores e tema em `/design/themes`
4. Adicione categorias e tags no admin
5. Crie posts de exemplo

---

## 🎓 Dicas

### Criar Dados de Teste

```python
python
>>> from app import create_app, db
>>> from app.models import *
>>> from datetime import datetime
>>> app = create_app()
>>> with app.app_context():
...     # Criar usuário
...     user = User(username='teste', email='teste@test.com')
...     user.set_password('senha123')
...     db.session.add(user)
...     
...     # Criar categoria
...     cat = Category(name='Tecnologia', slug='tecnologia')
...     db.session.add(cat)
...     
...     db.session.commit()
...     print("Dados criados!")
>>> exit()
```

### Ver Posts no Shell

```python
python
>>> from app import create_app
>>> from app.models import Post
>>> app = create_app()
>>> with app.app_context():
...     posts = Post.query.all()
...     for p in posts:
...         print(f"- {p.title} ({p.views_count} views)")
>>> exit()
```

---

## 🆘 Suporte

Se tiver problemas:

1. Verifique se o venv está ativado
2. Verifique se todas as dependências foram instaladas
3. Verifique o console Flask para mensagens de erro
4. Limpe o cache do navegador (Ctrl+Shift+Delete)
5. Reinicie a aplicação

---

## 🎉 Parabéns!

Você já tem um blog funcional! Agora explore as funcionalidades e comece a publicar conteúdo.

**Versão:** 1.0.0  
**Última Atualização:** Dezembro 2025
