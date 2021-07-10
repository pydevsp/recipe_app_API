from django.urls import path
from .views import *

app_name = 'user'

urlpatterns = [
    path('create/', CreateUserView.as_view(), name='create'),
    # name field use in test url ==== TOKEN_URL = reverse('user:tokenss')
    path('token/', CreateTokenView.as_view(), name='tokenss'),
    path('me', ManageUserView.as_view(), name='me'),
]
