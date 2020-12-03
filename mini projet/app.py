from flask import Flask
from flask import request
from jinja2 import Template, FileSystemLoader, Environment
import json

app = Flask(__name__)

def index_fun():
    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)

    template = env.get_template('index.jinja2.html')

    result = template.render(info=get_weekly_info())
    return result

def get_weekly_info():
    with open('info.json') as f:
        d = json.load(f)
        print(d)
    return d

@app.route('/')
def index():
    response = index_fun()
    return response

if __name__ == '__main__':
    app.run(debug=True)