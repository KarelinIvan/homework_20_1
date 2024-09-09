from django.shortcuts import render

# Создавайте свои мнения здесь.

def home(request):
    return render(request, 'home.html')

def contacts(request):
    return render(request, 'contacts.html')
