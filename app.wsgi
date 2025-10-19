import sys
sys.path.insert(0,'/users/a12345/public_html/wsgi')

# If you want to run the application in a virtual environment uncomment the following 3 lines
#activate_this ='/users/a12345/public_html/wsgi/LAB8_10/.virtualenv/bin/activate_this.py'
#with open(activate_this) as file_:
#    exec(file_.read(), dict(__file__=activate_this))

from LAB8_10 import app as application
