# coding: utf-8

from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, errors
from ..models import Permission


# 为了使模版中也能使用Permission类， 使用上下文管理器，能让变量在所有模版中全局访问
@main.app_context_processor
def inject_permission():
    return dict(Permission=Permission)
