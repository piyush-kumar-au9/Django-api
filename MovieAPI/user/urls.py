from django.conf.urls import url
from MovieAPI.user.views import UserRegistrationView


urlpatterns = [
    url('register', UserRegistrationView.as_view()),
    ]