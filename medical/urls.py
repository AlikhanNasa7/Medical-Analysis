from django.urls import path
from . import views


app_name = 'medical'

urlpatterns = [
    path('contacts/', views.post_contacts, name='contacts'),
    path('medicals/', views.post_medicals, name='medicals'),
    path('analysis/', views.get_analysis, name='analysis' )
]