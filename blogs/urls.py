from django.urls import path

from . import views

urlpatterns=[
    path('',views.index,name='starting_page'),
    path('posts',views.posts,name='post_page'),
    path('post/<slug:slug>',views.single_post,name='post_detail'),
    path('K',views.Karbaran_list),
    path('P/', views.Product_list, name='product-list'),
    path('P/<slug:slug>', views.product_detail, name='product-detail'),

]
