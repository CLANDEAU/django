from django.db import models


class Ecurie(models.Model):
    nom = models.CharField(max_length=50)
    marque = models.CharField(max_length=20)
    team_manager = models.CharField(max_length=50)
    sponsor = models.CharField(max_length=20)

    def __str__(self):
        texte = f"L'équipe {self.nom} de la marque {self.marque} est gérée par {self.team_manager} et est sponsorisé par {self.sponsor}"
        return texte

    def dico(self):
        return {'nom': self.nom, 'marque': self.marque, 'team_manager': self.team_manager, 'sponsor': self.sponsor,}


class Pilote(models.Model):
    ecurie = models.ForeignKey("Ecurie", on_delete=models.CASCADE, default=None)
    nom = models.CharField(max_length=20)
    prenom = models.CharField(max_length=20)
    age = models.IntegerField(blank=False)

    def __str__(self):
        textepilote = f"{self.nom} {self.prenom}est un pilote officiel de l'équipe {self.ecurie.nom}"
        return textepilote

    def dico(self):
        return {'nom': self.nom, 'prenom': self.prenom, 'age': self.age, 'ecurie': self.ecurie.nom}
