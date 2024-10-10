from django.urls import path
from . import views
from .views import HomeView,ArticleDetailView,AddPostView,UpdatePostView,DeletePostView,AddCatergoryView,CategoryView,CategoryListView,LikeView,AddCommentView
urlpatterns = [
    #path('',views.home,name="home"),
    path('',HomeView.as_view(),name="home"),
    path('article/<int:pk>',ArticleDetailView.as_view(),name="article_detail"),
    path('add_post/',AddPostView.as_view(),name="add_post"),
    path('update_post/<int:pk>',UpdatePostView.as_view(),name="update_post"),
    path('delete_post/<int:pk>',DeletePostView.as_view(),name="delete_post"),
    path('add_category/',AddCatergoryView.as_view(),name="add_category"),
    path('category/<str:cats>/',CategoryView,name='category'),
    path('category_list/',CategoryListView,name='category_list'),
    path('like_post/<int:pk>',LikeView,name='like_post'),
    path('add_comment/',views.add_comment,name="add_comment"),
    path('search_box/',views.search_box,name="search_box"),
    path('delete_comment/<int:id>',views.delete_comment,name="delete_comment"),
]