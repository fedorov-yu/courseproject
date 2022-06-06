from django.shortcuts import render

# Create your views here.
from testapp.models import Rubric


def test(request):
    return render(request, "testapp/test.html", {'rubrics': Rubric.objects.all()})


def get_rubric(request, name):
    rubric = Rubric.objects.filter(name=name)
    return render(request, "testapp/test.html", {'rubric': rubric})