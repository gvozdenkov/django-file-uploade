from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import ListView

from . models import UserProfile

# Create your views here.

# На основе модели созадём view для созадния объекта (CreateView)
# view рендерит темплейт с формой и заданными полями модели
class UserProfileCreateView(CreateView):
    model = UserProfile
    template_name = "profiles/create-profile.html"
    fields = "__all__"
    success_url = "/profiles"

class UserProfileListView(ListView):
    model = UserProfile
    template_name = "profiles/user-profiels.html"
    context_object_name = "profiles"
