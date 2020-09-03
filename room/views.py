from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, View

# Create your views here.
class Lounge(View):

    def get(self, request):
        return render(request, 'index.html', status=200)

    @csrf_exempt
    def post(self, request):
        return HttpResponse('congrats!', status=200)
        
