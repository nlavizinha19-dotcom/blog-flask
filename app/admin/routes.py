"""Rotas de administração"""
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app.admin import bp
from app.models import Post, User, Category, Tag, Comment, Statistics
from app import db
from functools import wraps

def admin_required(f):
    """Verificar se o usuário é administrador"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or not current_user.is_admin:
            flash('Você não tem permissão para acessar esta página!', 'danger')
            return redirect(url_for('main.index'))
        return f(*args, **kwargs)
    return decorated_function

@bp.route('/')
@login_required
@admin_required
def dashboard():
    """Painel de administração"""
    total_posts = Post.query.count()
    total_users = User.query.count()
    total_comments = Comment.query.count()
    total_views = db.session.query(db.func.sum(Post.views_count)).scalar() or 0
    
    recent_posts = Post.query.order_by(Post.created_at.desc()).limit(5).all()
    recent_comments = Comment.query.order_by(Comment.created_at.desc()).limit(5).all()
    
    stats = {
        'total_posts': total_posts,
        'total_users': total_users,
        'total_comments': total_comments,
        'total_views': total_views
    }
    
    return render_template('admin/dashboard.html', 
                         stats=stats, 
                         recent_posts=recent_posts,
                         recent_comments=recent_comments)

@bp.route('/posts')
@login_required
@admin_required
def manage_posts():
    """Gerenciar posts"""
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.created_at.desc()).paginate(page=page, per_page=20)
    return render_template('admin/manage_posts.html', posts=posts)

@bp.route('/users')
@login_required
@admin_required
def manage_users():
    """Gerenciar usuários"""
    page = request.args.get('page', 1, type=int)
    users = User.query.order_by(User.created_at.desc()).paginate(page=page, per_page=20)
    return render_template('admin/manage_users.html', users=users)

@bp.route('/user/<int:user_id>/toggle-admin', methods=['POST'])
@login_required
@admin_required
def toggle_admin(user_id):
    """Ativar/desativar admin"""
    user = User.query.get_or_404(user_id)
    if user.id == current_user.id:
        flash('Você não pode mudar seu próprio status de admin!', 'danger')
    else:
        user.is_admin = not user.is_admin
        db.session.commit()
        flash(f'Status de admin de {user.username} foi alterado!', 'success')
    return redirect(url_for('admin.manage_users'))

@bp.route('/categories')
@login_required
@admin_required
def manage_categories():
    """Gerenciar categorias"""
    categories = Category.query.all()
    return render_template('admin/manage_categories.html', categories=categories)

@bp.route('/tags')
@login_required
@admin_required
def manage_tags():
    """Gerenciar tags"""
    tags = Tag.query.all()
    return render_template('admin/manage_tags.html', tags=tags)

@bp.route('/comments')
@login_required
@admin_required
def manage_comments():
    """Moderar comentários"""
    page = request.args.get('page', 1, type=int)
    comments = Comment.query.order_by(Comment.created_at.desc()).paginate(page=page, per_page=20)
    return render_template('admin/manage_comments.html', comments=comments)

@bp.route('/comment/<int:comment_id>/approve', methods=['POST'])
@login_required
@admin_required
def approve_comment(comment_id):
    """Aprovar comentário"""
    comment = Comment.query.get_or_404(comment_id)
    comment.is_approved = True
    db.session.commit()
    flash('Comentário aprovado!', 'success')
    return redirect(url_for('admin.manage_comments'))

@bp.route('/comment/<int:comment_id>/reject', methods=['POST'])
@login_required
@admin_required
def reject_comment(comment_id):
    """Rejeitar comentário"""
    comment = Comment.query.get_or_404(comment_id)
    db.session.delete(comment)
    db.session.commit()
    flash('Comentário removido!', 'success')
    return redirect(url_for('admin.manage_comments'))
