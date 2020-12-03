from flask import Flask
from flask import request
from jinja2 import Template, FileSystemLoader, Environment
import json

app = Flask(__name__)

# Ouverture du template
file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)
template = env.get_template('index.jinja2.html')

def index_fun():
    result = template.render(info=get_weekly_info("Discounts","Cars"))
    return result

def get_weekly_info(categ1 = "all", categ2 = None):
    """
    Retourne la partie du JSON qui est utile à la page
    """
    # Ouvre le JSON
    with open('info.json') as f:
        data_return = json.load(f)
    # Vérifie que je veut toutes les données ou non
    if categ1 == "all":
        return data_return
    else:
        # Vérifie si il y a une sous catégorie
        if categ2:
            return data_return[categ1][categ2]
        else:
            return data_return[categ1]

@app.route('/')
def index():
    response = index_fun()
    return response

if __name__ == '__main__':
    app.run(debug=True)