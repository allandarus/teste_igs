from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CollaboratorsSerializer, DepartmentsSerializer
from .models import Collaborators, Departments

# Create your views here.

class CollaboratorsView(viewsets.ModelViewSet):
    queryset = Collaborators.objects.all()
    serializer_class = CollaboratorsSerializer


class DepartmentsView(viewsets.ModelViewSet):
    queryset = Departments.objects.all()
    serializer_class = DepartmentsSerializer


def index(request):
    collab = Collaborators.objects.all()
    depart = Departments.objects.all()
    return render(request, 'index.html',  {'collab': collab, 'depart': depart})
