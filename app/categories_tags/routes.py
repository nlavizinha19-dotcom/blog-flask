"""Rotas de categorias e tags"""
from flask import render_template, request
from app.categories_tags import bp
from app.models import Category, Tag, Post
from sqlalchemy import desc

@bp.route('/category/<slug>')
def category(slug):
    """Ver posts de uma categoria"""
    category = Category.query.filter_by(slug=slug).first_or_404()
    page = request.args.get('page', 1, type=int)
    
    posts = Post.query.filter(
        Post.categories.contains(category),
        Post.is_published == True
    ).order_by(desc(Post.published_at)).paginate(page=page, per_page=10)
    
    return render_template('categories_tags/category.html', category=category, posts=posts)

@bp.route('/tag/<slug>')
def tag(slug):
    """Ver posts com uma tag"""
    tag = Tag.query.filter_by(slug=slug).first_or_404()
    page = request.args.get('page', 1, type=int)
    
    posts = Post.query.filter(
        Post.tags.contains(tag),
        Post.is_published == True
    ).order_by(desc(Post.published_at)).paginate(page=page, per_page=10)
    
    return render_template('categories_tags/tag.html', tag=tag, posts=posts)

@bp.route('/categories')
def categories_list():
    """Listar todas as categorias"""
    categories = Category.query.all()
    return render_template('categories_tags/categories_list.html', categories=categories)

@bp.route('/tags')
def tags_list():
    """Listar todas as tags"""
    tags = Tag.query.all()
    return render_template('categories_tags/tags_list.html', tags=tags)
