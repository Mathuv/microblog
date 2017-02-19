# microblog
Coding as I follow tutorial under https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world


# Learnings:
**ERROR**

This error is unique to python environment on Ubuntu
>python -m venv flask

Error: Command '['/home/mathu/PycharmProjects/microblog/flask/bin/python', '-Im', 'ensurepip', '--upgrade', '--default-pip']' returned non-zero exit status 1.

**Resolution**
>python -m venv flask --without-pip

or

>sudo apt-get install python3-venv

all of the required python packages can be installed with a single pip install command

>$ flask/bin/pip install flask flask-login flask-openid flask-mail flask-sqlalchemy sqlalchemy-migrate flask-whooshalchemy flask-wtf flask-babel guess_language flipflop coverage

**Additional Resources**

A simple introduction to Python decorators
http://stackoverflow.com/questions/739654/how-to-make-a-chain-of-function-decorators/1594484#1594484
