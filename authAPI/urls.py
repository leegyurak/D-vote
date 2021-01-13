from django.urls import path
from .views import loginView, registerView

urlpatterns = [
    path('login', loginView.as_view()),
    path('signUp', registerView.as_view()),
]