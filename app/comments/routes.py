"""Rotas de comentários"""
from flask import render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user
from app.comments import bp
from app.models import Comment, Post
from app import db

@bp.route('/post/<slug>/comment/add', methods=['POST'])
@login_required
def add_comment(slug):
    """Adicionar comentário a um post"""
    post = Post.query.filter_by(slug=slug).first_or_404()
    
    content = request.form.get('content')
    parent_id = request.form.get('parent_id')
    
    if not content or len(content.strip()) == 0:
        flash('Comentário não pode estar vazio!', 'danger')
        return redirect(url_for('posts.view_post', slug=slug))
    
    comment = Comment(
        content=content,
        author_id=current_user.id,
        post_id=post.id,
        parent_id=parent_id if parent_id else None,
        is_approved=True  # Implementar moderação após
    )
    
    db.session.add(comment)
    db.session.commit()
    
    flash('Comentário adicionado com sucesso!', 'success')
    return redirect(url_for('posts.view_post', slug=slug))

@bp.route('/comment/<int:comment_id>/delete', methods=['POST'])
@login_required
def delete_comment(comment_id):
    """Deletar comentário"""
    comment = Comment.query.get_or_404(comment_id)
    post_slug = comment.post.slug
    
    if comment.author_id != current_user.id and not current_user.is_admin:
        flash('Você não tem permissão para deletar este comentário!', 'danger')
        return redirect(url_for('posts.view_post', slug=post_slug))
    
    db.session.delete(comment)
    db.session.commit()
    
    flash('Comentário deletado com sucesso!', 'success')
    return redirect(url_for('posts.view_post', slug=post_slug))

@bp.route('/comment/<int:comment_id>/edit', methods=['POST'])
@login_required
def edit_comment(comment_id):
    """Editar comentário"""
    comment = Comment.query.get_or_404(comment_id)
    
    if comment.author_id != current_user.id and not current_user.is_admin:
        flash('Você não tem permissão para editar este comentário!', 'danger')
        return redirect(url_for('posts.view_post', slug=comment.post.slug))
    
    content = request.form.get('content')
    
    if not content or len(content.strip()) == 0:
        flash('Comentário não pode estar vazio!', 'danger')
        return redirect(url_for('posts.view_post', slug=comment.post.slug))
    
    comment.content = content
    db.session.commit()
    
    flash('Comentário atualizado com sucesso!', 'success')
    return redirect(url_for('posts.view_post', slug=comment.post.slug))
