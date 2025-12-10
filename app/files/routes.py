"""Rotas de gerenciamento de arquivos"""
from flask import render_template, request, redirect, url_for, flash, send_file, current_app
from flask_login import login_required, current_user
from app.files import bp
from app import db
from werkzeug.utils import secure_filename
import os

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'doc', 'docx', 'zip'}

def allowed_file(filename):
    """Verificar extensão do arquivo"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@bp.route('/upload', methods=['GET', 'POST'])
@login_required
def upload_file():
    """Fazer upload de arquivo"""
    if request.method == 'POST':
        # Verificar se arquivo foi enviado
        if 'file' not in request.files:
            flash('Nenhum arquivo selecionado!', 'danger')
            return redirect(request.url)
        
        file = request.files['file']
        
        if file.filename == '':
            flash('Nenhum arquivo selecionado!', 'danger')
            return redirect(request.url)
        
        if not allowed_file(file.filename):
            flash('Tipo de arquivo não permitido!', 'danger')
            return redirect(request.url)
        
        # Salvar arquivo
        filename = secure_filename(file.filename)
        # Adicionar timestamp ao nome para evitar conflitos
        import time
        filename = f"{int(time.time())}_{filename}"
        
        try:
            file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
            flash(f'Arquivo {file.filename} enviado com sucesso!', 'success')
            return redirect(url_for('files.my_files'))
        except Exception as e:
            flash(f'Erro ao fazer upload: {str(e)}', 'danger')
            return redirect(request.url)
    
    return render_template('files/upload.html')

@bp.route('/my-files')
@login_required
def my_files():
    """Listar arquivos do usuário"""
    upload_folder = current_app.config['UPLOAD_FOLDER']
    files = []
    
    if os.path.exists(upload_folder):
        files = os.listdir(upload_folder)
    
    return render_template('files/my_files.html', files=files)

@bp.route('/download/<filename>')
@login_required
def download_file(filename):
    """Baixar arquivo"""
    filename = secure_filename(filename)
    upload_folder = current_app.config['UPLOAD_FOLDER']
    filepath = os.path.join(upload_folder, filename)
    
    if os.path.exists(filepath):
        return send_file(filepath, as_attachment=True)
    else:
        flash('Arquivo não encontrado!', 'danger')
        return redirect(url_for('files.my_files'))

@bp.route('/delete/<filename>', methods=['POST'])
@login_required
def delete_file(filename):
    """Deletar arquivo"""
    filename = secure_filename(filename)
    upload_folder = current_app.config['UPLOAD_FOLDER']
    filepath = os.path.join(upload_folder, filename)
    
    try:
        if os.path.exists(filepath):
            os.remove(filepath)
            flash('Arquivo deletado com sucesso!', 'success')
        else:
            flash('Arquivo não encontrado!', 'danger')
    except Exception as e:
        flash(f'Erro ao deletar: {str(e)}', 'danger')
    
    return redirect(url_for('files.my_files'))
