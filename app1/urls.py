from django.urls import path
from app1.views import list_universities, university_detail

app = "app1"

urlpatterns = [
    path("", list_universities, name="list-universities"),
    path("university_detail/<str:pk>", university_detail, name="university-detail"),
]
