from django.shortcuts import render ,HttpResponse
from django.http import JsonResponse
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view

from distutils.log import error
import csv 

# Create your views here.
def event(request):
    return render(request, "event_formulaire/impact.html")
def ajax_save_data_formulaire(request):
    if request.method  =='POST':
      nom_complet = request.POST['nom_complet']
      numero_tel = request.POST['numero_tel']
      participant = request.POST['participant']
      qr_code_data = request.POST['qr_code_data']
      if not L_impact.objects.filter(numero_tel=numero_tel).exists():
        db_evenement = L_impact()
        db_evenement.nom_complet = nom_complet
        db_evenement.numero_tel = numero_tel
        db_evenement.participant = participant
        db_evenement.a_participe = False
        db_evenement.qr_code_data = qr_code_data
        db_evenement.save()
         
      print("*"*100)
      print(qr_code_data)
      print(participant)
      print(nom_complet)
    
      #--------- on met le commentaire en faissnt appele a set_commentaitre
      
    return JsonResponse({"success":"Merci pour nous avoir envoyé le formulaire"})
   
@api_view(["PUT"])
def api_update_status_a_participe (request,pk,*args,**kwargs):
    instance  = L_impact.objects.get(qr_code_data=pk)
    serializer_class = table_L_impact_Serializer(data=request.data,instance=instance)
    if serializer_class.is_valid():
        serializer_class.save()

    return Response(serializer_class.data)


# Create your views here.
def export_to_csv(reuest):
     evenements_list = L_impact.objects.all()
     response = HttpResponse('text/csv')
     response["Content-Disposition"] = "attachment; filename=evenement_L-impact_export.csv"
     writer = csv.writer(response)
     writer.writerow(["id","nom_complet","numero_tel","participant","a_participe","qr_code_data"])
     evenements_fields = evenements_list.values_list("id","nom_complet","numero_tel","participant","a_participe","qr_code_data")
     for i in evenements_fields :
          writer.writerow(i)
     return response 

def error_404(request,exception):
        
        return render(request,'event_formulaire/404.html')

def error_500(request):
        
        return render(request,'event_formulaire/500.html')