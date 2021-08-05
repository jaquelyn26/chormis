from django.shortcuts import render

# Create your views here.
def chormi(request):
    return render(request, 'index.html')

