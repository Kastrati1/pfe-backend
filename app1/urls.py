from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('products', views.ProductsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('current_user/', views.Current_user),
    path('current_user_products/', views.GetUserProducts),
    path('users/', views.UserList.as_view()),
    path('productsByCat', views.ProductsByCat.as_view()),
    path('allCategories', views.GetAllCategories),
    path('pay', views.StripeView.as_view()),
    path('getProduct', views.GetProductByIdView.as_view()),

]
