from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required, logout_user, current_user
from flask_user import roles_required

#from flask_admin.contrib.sqla import ModelView
#from werkzeug.security import generate_password_hash, check_password_hash


from flask_admin import BaseView, expose


#import models.Usuario
from app import db


admin_dash = Blueprint('admin_dash', __name__)



@admin_dash.route('/admin/dashboard')
@login_required
def dashboard():
    
    #produtos = Produto.query.order_by(Produto.id.desc()).limit(5)
    #produtos=produtos

    return render_template('admin/dashboard.html', name=current_user.username)



@admin_dash.route('/admin/produtos')
@login_required
def produtos():
    
    #produtos = Produto.query.order_by(Produto.id.desc()).limit(5)
    #produtos=produtos

    return render_template('admin/produtos.html', name=current_user.username)


@admin_dash.route('/admin/cadastrar_produtos')
@login_required
def cadastrar_produtos():
    
    #produtos = Produto.query.order_by(Produto.id.desc()).limit(5)
    #produtos=produtos

    return render_template('admin/cadastrar_produtos.html', name=current_user.username)


@admin_dash.route('/admin/pedidos')
@login_required
def pedidos():
    
    #produtos = Produto.query.order_by(Produto.id.desc()).limit(5)
    #produtos=produtos

    return render_template('admin/pedidos.html', name=current_user.username)



@admin_dash.route('/admin/relatorios')
@login_required
def relatorios():
    
    #produtos = Produto.query.order_by(Produto.id.desc()).limit(5)
    #produtos=produtos

    return render_template('admin/relatorios.html', name=current_user.username)