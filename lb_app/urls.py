from django.urls import path
from .import views

urlpatterns = [
    path('',views.index),
    path('insert',views.insertBookdetail,name='insert'),
    path('show',views.showbook),
    path('delete/<int:id>',views.deletebook,name='deletion'),
    path('edit/<int:id>', views.updatebook, name='edition'),

]