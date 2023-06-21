"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from myapp import views  # import views from myapp

urlpatterns = [
	path('', views.home, name='home'),  # add a URL pattern for myapp's home view
	# include URL patterns for other apps in your project here

	path ('welcome/', views.welcome, name = 'welcome'),
	path ('mqtt-handler/', views.mqtt_handler, name = 'mqtt_handler')

]

