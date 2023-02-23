from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('products/', views.getProducts, name='getProducts'),
    path('search_products/<name>', views.searchProducts, name='searchProducts'),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path('add_to_cart/<product_id>', views.add_to_cart, name='add_to_cart'),
    path('get_user_cart/<user_id>', views.get_user_cart, name='get_user_cart'),
    path('execute_order/<order_id>', views.execute_order, name='execute_order'),
    path('get_user_orders/<user_id>', views.get_user_orders, name='get_user_orders'),

]
