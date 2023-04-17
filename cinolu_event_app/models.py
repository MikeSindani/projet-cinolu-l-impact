from django.db import models

# Create your models 
# here.

class L_impact(models.Model):
    nom_complet = models.CharField(max_length=50,null=True)
    numero_tel = models.CharField(max_length=50,null=True)
    participant = models.CharField(max_length=250,null=True)
    a_participe = models.BooleanField(default=False)
    qr_code_data = models.CharField(max_length=250,null=True)
    
    def __str__(self ):
        return self.nom_complet
