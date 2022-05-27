from django.shortcuts import render, redirect
from .models import UserModel


def index_view(request):
    return render(request, 'index.html')


def sign_up_view(request):
    if request.method == 'GET':  # GET 메서드로 요청이 들어 올 경우
        return render(request, 'user/index.html')
    elif request.method == 'POST':  # POST 메서드로 요청이 들어 올 경우
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        password2 = request.POST.get('password2', None)

        if password != password2:
            return render(request, 'user/index.html')
        else:
            new_user = UserModel()
            new_user.username = username
            new_user.password = password
            new_user.save()
        return redirect('/index')