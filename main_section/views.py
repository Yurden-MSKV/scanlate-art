from django.shortcuts import render

def index(request):
    return render(request, 'top_panel.html')