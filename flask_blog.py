from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'b8b8d7288506b91e058efcbdd4258e68'
#app.config['SQLALCHEMY_DATABASE_URI'] = ''

posts = [
    {
        'author':'Corey Schafer',
        'title':'Blog Post 1',
        'content':'First post content',
        'date_posted':'April 20, 2019'

    },
    {
        'author':'Corey Schafer',
        'title':'Blog Post 2',
        'content':'First post content',
        'date_posted':'April 20, 2019'

    },
    {
        'author':'Corey Schafer',
        'title':'Blog Post 3',
        'content':'First post content',
        'date_posted':'April 20, 2019'

    }
]

@app.route('/')
@app.route("/home")
def home():
    return render_template('homeLayout.html',posts=posts)


@app.route("/about")
def about():
    return render_template('about.html',title='About')

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash('Account created for {}!'.format(form.username.data),'success') 
        return redirect(url_for('home'))
    return render_template('register.html',title='Register', form=form)

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been Logged in!','sucess')
            return redirect(url_for('home'))
        else:
            flash('Login Unseccessful. Please check username and password','danger')

    return render_template('login.html',title='Login', form=form)

if __name__  == '__main__':
    app.run(debug=True)


#How to run an flask app
#export FLASK_APP=flask_blog.py
#flask run

#How to run app flask in debug mode
#export FLASK_DEBUG=1
#flask run