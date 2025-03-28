from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('categories/', views.CategoryList.as_view(), name='categories'),
    path('categories/home/', views.HomeCategoryList.as_view(), name='home_categories_list'),
    path('marques/', views.MarqueList.as_view(), name='marques'),
    path('', views.ProducList.as_view(), name='products_list'),
    path('popular/', views.PopularProductList.as_view(), name='popular_products_list'),
    path('byType/', views.ProducListByType.as_view(), name='products_by_type'),
    path('search/', views.SearchProductByTitle.as_view(), name='search_products'),
    path('category/', views.ProductByCategory.as_view(), name='product_by_category'),
    path('recommandations/', views.SimilarProductList.as_view(), name='similar_products_list'),
    # les urls du panier
    path('cart/', views.CartDetailView.as_view(), name='cart-detail'),
    path('cart/add/', views.AddToCartView.as_view(), name='cart-add'),
    path('cart/add/', views.AddToCartView.as_view(), name='add-to-cart'),
    path('cart/remove/<int:item_id>/', views.RemoveFromCartView.as_view(), name='cart-remove'),
    path('cart/update/<int:item_id>/', views.UpdateCartItemView.as_view(), name='cart-update'),
]
    

