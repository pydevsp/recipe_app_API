from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    # name field use in test url ==== TOKEN_URL = reverse('user:tokenss')
    path('token/', views.CreateTokenView.as_view(), name='tokenss'),
    path('me', views.ManageUserView.as_view(), name='me'),
]
