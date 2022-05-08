from django.shortcuts import render, HttpResponseRedirect
from .forms import EcurieForm, PiloteForm
from . import models




def main(request):
    return render(request, 'formule1/main.html')



def index(request):
    liste = list(models.Ecurie.objects.all())
    liste2 = list(models.Pilote.objects.all())
    return render(request, "formule1/index.html", {"liste": liste, 'liste2': liste2})



def ajout(request):
    if request.method == "POST":
        form = EcurieForm(request)
        return render(request, 'formule1/ajout.html', {"form": form})

    else:
        form = EcurieForm()
        return render(request, 'formule1/ajout.html', {"form": form})

def inscrire(request):
    if request.method == "POST":
        form = PiloteForm(request)
        return render(request, 'formule1/inscrire.html', {"form": form})

    else:
        form = PiloteForm()
        return render(request, 'formule1/inscrire.html', {"form": form})



def traitement(request):
    tform = EcurieForm(request.POST)
    if tform.is_valid():
        ecurie = tform.save()
        return HttpResponseRedirect('/formule1')

    else:
        return render(request, 'formule1/ajout.html', {"form": tform})

def traitementpilote(request):
    tpform = PiloteForm(request.POST)
    if tpform.is_valid():
        pilote = tpform.save()
        return HttpResponseRedirect('/formule1')

    else:
        return render(request, 'formule1/inscrire.html', {"form": tpform})



def affiche(request, id):
    ecurie = models.Ecurie.objects.get( pk = id)
    return render(request, 'formule1/affiche.html', {'ecurie': ecurie})

def affichepilote(request, id):
    pilote = models.Pilote.objects.get( pk = id)
    return render(request, 'formule1/affichepilote.html', {'pilote': pilote})



def update(request, id):
    ecurie = models.Ecurie.objects.get( pk = id)
    form = EcurieForm(ecurie.dico())
    return render(request, 'formule1/ajout.html', {'form': form, 'id': id})

def updatepilote(request, id):
    pilote = models.Pilote.objects.get( pk = id)
    form = PiloteForm(pilote.dico())
    return render(request, 'formule1/inscrire.html', {'form': form, 'id': id})



def updatetraitement(request, id):
    tform = EcurieForm(request.POST)

    if tform.is_valid():
        ecurie = tform.save(commit=False)
        ecurie.id = id
        ecurie.save()
        return HttpResponseRedirect('/formule1')

    else:
        return render(request, 'formule1/ajout.html', {"form": tform, 'id': id})

def updatetraitementpilote(request, id):
    tpform = PiloteForm(request.POST)

    if tpform.is_valid():
        pilote = tpform.save(commit=False)
        pilote.id = id
        pilote.save()
        return HttpResponseRedirect('/formule1')

    else:
        return render(request, 'formule1/inscrire.html', {"form": tpform, 'id': id})


def delete(request, id):
    ecurie = models.Ecurie.objects.get(pk=id)
    ecurie.delete()
    return HttpResponseRedirect('/formule1')

def deletepilote(request, id):
    pilote = models.Pilote.objects.get(pk=id)
    pilote.delete()
    return HttpResponseRedirect('/formule1')

