"""
Script para executar a aplicação Flask Blog
"""
import os
from app import create_app, db

if __name__ == '__main__':
    app = create_app(os.getenv('FLASK_ENV', 'development'))
    
    @app.shell_context_processor
    def make_shell_context():
        """Adiciona objetos ao contexto de shell"""
        return {'db': db}
    
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0', port=5000)
