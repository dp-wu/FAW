from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
    # <int:pk> means that django expects an integer value and will transfer
    # it to a view as a variable called pk.
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]