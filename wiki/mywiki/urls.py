from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('problem_solution', views.problem_solution, name='problem_solution'),
    path('machine', views.machines, name='machine'),
]