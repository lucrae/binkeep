from flask import Blueprint, render_template, redirect, url_for, request, abort
from flask_login import login_required, current_user, login_user, logout_user

from project.models import db, User, Collection

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/home')
def home():
    collections = Collection.query.all()
    return render_template('home.html', collections=collections)

@main.route('/<user_username>')
def user(user_username):
    user = User.query.filter_by(username=user_username).first()
    
    # abort 404 on user not found
    if user == None:
        return abort(404)
    
    return render_template('user.html', user=user)

@main.route('/<user_username>/<collection_token>')
def collection(user_username, collection_token):
    user = User.query.filter_by(username=user_username).first() # get user

    # abort 404 on user not found
    if user == None:
        return abort(404)

    collection = user.collections.filter_by(token=collection_token).first() # get collection of user
    
    # abort 404 on user not found
    if collection == None:
        return abort(404)
    
    return render_template('collection.html', collection=collection)

@main.route('/c/<collection_token>') # redirect route to 'collection'
def collection_from_token(collection_token):
    collection = Collection.query.filter_by(token=collection_token).first()

    # abort 404 on collection not found
    if collection == None:
        return abort(404)
    
    return redirect(url_for('main.collection', user_username=collection.author.username, collection_token=collection.token))

@main.route('/cid/<collection_id>') # redirect route to 'collection'
def collection_from_id(collection_id):
    collection = Collection.query.get(collection_id)

    # abort 404 on collection not found
    if collection == None:
        return abort(404)
    
    return redirect(url_for('main.collection', user_username=collection.author.username, collection_token=collection.token))