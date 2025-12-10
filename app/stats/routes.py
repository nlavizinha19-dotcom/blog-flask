"""Rotas de estatísticas"""
from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user
from app.stats import bp
from app.models import Post, Statistics
from app import db
from datetime import datetime, timedelta

@bp.route('/my-stats')
@login_required
def my_stats():
    """Estatísticas dos posts do usuário"""
    # Posts do usuário
    posts = current_user.posts.all()
    
    # Total de views
    total_views = db.session.query(db.func.sum(Post.views_count)).filter(
        Post.author_id == current_user.id
    ).scalar() or 0
    
    # Posts mais visualizados
    top_posts = Post.query.filter_by(author_id=current_user.id).order_by(
        Post.views_count.desc()
    ).limit(10).all()
    
    # Estatísticas dos últimos 30 dias
    thirty_days_ago = datetime.utcnow() - timedelta(days=30)
    recent_stats = Statistics.query.filter(
        Statistics.post_id.in_([p.id for p in posts]),
        Statistics.viewed_at >= thirty_days_ago
    ).all()
    
    views_by_day = {}
    for stat in recent_stats:
        day = stat.viewed_at.strftime('%Y-%m-%d')
        views_by_day[day] = views_by_day.get(day, 0) + 1
    
    return render_template('stats/my_stats.html',
                         posts=posts,
                         total_views=total_views,
                         top_posts=top_posts,
                         views_by_day=views_by_day)

@bp.route('/post/<int:post_id>/stats')
@login_required
def post_stats(post_id):
    """Estatísticas de um post específico"""
    post = Post.query.get_or_404(post_id)
    
    if post.author_id != current_user.id and not current_user.is_admin:
        return redirect(url_for('main.index'))
    
    # Estatísticas detalhadas
    stats = Statistics.query.filter_by(post_id=post_id).order_by(
        Statistics.viewed_at.desc()
    ).all()
    
    # Mapa de países (simplificado)
    countries = {}
    browsers = {}
    
    for stat in stats:
        # Agrupar por user agent
        ua = stat.user_agent or 'Unknown'
        browsers[ua] = browsers.get(ua, 0) + 1
    
    return render_template('stats/post_stats.html',
                         post=post,
                         stats=stats,
                         browsers=browsers)
