from django.http import HttpResponse
from django.shortcuts import render
from .models import Machine
# Create your views here.
def home(request):
    all_data= Machine.objects.all
    return  render(request,'index.html', {'machineInfo' : all_data});
def problem_solution(request):
    return  render(request,'problem-solution.html');
def machines(request):
    return  render(request,'machines.html');