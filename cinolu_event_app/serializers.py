from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User, Group

class table_L_impact_Serializer(serializers.ModelSerializer):
    class Meta:
        model = L_impact 
        fields = [
            "nom_complet",
            'a_participe', 
        ]
