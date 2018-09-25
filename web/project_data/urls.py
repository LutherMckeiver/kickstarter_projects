from django.urls import path
from .views import projects_detail_view, projects_list_view


urlpatterns = [
    path('', projects_list_view, name='projects_list'),
    path('<int:pk>', projects_detail_view, name='projects_detail'),
]
