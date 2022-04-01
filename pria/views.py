from django.shortcuts import render


def index(request):
    return render(request, 'pria/zaglav.html')

def mypage(request):
    return render(request, 'pria/mypage.html')
