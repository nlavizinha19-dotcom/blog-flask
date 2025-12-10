"""Rotas de posts"""
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app.posts import bp
from app.models import Post, Category, Tag, Statistics
from app import db
from slugify import slugify
from datetime import datetime

@bp.route('/post/new', methods=['GET', 'POST'])
@login_required
def new_post():
    """Criar novo post"""
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        summary = request.form.get('summary')
        is_published = request.form.get('is_published') == 'on'
        
        slug = slugify(title)
        
        # Verificar se slug já existe
        if Post.query.filter_by(slug=slug).first():
            flash('Um post com este título já existe!', 'danger')
            return redirect(url_for('posts.new_post'))
        
        post = Post(
            title=title,
            slug=slug,
            content=content,
            summary=summary,
            author_id=current_user.id,
            is_published=is_published,
            published_at=datetime.utcnow() if is_published else None
        )
        
        db.session.add(post)
        db.session.commit()
        
        flash('Post criado com sucesso!', 'success')
        return redirect(url_for('posts.view_post', slug=post.slug))
    
    categories = Category.query.all()
    tags = Tag.query.all()
    return render_template('posts/new_post.html', categories=categories, tags=tags)

@bp.route('/post/<slug>', methods=['GET'])
def view_post(slug):
    """Visualizar um post"""
    post = Post.query.filter_by(slug=slug).first_or_404()
    
    # Registrar visualização
    if request.remote_addr:
        stat = Statistics(
            post_id=post.id,
            visitor_ip=request.remote_addr,
            user_agent=request.headers.get('User-Agent', ''),
            referrer=request.referrer
        )
        db.session.add(stat)
        post.views_count += 1
        db.session.commit()
    
    return render_template('posts/view_post.html', post=post)

@bp.route('/post/<slug>/edit', methods=['GET', 'POST'])
@login_required
def edit_post(slug):
    """Editar um post"""
    post = Post.query.filter_by(slug=slug).first_or_404()
    
    if post.author_id != current_user.id and not current_user.is_admin:
        flash('Você não tem permissão para editar este post!', 'danger')
        return redirect(url_for('posts.view_post', slug=slug))
    
    if request.method == 'POST':
        post.title = request.form.get('title')
        post.content = request.form.get('content')
        post.summary = request.form.get('summary')
        post.is_published = request.form.get('is_published') == 'on'
        post.is_featured = request.form.get('is_featured') == 'on'
        
        if post.is_published and not post.published_at:
            post.published_at = datetime.utcnow()
        
        db.session.commit()
        flash('Post atualizado com sucesso!', 'success')
        return redirect(url_for('posts.view_post', slug=post.slug))
    
    categories = Category.query.all()
    tags = Tag.query.all()
    return render_template('posts/edit_post.html', post=post, categories=categories, tags=tags)

@bp.route('/post/<slug>/delete', methods=['POST'])
@login_required
def delete_post(slug):
    """Deletar um post"""
    post = Post.query.filter_by(slug=slug).first_or_404()
    
    if post.author_id != current_user.id and not current_user.is_admin:
        flash('Você não tem permissão para deletar este post!', 'danger')
        return redirect(url_for('posts.view_post', slug=slug))
    
    db.session.delete(post)
    db.session.commit()
    flash('Post deletado com sucesso!', 'success')
    return redirect(url_for('main.index'))
