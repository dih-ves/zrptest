from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required, logout_user, current_user
#from werkzeug.security import generate_password_hash, check_password_hash

import models.Usuario
from app import db


dash = Blueprint('dash', __name__)


@dash.route('/dashboard')
@login_required
def dashboard():
    
    #produtos = Produto.query.order_by(Produto.id.desc()).limit(5)
    #produtos=produtos

    return render_template('vendedor/dashboard.html', name=current_user.username)


@dash.route('/clientes')
@login_required
def clientes():

    #cliente = Cliente.query.filter_by(user_id=current_user.id)
    #user = User.query.filter_by(username=form.username.data).first()

    return render_template('vendedor/clientes.html', name=current_user.username) 




'''
@dash.route('/cadastrar_clientes',  methods=['GET', 'POST'])
@login_required
def clientes_cadastro():
    form = ClienteForm()

    if form.validate_on_submit():
        
        new_cliente = Cliente(nome = form.nome.data, email = form.email.data, telefone=form.telefone.data, endereco= form.endereco.data, user_id= current_user.id)
        db.session.add(new_cliente)
        db.session.commit()

    return render_template('clientes_cadastrar.html', form=form)
'''


@dash.route('/produtos')
@login_required
def produtos():
    #produtos = Produto.query.all()
    #produtos = Produto.query.all()

    return render_template('vendedor/produtos.html', name=current_user.username) # , produtos=produtos



''' 
@dash.route('/cadastrar_produto',  methods=['GET', 'POST'])
@login_required
def produto_cadastro():
    form = ProdutoForm()

    if  form.validate_on_submit():
        
        new_produto = Produto(nome=form.nome.data, descricao=form.descricao.data, preco=form.preco.data, tipo_de_calculo=form.tipo_de_calculo.data)
        db.session.add(new_produto)
        db.session.commit()

    return render_template('produtos_cadastrar.html', form=form)
'''




@dash.route('/orcamentos')
@login_required
def orcamentos():

    #orca = Cliente.query.filter_by(user_id=current_user.id)

    return render_template('vendedor/orcamentos.html', name=current_user.username) #, name=current_user.username, orca=orca



'''
@dash.route('/orcamento_iniciar')
@login_required
def iniciar_orcamento():

    produtos = Produto.query.all()
    
    
    return render_template('orcamento_iniciar.html', name=current_user.username, produtos=produtos  )
'''

''' 
@dash.route('/orcamento_iniciar/add/<int:id_item>')
def add_item(id_item):

    dic_enviado = request.json
    
    produto = Produto.query.filter_by(id_item)
    print(produto)
    print(produto.preco)

    #return 'adiciona o produto na lista de OrcamentoProdutos'
    return 'Foi'
'''


@dash.route('/pedidos')
@login_required
def pedidos():
    return render_template('vendedor/pedidos.html', name=current_user.username)



@dash.route('/cadastrar_cliente')
@login_required
def cadastrar_cliente():
    return render_template('vendedor/cadastrar_cliente.html', name=current_user.username)
