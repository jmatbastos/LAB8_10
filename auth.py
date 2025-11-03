from flask import (
    Blueprint, flash, redirect, render_template, request, session, url_for, make_response
)

from flask import Flask
from flask_mail import Mail
from flask_mail import Message
app = Flask(__name__)
app.config['MAIL_SERVER'] = 'localhost'
app.config['MAIL_PORT'] = 25
mail = Mail(app)


from Flask_exame2.db import (register_user,login_user, validate_email, update_password_digest, 
                             validate_token, update_password,generate_cookie,cookie_reset
)
bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=('GET', 'POST'))
def register():
    pass

@bp.route('/login', methods=('GET', 'POST'))
def login():
    pass



@bp.route('/reset_password', methods=('GET', 'POST'))
def reset_password():
    pass

@bp.route('/new_password/<token>', methods=('GET', 'POST'))
def new_password(token):
    pass

def send_email(email, reset_digest):
    msg = Message(
    subject="Password reset",
    sender="webmaster@josebastos.eu",
    recipients=[email],
    )
    msg.html = render_template('auth/reset_email.html',reset_digest=reset_digest)
    mail.send(msg)
    ## problemas em receber o email na aplicação Papercut-SMTP ?
    ## comente todas as linhas anteriores e descomente a linha seguinte ...
    # return render_template('auth/reset_email.html',reset_digest=reset_digest)