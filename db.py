from flask import session
import pymysql.cursors
import hashlib
from  datetime import datetime


def get_db():
    db = pymysql.connect(
        host='localhost',
        user='a12345',
        password='PASS',
        database='db_a12345',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor)
    return db


def register_user(username, email, password):
    pass

def login_user(email,password):
    pass

def get_posts():
    pass


def get_post(post_id):
    pass


def new_post(content):
    pass

def update_post(post_id, content):
    pass
        

def delete_post(post_id):
    pass

def validate_email(email):
    pass

def validate_token(token):
    pass
	
def update_reset_digest(email):
    db = get_db()
    present_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    reset_digest = hashlib.md5(str(datetime.now()).encode()).hexdigest()

    query  = "UPDATE users SET reset_digest = '" + reset_digest + "' , reset_sent_at = '" + present_date + "' WHERE email = '" + email  + "'"
    db.cursor().execute(query) 
    db.commit()
    return reset_digest

def update_password(user_id, password):
    pass

def update_password_digest(email):
    pass

def generate_cookie(email):
    db = get_db()
    present_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    remember_digest = hashlib.md5(str(datetime.now()).encode()).hexdigest()

    query  = "UPDATE users SET remember_digest = '" + remember_digest + "' , updated_at = '" + present_date + "' WHERE email = '" + email  + "'"
    db.cursor().execute(query) 
    db.commit()
    return remember_digest

def validate_cookie(cookie):
    pass

def cookie_reset(id):
    pass