from django.shortcuts import render
from .models import sample
# Create your views here.
def index(request):
    return render(request, 'fapp/index.html')

def showSample(request):
    samples= sample.objects.all().values()
    return render(request, 'fapp/sample.html',{'samples':samples})