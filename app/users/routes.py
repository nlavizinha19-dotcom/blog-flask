"""Rotas de usuários"""
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from app.users import bp
from app.models import User
from app import db

@bp.route('/register', methods=['GET', 'POST'])
def register():
    """Registrar novo usuário"""
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        
        # Validações
        if User.query.filter_by(username=username).first():
            flash('Usuário já existe!', 'danger')
            return redirect(url_for('users.register'))
        
        if User.query.filter_by(email=email).first():
            flash('Email já cadastrado!', 'danger')
            return redirect(url_for('users.register'))
        
        if password != confirm_password:
            flash('As senhas não correspondem!', 'danger')
            return redirect(url_for('users.register'))
        
        # Criar novo usuário
        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        
        flash('Conta criada com sucesso! Faça login.', 'success')
        return redirect(url_for('users.login'))
    
    return render_template('users/register.html')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    """Fazer login"""
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        remember = request.form.get('remember', False)
        
        user = User.query.filter_by(username=username).first()
        
        if user is None or not user.check_password(password):
            flash('Usuário ou senha inválidos!', 'danger')
            return redirect(url_for('users.login'))
        
        if not user.is_active:
            flash('Sua conta foi desativada!', 'danger')
            return redirect(url_for('users.login'))
        
        login_user(user, remember=remember)
        next_page = request.args.get('next')
        return redirect(next_page) if next_page else redirect(url_for('main.index'))
    
    return render_template('users/login.html')

@bp.route('/logout')
@login_required
def logout():
    """Fazer logout"""
    logout_user()
    flash('Você foi desconectado!', 'info')
    return redirect(url_for('main.index'))

@bp.route('/profile/<username>')
def profile(username):
    """Perfil do usuário"""
    user = User.query.filter_by(username=username).first_or_404()
    page = request.args.get('page', 1, type=int)
    posts = user.posts.filter_by(is_published=True).paginate(page=page, per_page=10)
    return render_template('users/profile.html', user=user, posts=posts)

@bp.route('/profile/edit', methods=['GET', 'POST'])
@login_required
def edit_profile():
    """Editar perfil"""
    if request.method == 'POST':
        current_user.first_name = request.form.get('first_name', '')
        current_user.last_name = request.form.get('last_name', '')
        current_user.bio = request.form.get('bio', '')
        db.session.commit()
        flash('Perfil atualizado com sucesso!', 'success')
        return redirect(url_for('users.profile', username=current_user.username))
    
    return render_template('users/edit_profile.html')
