from flask import Flask
from jinja2 import Template, FileSystemLoader, Environment

app = Flask(__name__)

def index_fun():
    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)

    template = env.get_template('index.jinja2.html')

    result = template.render()
    return result


def name():
    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)

    template = env.get_template('template.jinja2.html')

    result = template.render(name='baptiste')
    return result

@app.route('/')
def index():
    return index_fun()

@app.route('/about')
def about():
    return str(app.route)

if __name__ == '__main__':
    app.run(debug=True)