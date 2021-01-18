from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('types', views.about, name='about'),
    path('create', views.create, name='create'),
    path('black', views.black, name='black'),
    path('milk', views.milk, name='milk'),
    path('white', views.white, name='white'),
    path('view', views.TypesView.as_view(), name='view')
]