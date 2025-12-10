"""Rotas de design e temas"""
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app.design import bp
from app.models import Theme
from app import db

@bp.route('/themes')
def list_themes():
    """Listar temas disponíveis"""
    themes = Theme.query.all()
    active_theme = Theme.query.filter_by(is_active=True).first()
    return render_template('design/list_themes.html', themes=themes, active_theme=active_theme)

@bp.route('/theme/<int:theme_id>/activate', methods=['POST'])
@login_required
def activate_theme(theme_id):
    """Ativar um tema"""
    if not current_user.is_admin:
        flash('Você não tem permissão para fazer isto!', 'danger')
        return redirect(url_for('design.list_themes'))
    
    # Desativar todos os temas
    Theme.query.update({Theme.is_active: False})
    
    # Ativar o tema selecionado
    theme = Theme.query.get_or_404(theme_id)
    theme.is_active = True
    db.session.commit()
    
    flash(f'Tema {theme.name} foi ativado!', 'success')
    return redirect(url_for('design.list_themes'))

@bp.route('/customizer')
@login_required
def customizer():
    """Customizador de temas"""
    if not current_user.is_admin:
        flash('Você não tem permissão para fazer isto!', 'danger')
        return redirect(url_for('main.index'))
    
    active_theme = Theme.query.filter_by(is_active=True).first()
    return render_template('design/customizer.html', active_theme=active_theme)

@bp.route('/customizer/update', methods=['POST'])
@login_required
def update_customizer():
    """Atualizar customização"""
    if not current_user.is_admin:
        flash('Você não tem permissão para fazer isto!', 'danger')
        return redirect(url_for('main.index'))
    
    active_theme = Theme.query.filter_by(is_active=True).first()
    
    if active_theme:
        active_theme.primary_color = request.form.get('primary_color', active_theme.primary_color)
        active_theme.secondary_color = request.form.get('secondary_color', active_theme.secondary_color)
        active_theme.accent_color = request.form.get('accent_color', active_theme.accent_color)
        active_theme.font_family = request.form.get('font_family', active_theme.font_family)
        db.session.commit()
        flash('Tema atualizado com sucesso!', 'success')
    
    return redirect(url_for('design.customizer'))
