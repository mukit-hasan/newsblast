from django.urls import path
from . import views

urlpatterns = [
    path('newsletter/', views.sub_or_unsub, name='newletter'),
    path('chkmail/', views.chackmail, name='ckmail')
]
