from hanuman.views import*
from django.urls import path
app_name ='devotional'

urlpatterns=[
    path('hanuman/',hanuman,name='hanuman'),
]