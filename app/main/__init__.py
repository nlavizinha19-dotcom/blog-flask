"""Main blueprint - Página inicial e rotas gerais"""
from flask import Blueprint

bp = Blueprint('main', __name__)

from app.main import routes
