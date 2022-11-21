from django.urls import path
from . import views

urlpatterns = [
    path('',  views.getRoutes),
    path('events/', views.getEvents),
    path('events/<str:pk>/', views.getEvent),
    path('create-events/', views.createEvent),
    path('delete-events/<str:pk>/',views.deleteEvent),
    path('edit-events/<str:pk>/',views.editEvent),
    path('registrants/', views.getRegistrans),
    path('delete-registrants/<str:pk>/', views.deleteRegistrant),
    path('create-registrants/<str:pk>/', views.createRegistrant)

]