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
from django.urls import path, re_path, include
from app01 import views
from rest_framework.routers import DefaultRouter
from app01.views import BookView
from app02 import urls
from app03 import urls


urlpatterns = [
    path('admin/', admin.site.urls),
    # re_path('books/(?P<pk>\d+)', views.BookView.as_view()),
    path('books/', views.BooksView.as_view()),
    path('books2/', views.BooksView2.as_view()),
    path('app02/', include(urls)),
    path('app03/', include(urls)),
]

# router = DefaultRouter()
# router.register('book',views.BookViewSet)

# urlpatterns += router.urls



