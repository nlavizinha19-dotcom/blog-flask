"""Rotas de busca"""
from flask import render_template, request
from app.search import bp
from app.models import Post
from sqlalchemy import or_, desc

@bp.route('/search')
def search():
    """Buscar posts"""
    query = request.args.get('q', '')
    page = request.args.get('page', 1, type=int)
    
    if len(query) < 2:
        posts = None
    else:
        posts = Post.query.filter(
            or_(
                Post.title.ilike(f'%{query}%'),
                Post.content.ilike(f'%{query}%'),
                Post.summary.ilike(f'%{query}%')
            ),
            Post.is_published == True
        ).order_by(desc(Post.published_at)).paginate(page=page, per_page=10)
    
    return render_template('search/search.html', posts=posts, query=query)
