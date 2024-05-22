from django.urls import path
from . import views


urlpatterns = [
    path('', views.ListProducts.as_view(), name='ListProducts'),
    path('details/<int:pk>/', views.ProductDetails.as_view(), name='ProductDetails'),
    path('add_product/', views.AddProducts.as_view(), name='AddProducts'),
    path('edit_product/<int:pk>/', views.EditProduct.as_view(), name='EditProduct'),
    path('delete_product/<int:pk>/', views.delete_product, name='delete_product'),

    path('my_profile/<int:pk>/', views.MyProfile.as_view(), name='MyProfile'),
    path('profile/<int:pk>/', views.Profile.as_view(), name='Profile'),
    path('my_profile_edit/<int:pk>/', views.EditProfile.as_view(), name='EditProfile'),

    path('add_comment/<int:pk>/', views.AddComment.as_view(), name='AddComment'),
    path('edit_comment/<int:pk>/', views.EditComment.as_view(), name='EditComment'),
    path('delete_comment/<int:pk>/', views.delete_comment, name='delete_comment'),

    path('list_categories/', views.ListCategories.as_view(), name='ListCategories'),
    path('filter_categories/<int:pk>/', views.FilterCategories.as_view(), name='FilterCategories')
]
