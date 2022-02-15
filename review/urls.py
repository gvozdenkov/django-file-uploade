from django.urls import path

from review import views

urlpatterns = [
    path('', views.MessageView.as_view(success_url='/thank-you'), name='review_form'),
    path('thank-you', views.ThankyouView.as_view(), name='thankyou'),
    path('reviews', views.MessageListView.as_view(), name='review_list'),
    path('reviews/<int:pk>', views.MessageDetailView.as_view(), name='review_detail')
]
