from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm



@app.route('/login', methods=['GET', 'POST'])

def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html',
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Mat'} # fake user
    location = {'city': 'Sydney', 'country': 'Australia'}

    # return '''
    # <html>
    #     <head>
    #         <title>Home Page</title>
    #     </head>
    #     <body>
    #         <h1>Hello, ''' + user['nickname'] + '''</h1>
    #     </body>
    # </html>
    # '''

    posts = [ # fake array of posts
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'nickname': 'Dawkins'},
            'body': 'The greatest show on earth'
        }
     ]

    return render_template('index.html',
                           title='Home',
                           user=user,
                           location=location,
                           posts=posts)

    # return render_template('index.html',
    #                        user=user)