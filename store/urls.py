from django.urls import path

from . import views

app_name='store'
urlpatterns=[
    path('checkout/',views.checkout,name='checkout'),
    path('product_list/',views.product_list,name='product_list'),
    path('product_detail/<slug:slug>/',views.product_detail,name='product_detail'),
    path('category_detail/<slug:slug>/',views.category_detail,name='category_detail'),
    path('cart_detail/',views.cart_detail,name='cart_detail'),
    path('add/<int:product_id>/',views.add_to_cart,name='add_to_cart'),
    path('remove/<int:product_id>/',views.remove_from_cart,name='remove_from_cart'),

]