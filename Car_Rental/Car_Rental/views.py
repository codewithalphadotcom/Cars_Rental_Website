from django.shortcuts import render

# pages to load when the user visits the routes
def home(request):
    return render(request, './index.html')

def about(request):
    return render(request, './pages/about.html')

def cars(request):
    return render(request, './pages/cars.html')

def features(request):
    return render(request, './pages/features.html')

def helpp(request):
    return render(request, './pages/help.html')