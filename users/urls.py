
from django.urls import path, include
from .views import *

urlpatterns = [
    path("register/", register_user),
    path("update/", update_user),
    path("",GetUser.as_view()),
    path('activate/<uidb64>/<token>/', activate_account, name='activate'),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
]
