from django.shortcuts import render
from .models import Movie

# Create your views here.
def index(request):
    movie_list = Movie.objects.all()
    context = {'movie_list': movie_list}

    return render(request, 'movieApp/index.html', context)

def about(request):
    return render(request, 'movieApp/about.html')

def test(request):

    return render(request, 'movieApp/test.html')

def newIndex(request):
    movie_list2 = Movie.objects.all()
    context = {'movie_list2':movie_list2}
    return render(request, 'movieApp/newIndex.html', context)