from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user

from project.models import db, User, Collection

admin = Blueprint('admin', __name__)

@admin.route('/')
def index():
    return render_template("admin/admin.html")

@admin.route('/database')
def database():
    tables = [
        User,
        Collection,
    ]
    return render_template("admin/admin_database.html", db=db, tables=tables)
