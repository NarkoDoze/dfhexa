from django.shortcuts import render
from .API.makefail import List, MakeFail
from django.http import HttpResponse
import json

# Create your views here.
def make_fail(request):
    if request.method == "GET":
        epic = List().epic
        FailRange = ['', '+1', '+2', '+3', '+4', '+5', '+6', '+7', '+8']
        return render(request, 'makefail.html', {'kind': epic.keys(), 'epic': json.dumps(epic), 'defaultname': epic['소검'].keys(), 'fail': FailRange})
    elif request.method == "POST":
        img = MakeFail(request.POST['kinds'], request.POST['name'], request.POST['fail']).image()
        response = HttpResponse(content_type="image/png")
        img.save(response, format='PNG')
        return response