from django.conf.urls import include, url
from . import views
urlpatterns = [
        url(r'^$', views.mostrar_indice, name='mostrar_indice'),
         url(r'^lol$', views.get_name),

#        url(r'^thanks/', views.show_name),
        url(r'^donar/', views.donar,name="donar"),
        url(r'^estadistica/', views.estadisticas,name="estadisticas"),
        url(r'^tutoriales/', views.mostrar_tutoriales,name="mostrar_tutoriales"),
        url(r'^voluntario/', views.mostrar_voluntario,name="mostrar_voluntario"),
        url(r'^integrantes/', views.mostrar_sobreNosotros,name="mostrar_nsobreNosotros"),


        url(r'^loginAdmin/', views.mostrar_loginAdmin,name="mostrar_login"),
        
        url(r'^administradorGeneral/', views.mostrar_administradorGeneral,name="mostrar_administrador_general"),
        url(r'^administradorZonal/', views.mostrar_administradorZonal,name="mostrar_administrador_zonal"),
        url(r'^configucaionCapacidades/', views.mostrar_configuracionCapacidades,name="mostrar_configuracionCapacidades"),
        url(r'^configucaionCuenta/', views.mostrar_configuracionCuenta,name="mostrar_configuracionCuenta"),
        url(r'^crearProducto/', views.mostrar_crearProducto,name="mostrar_crearProducto"),
        url(r'^inventarioAgua/', views.mostrar_inventarioAgua,name="mostrar_inventarioAgua"),
        url(r'^inventarioComida/', views.mostrar_inventarioComida,name="mostrar_inventarioComida"),
        url(r'^inventarioRopa/', views.mostrar_inventarioRopa,name="mostrar_inventarioRopa"),


        url(r'^buscarCentroAcopio/', views.mostrar_buscarCentroAcopio,name="mostrar_buscarCentroAcopio"),
        url(r'^configCuenta/', views.mostrar_configCuenta,name="mostrar_configCuenta"),
        url(r'^crearAdmin/', views.mostrar_crearAdministrador,name="mostrar_crearAdministrador"),
        url(r'^verCentro/', views.mostrar_verCentro,name="mostrar_verCentro"),


    ]
