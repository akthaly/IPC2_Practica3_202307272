from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('visualizarXML/', views.visualizarXML, name='visualizarXML'),
    path('mostrarResultadosXML/', views.mostrarResultadosXML, name='mostrarResultadosXML'),
    path('subirXML/', views.subirXML, name='subirXML'),
    path('informacion/', views.informacion, name='informacion'),
    path('graficos', views.graficos, name='graficos'),
    path('datos/', views.datos, name='datos'),
    path('graficarVentas/', views.mostrar_grafica, name='graficarVentas'),

]