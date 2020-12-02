# Commandes Docker

- Docker run permet de lancer un conteneur a partir d'une image
- Docker exec lance une commande dans un conteneur
- Docker build permet de créer une image a partir d'un fichier Dockerfile


# Hello World

![](hello_world.png)

# Run an image

- Pour run une image il faut:
- - build l'image avec la commande : sudo docker build . -t image1
- - récupérer l'id de l'image avec : sudo docker images
- - run l'image avec : sudo docker run --name flask -p 5000:5000 [id]
- - pour delete toutes les images : sudo docker system prune

# Host sur Heroku

- Pour lier le github à heroku, il faut utiliser : heroku git:remote -a flask-mj
- Pour préciser que c'est du python : heroku buildpacks:set heroku/python
- Pour créer le l'application heroku : heroku create
- Pour déployer le code : git push heroku main
- Check si il tourne : heroku ps:scale web=1
- Ouvrir le projet : heroku open
- Voir les logs : heroku logs --tail
- Procfile -> command executer au démarrage
- Pour le scaling : heroku ps:scale web=[nb]