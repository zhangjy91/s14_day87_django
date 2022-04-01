"""s14_day87_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, re_path
# from app01 import views
from rest_framework.routers import DefaultRouter
from app01.views import BookView
from app02.views import Book2View
from app02.views import Book2View
from app03 import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('fruits4', views.Fruit4ViewSet)

urlpatterns = [

    re_path('fruits/(?P<pk>\d+)',views.FruitDetailView.as_view()),
    path('fruits/', views.FruitView.as_view()),

    re_path('fruits2/(?P<pk>\d+)',views.Fruit2DetailView.as_view()),
    path('fruits2/', views.Fruit2View.as_view()),

    re_path('fruits3/(?P<pk>\d+)',views.Fruit3View.as_view(actions={'get':'retrieve', 'put':'update', 'delete':'destroy'})),
    path('fruits3/', views.Fruit3View.as_view(actions={'get':'list', 'post':'create'})),

    path('login/', views.LoginView.as_view()),

    path('fruits5/', views.Fruit5View.as_view()),

    path('fruits6/', views.Fruit6View.as_view()),
]

urlpatterns += router.urls



