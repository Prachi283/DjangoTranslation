from django.urls import path
# HERE
from .views import HomePageView, home

app_name = 'myapp_one'

urlpatterns = [
    path('', 
         HomePageView.as_view(), 
         name='home'),
    # HERE
    path('home/', 
         home,
         name='home_function')
]