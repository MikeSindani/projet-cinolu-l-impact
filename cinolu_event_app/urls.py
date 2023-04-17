

from django.urls import path ,include
from . import views

urlpatterns = [
    path('ajax/evenement_cinolu_formulaire/', views.ajax_save_data_formulaire,name="ajax_formulaire"),
    path('', views.event),
    path('api/update_status/<str:pk>/', views.api_update_status_a_participe),
    path('csv/', views.export_to_csv),
    
]