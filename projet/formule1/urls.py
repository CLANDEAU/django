from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.index),
    path('main/', views.main),
    path('index/', views.index),


    path('ajout/', views.ajout),
    path('traitement/', views.traitement),
    path('affiche/<int:id>/', views.affiche),
    path('update/<int:id>/', views.update),
    path('updatetraitement/<int:id>/', views.updatetraitement),
    path('updatetraitement//', views.traitement),
    path('delete/<int:id>/', views.delete),


    path('inscrire/', views.inscrire),
    path('traitementpilote/', views.traitementpilote),
    path('affichepilote/<int:id>/', views.affichepilote),
    path('updatepilote/<int:id>/', views.updatepilote),
    path('updatetraitementpilote/<int:id>/', views.updatetraitementpilote),
    path('updatetraitementpilote//', views.traitementpilote),
    path('deletepilote/<int:id>/', views.deletepilote),
]
