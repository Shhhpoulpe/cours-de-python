# EX 1

class CompteBancaire :
    def __init__(self,
                 nom,
                 solde):
        self.nom = nom
        self.solde = solde
    
    def depot(self, valeur):
        self.solde -= valeur
    
    def retrait(self, valeur):
        self.solde += valeur
    
    def affiche(self):
        print('Nom: {}, Solde: {}'.format(self.nom,self.solde))

compte = CompteBancaire('Jean', 1000)
compte2 = CompteBancaire('Renée', 5000)

compte.depot(500)
compte2.retrait(1000)

compte.affiche()
compte2.affiche()

# EX 2

class Point :
    def __init__(self,x,y,z=None):
        self.x = x
        self.y = y
        self.z = z

    def ToString(self):
        if self.z is None:
            return "P({} , {})".format(float(self.x),float(self.y))
        else:
            return "P({} , {} , {})".format(float(self.x),float(self.y),float(self.z))

point = Point(5,6)

print(point.ToString())

point2 = Point(7,8,9)

print(point2.ToString())

# EX 3

class DateNaissance :
    def __init__(self,
                 jours,
                 mois,
                 annee):
        self.jours = jours
        self.mois = mois
        self.annee = annee

    def ToString(self):
        return "{} / {} / {}".format(self.jours,self.mois,self.annee)

class Personne :
    def __init__(self,
                 nom,
                 prenom,
                 dateNaissance):
        self.nom = nom
        self.prenom = prenom
        self.dateNaissance = dateNaissance
    
    def afficher(self):
        print('Nom: ' + self.nom + ', Prenom: ' + self.prenom + ', Date de naissance: ' + str(self.dateNaissance.ToString()))


personne = Personne('Renée','Jean',DateNaissance(5,3,1999))
personne.afficher()


class Employe(Personne):

    def __init__(self, nom, prenom, dateNaissance, salaire):
        Personne.__init__(self,nom,prenom,dateNaissance)
        self.salaire = salaire
    
    def afficher(self):
        print('Nom: ' + self.nom + ', Prenom: ' + self.prenom + ', Date de naissance: ' + str(self.dateNaissance.ToString()) + ', Salaire: ' + str(self.salaire))

employe = Employe('Guillaume','Dupont',DateNaissance(5,3,1999),15000)
employe.afficher()

class Chef(Employe):

    def __init__(self, nom, prenom, dateNaissance, salaire, service):
        Employe.__init__(self, nom, prenom, dateNaissance, salaire)
        self.service = service
    
    def afficher(self):
        print('Nom: ' + self.nom + ', Prenom: ' + self.prenom + ', Date de naissance: ' + str(self.dateNaissance.ToString()) + ', Salaire: ' + str(self.salaire) + ', Service: ' + str(self.service))

chef = Chef('Martin', 'Mister', DateNaissance(5,3,1999),500000,'Big boss')
chef.afficher()


#EX 4

class Courrier:
    
    def __init__(self, poids, expedition, adresse_destination, adresse_expedition):
        self.poids = poids
        self.expedition = expedition
        self.adresse_destination = adresse_destination
        self.adresse_expedition = adresse_expedition

class Lettre(Courrier):
    
    def __init__(self, poids, expedition, adresse_destination, adresse_expedition, format):
        Courrier.__init__(self, poids, expedition, adresse_destination, adresse_expedition)
        self.format = format

    def ToString(self):
        print("Colis : ")
        print("Adresse destination: "+self.adresse_destination) 
        print("Adresse expedition: "+self.adresse_expedition)
        print("Poids: {} grammes".format(self.poids))
        print("Mode: "+self.expedition) 
        print("Format: "+str(self.format))
        print("Prix du timbre: "+str(self.calculTimbre()))


    def calculTimbre(self):
        tarifBase = 0
        if self.expedition == "normal":
            if self.format == "A4":
                tarifBase = 2.50
            else:
                tarifBase = 3.50
            
            return tarifBase+1.0*self.poids
        else:
            return tarifBase*2

class Colis(Courrier):

    def __init__(self, poids, expedition, adresse_destination, adresse_expedition, volume):
        Courrier.__init__(self, poids, expedition, adresse_destination, adresse_expedition)
        self.volume = volume
    
    def ToString(self):
        print("Colis : ")
        print("Adresse destination: "+self.adresse_destination) 
        print("Adresse expedition: "+self.adresse_expedition)
        print("Poids: {} grammes".format(self.poids))
        print("Mode: "+self.expedition) 
        print("Volume: "+str(self.volume))
        print("Prix du timbre: "+str(self.calculTimbre()))

    def calculTimbre(self):
        if self.expedition == "normal":
            return 0.25*self.volume+self.poids*1.0
        else:
            return (0.25*self.volume+self.poids*1.0)*2


L1 = Lettre( 80, "normal","Lille", "Paris", "A4")
L1.ToString()
C1 = Colis(3500, "expresse", "Marrakeche", "Barcelone", 2.25)
C1.ToString()