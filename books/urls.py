from django.urls import path

from . import views

app_name = 'books'
urlpatterns = [
    path('<int:id>/authors', views.get_authors, name='index'),

]