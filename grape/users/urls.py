from django.urls import path

from .views import register, LoginUser, loguot_user


urlpatterns = [
    path('registration/', register, name='registration'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', loguot_user, name='logout'),
]






