from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import University


def list_universities(request):
    universities = University.objects.all().order_by("-full_name")
    context = {"universities": universities}
    return render(request, "app1/index.html", context)


def university_detail(request, pk):
    context = {"university": get_object_or_404(University, pk=pk)}
    return render(request, "app1/university_detail.html", context)
