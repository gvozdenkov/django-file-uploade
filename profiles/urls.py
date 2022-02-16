from xml.dom.minidom import Document
from django.urls import path

from . import views

urlpatterns = [
    path("", views.UserProfileCreateView.as_view()),
    path("list", views.UserProfileListView.as_view())
]