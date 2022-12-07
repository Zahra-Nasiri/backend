from django.urls import path
from . import views

urlpatterns = [
    path('',  views.get_routes),
    path('events/', views.get_events),
    path('events/<str:pk>/', views.get_event),
    path('create-events/', views.create_event),
    path('delete-events/<str:pk>/', views.delete_event),
    path('edit-events/<str:pk>/', views.edit_event),
    path('registrants/', views.get_registrans),
    path('delete-registrants/<str:pk>/', views.delete_registrant),
    path('create-registrants/<str:pk>/', views.create_registrant),
]
