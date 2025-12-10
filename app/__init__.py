"""
Factory para criar e configurar a aplicação Flask
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import config
import os

db = SQLAlchemy()
login_manager = LoginManager()

def create_app(config_name='development'):
    """Cria e configura a aplicação Flask"""
    app = Flask(__name__, static_folder='static', template_folder='templates')
    
    # Carrega configuração
    app.config.from_object(config[config_name])
    
    # Inicializa extensões
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'users.login'
    login_manager.login_message = 'Por favor, faça login para acessar esta página.'
    
    # Cria pasta de uploads se não existir
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    
    # Registra blueprints
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
    
    from app.users import bp as users_bp
    app.register_blueprint(users_bp)
    
    from app.posts import bp as posts_bp
    app.register_blueprint(posts_bp)
    
    from app.categories_tags import bp as categories_tags_bp
    app.register_blueprint(categories_tags_bp)
    
    from app.comments import bp as comments_bp
    app.register_blueprint(comments_bp)
    
    from app.admin import bp as admin_bp
    app.register_blueprint(admin_bp, url_prefix='/admin')
    
    from app.design import bp as design_bp
    app.register_blueprint(design_bp, url_prefix='/design')
    
    from app.search import bp as search_bp
    app.register_blueprint(search_bp)
    
    from app.stats import bp as stats_bp
    app.register_blueprint(stats_bp)
    
    from app.files import bp as files_bp
    app.register_blueprint(files_bp)
    
    # Importa modelos
    from app.models import User, Post, Category, Tag, Comment, Statistics, Theme
    
    # User loader
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    # Criar tabelas
    with app.app_context():
        db.create_all()
    
    return app
