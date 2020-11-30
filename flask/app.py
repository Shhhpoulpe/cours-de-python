from flask import Flask
from flask import request
from jinja2 import Template, FileSystemLoader, Environment

app = Flask(__name__)

def index_fun():
    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)

    template = env.get_template('template.jinja2.html')

    result = template.render(name='jean-renée')
    return result

def do_the_login():
    return 'do the login'

def show_the_login_form():
    return 'show the login form'

@app.route('/', methods=["GET", "POST"])
def index():
    response = index_fun()
    return response

@app.route('/about')
def about():
    return 'The about page'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

if __name__ == '__main__':
    app.run(debug=True)