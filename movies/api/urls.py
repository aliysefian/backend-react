"""webdev URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from movies.api.views import MovieApiView, MovieDetailApiView, MovieUpdateApiView, MovieDeleteApiView, \
    MovieCreateApiView
from movies.views import aliView

urlpatterns = [
    # path('',   aliView, name='list_movie'),
    path('', MovieApiView.as_view(), name='list_movie'),
    path('<int:pk>/', MovieDetailApiView.as_view(), name='detail_movie'),
    path('edit/<int:pk>/', MovieUpdateApiView.as_view(), name='update_movie'),
    path('delete/<int:pk>/', MovieDeleteApiView.as_view(), name='delete_movie'),
    path('create/', MovieCreateApiView.as_view(), name='create_movie'),
    # path('ali', aliView),

]
