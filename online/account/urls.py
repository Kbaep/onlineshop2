from django.urls import path
from account.views import AuthView, LogoutView,RegistrationView

app_name = "account"
urlpatterns = [
    path('', AuthView.as_view(), name='auth'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('registration/', RegistrationView.as_view(), name='registration'),
]
