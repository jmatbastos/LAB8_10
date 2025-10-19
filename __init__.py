import os

from flask import Flask



# create and configure the app
app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY='dev',
)


from . import db
 
from . import auth
app.register_blueprint(auth.bp)

from . import posts
app.register_blueprint(posts.bp)

app.add_url_rule('/', endpoint='index')

