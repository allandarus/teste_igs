from .views import CollaboratorsView, DepartmentsView, index
from django.urls import path
from rest_framework import routers
from django.urls import include

router = routers.DefaultRouter()
router.register(r'collaborators', CollaboratorsView)
router.register(r'departments', DepartmentsView)

urlpatterns = [
    path('', include(router.urls)),
    path('index/', index, name='index')
]
