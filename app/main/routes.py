"""Rotas principais"""
from flask import render_template, request
from app.main import bp
from app.models import Post, Category
from app import db
from sqlalchemy import desc

@bp.route('/')
@bp.route('/index')
def index():
    """Página inicial com posts mais recentes"""
    page = request.args.get('page', 1, type=int)
    posts = Post.query.filter_by(is_published=True).order_by(
        desc(Post.published_at)
    ).paginate(page=page, per_page=10)
    
    featured_posts = Post.query.filter_by(
        is_published=True, 
        is_featured=True
    ).limit(3).all()
    
    categories = Category.query.all()
    
    return render_template('index.html', 
                         posts=posts, 
                         featured_posts=featured_posts,
                         categories=categories)

@bp.route('/about')
def about():
    """Página sobre o blog"""
    return render_template('about.html')

@bp.route('/contact', methods=['GET', 'POST'])
def contact():
    """Página de contato"""
    if request.method == 'POST':
        # Implementar envio de email
        pass
    return render_template('contact.html')
