from flask import Flask
from flask import request
from jinja2 import Template, FileSystemLoader, Environment
import json

"""
L'application web python va permettre aux joueurs de GTA
d'avoir un accès facile au nouveauté de la semaine sur
la page internet
"""

app = Flask(__name__)



def index_fun(categ1 = "all", categ2 = None):
    # Ouverture du template
    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)
    template = env.get_template('index.jinja2.html')
    result = template.render(info=get_weekly_info(categ1,categ2),
                             categ1 = categ1,
                             categ2 = categ2)
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

@app.route('/podium')
def podium():
    response = index_fun("Podium")
    return response

@app.route('/login')
def login():
    response = index_fun("Log in")
    return response

@app.route('/double')
def double_money():
    response = index_fun("Double money")
    return response

@app.route('/triple')
def triple_money():
    response = index_fun("Triple money")
    return response

@app.route('/discounts/cars')
def discounts_cars():
    response = index_fun("Discounts","Cars")
    return response

@app.route('/discounts/properties')
def discounts_Properties():
    response = index_fun("Discounts","Properties")
    return response

if __name__ == '__main__':
    app.run(debug=True)