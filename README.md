# Flask LAB8_10 skeleton

### Download into C:\XAMPP\htdocs folder with your browser:
```
https://github.com/jmatbastos/LAB8_10/archive/refs/heads/main.zip
```
### or with git 
```
git clone https://github.com/jmatbastos/LAB8_10.git
```


### Install required packages 
```
pip install -r requirements.txt
```

### Compiles and hot-reloads for development
```
python -m flask --app LAB8_10 run --debug --host=0.0.0.0
```

### Open project in browser at URL
```
http://josebastos.eu:5000
```

### Compiles and minifies for production

Change '12345' with your student number:

```
nano app.wsgi

import sys
sys.path.insert(0,'/users/a12345/public_html/wsgi')

from LAB8_10 import app as application
```

### Open project in browser at URL
```
http://josebastos.eu/~a12345/wsgi/LAB8_10
```