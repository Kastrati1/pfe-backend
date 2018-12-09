from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
#router.register('app1', views.ProductView)
# ProductView is a class in views

urlpatterns = [
    path('', include(router.urls)),
    path('current_user/', views.current_user),
    path('users/', views.UserList.as_view()),  # inscription
    path('products', views.GetProducts),
    path('productsByCat', views.GetProductsByCategory)

]
