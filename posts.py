from flask import Flask
from flask import (
    Blueprint, session, flash, redirect, render_template, request, url_for
)

from LAB8_10.db import get_posts, new_post, get_post, update_post, delete_post, validate_cookie




bp = Blueprint('posts', __name__)


@bp.route('/')
def index():
    lab_name='LAB8_10'
    return render_template('posts/index.html',lab_name=lab_name) 



@bp.route('/delete/<int:id>')
def delete(id):
    pass

@bp.route('/new', methods=('GET', 'POST'))
@bp.route('/update/<int:id>', methods=('GET', 'POST'))
def new_or_update(id=None):
    pass

