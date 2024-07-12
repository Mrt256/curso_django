from django.urls import path
from recipes.views import home, contato, my_view


urlpatterns = [
    path('', home),
    path('contato/', contato),
    path('sobre/', my_view),
    ]
