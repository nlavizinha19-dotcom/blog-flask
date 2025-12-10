"""Categories and Tags blueprint"""
from flask import Blueprint

bp = Blueprint('categories_tags', __name__)

from app.categories_tags import routes
