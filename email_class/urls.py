from django.urls import path
from .views import home_view, classificar_email_view

urlpatterns = [

    path('', home_view, name='home'),

    path('api/classify/', classificar_email_view, name='classify_email'),
]