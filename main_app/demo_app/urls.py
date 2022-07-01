from django.urls import path
from . import views
urlpatterns = [

    path('get_api/', views.get_api),
    path('post_api/', views.post_api),
    path('delete_api/<int:id>/', views.delete_api),

]