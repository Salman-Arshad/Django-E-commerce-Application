from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('category/<cat>',views.category,name="categories"),
    path('product/<id>', views.product, name='product'),
    path('product/<id>/addtocart/<quantity>', views.addtocart, name='Product'),
    path('cart', views.cart, name='cart'),
    path('cart/clear',views.clearCart,name='cart')
]
