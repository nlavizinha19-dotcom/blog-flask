"""Design blueprint - Personalização de temas"""
from flask import Blueprint

bp = Blueprint('design', __name__)

from app.design import routes
