from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView


from . forms import MessageForm
from . models import Message

# Create your views here.

class ThankyouView(TemplateView):
    template_name = "review/thank-you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["custom_message"] = "sending data successfull"
        return context

class MessageView(CreateView):
    model = Message
    form_class = MessageForm
    template_name = 'review/review-form.html'

class MessageListView(ListView):
    template_name = "review/review-list.html"
    model = Message
    context_object_name = "messages"

class MessageDetailView(DetailView):
    template_name = "review/review-detail.html"
    model = Message
    context_object_name = "msg"