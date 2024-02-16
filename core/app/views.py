from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    user = request.user
    groups = user.groups.all()
    for group in groups:
        print(group.name)
        return render(request,'app/index.html')