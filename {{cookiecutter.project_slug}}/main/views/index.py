from django.shortcuts import render

class IndexView():
    def index(request):
        return render(request, 'index/index.html')