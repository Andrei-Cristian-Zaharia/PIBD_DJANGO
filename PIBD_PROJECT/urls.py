"""
PIBD URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from PIBD_PROJECT.views import home_page_view
from PIBD_PROJECT.views.home_page_view import HomePageView
from PIBD_PROJECT.views.actors_page_view import ActorPageView
from PIBD_PROJECT.views.movie_page_view import MoviePageView
from PIBD_PROJECT.views.contracts_page_view import ContractPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('actors', ActorPageView.as_view(), name='actors'),
    path('movies', MoviePageView.as_view(), name='movies'),
    path('contracts', ContractPageView.as_view(), name='contracts'),
]