# 🔧 COMO RESOLVER OS ERROS DE IMPORTAÇÃO

## ❌ Problema

Você está vendo erros de importação no VS Code como:
```
Import "flask_login" could not be resolved
Import "flask_sqlalchemy" could not be resolved
```

## ✅ Solução

### 1️⃣ Instale as Dependências

Execute no terminal:

```powershell
# Ative o ambiente virtual
.\venv\Scripts\Activate.ps1

# Instale as dependências
pip install -r requirements.txt
```

### 2️⃣ Recarregue o VS Code

Após instalar, você pode:

**Opção A**: Feche e reabra o VS Code

**Opção B**: Pressione `Ctrl+Shift+P` e digite:
```
Python: Select Interpreter
```
Escolha o Python do seu venv.

**Opção C**: Clique em "Reload Window"
- Pressione: `Ctrl+Shift+P`
- Digite: `reload window`
- Pressione Enter

### 3️⃣ Verifique se Foi Resolvido

Abra qualquer arquivo Python e veja se os erros desapareceram.

---

## 📋 Lista de Dependências Instaladas

Ao executar `pip install -r requirements.txt`, estes pacotes serão instalados:

- ✅ Flask==3.0.0
- ✅ Flask-SQLAlchemy==3.1.1
- ✅ Flask-Login==0.6.3
- ✅ Flask-WTF==1.2.1
- ✅ WTForms==3.1.1
- ✅ python-dotenv==1.0.0
- ✅ Werkzeug==3.0.1
- ✅ Jinja2==3.1.2
- ✅ MarkupSafe==2.1.3
- ✅ itsdangerous==2.1.2
- ✅ click==8.1.7
- ✅ Pillow==10.1.0
- ✅ slugify==0.0.1
- ✅ PyYAML==6.0.1

---

## 🎯 Erros que Devem Desaparecer

Após instalar e recarregar:

❌ ~~Import "flask_login" could not be resolved~~  
❌ ~~Import "flask_sqlalchemy" could not be resolved~~  
❌ ~~Import "sqlalchemy" could not be resolved~~  
❌ ~~Import "slugify" could not be resolved~~  

✅ Todos resolvidos!

---

## 💡 Dica: Verificar Instalação

Se quiser verificar se tudo foi instalado corretamente:

```powershell
# Ative o venv
.\venv\Scripts\Activate.ps1

# Teste as importações
python -c "import flask; import flask_login; import flask_sqlalchemy; print('✅ Tudo OK!')"
```

Se tiver erros, execute novamente:
```bash
pip install -r requirements.txt
```

---

## ⚠️ Problemas Comuns

### "ModuleNotFoundError: No module named..."
Significa que o venv não está ativado ou a dependência não foi instalada.

**Solução**:
1. Ative: `.\venv\Scripts\Activate.ps1`
2. Instale: `pip install -r requirements.txt`
3. Recarregue VS Code

### "python not found"
Significa que Python não está instalado ou não está no PATH.

**Solução**:
- Instale Python 3.7+ de https://python.org
- Ou use: `py -m venv venv`

---

## ✨ Depois de Resolver

Os erros de importação desaparecerão e você poderá:
- ✅ Ver autocomplete do código
- ✅ Navegar para definições
- ✅ Executar a aplicação sem erros
- ✅ Usar o debugger

---

**Pronto! Agora execute:**

```bash
python run.py
```

---

Criado: Dezembro 2025
