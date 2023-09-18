from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('view/<int:pk>', views.view_player, name='view'),
    path('delete/<int:pk>', views.delete_player, name='delete'),
    path('add/', views.add_player, name='add'),
    path('update/<int:pk>', views.update_player, name='update'),
]
