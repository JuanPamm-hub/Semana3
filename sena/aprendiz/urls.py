from django.urls import path
from .views import lista_aprendices

urlpatterns = [
    path('aprendices/', lista_aprendices, name='lista')
]