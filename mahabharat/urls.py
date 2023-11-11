from  mahabharat.views import*
from django.urls import path
app_name = 'Dharma'

urlpatterns=[
    path('madhava/',madhava,name='madhava')
]