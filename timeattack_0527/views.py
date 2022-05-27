from django.shortcuts import render

def index_view(request):
    return render(request, 'index.html')

class myUser:
    def __init__(self,email,password):
        self.email = email
        self.password = password
    email : ''
    password : ''
