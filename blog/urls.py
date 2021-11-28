from django.urls import path

from . import views
# django 的路由匹配规则有很多类型，除了这里的 int 整数类型，还有 str 字符类型、uuid 等，可以通过官方文档了解
# https://docs.djangoproject.com/en/2.2/topics/http/urls/#path-converters

#指定index、detail函数的使用空间
app_name = 'blog'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    path('about/', views.about, name='about'),
    path('link/', views.LinkView.as_view(), name='link'),
    path('category/', views.category, name='category'),
    path('tag/', views.tag, name='tag'),
    path('categories/<int:pk>/', views.CategoryView.as_view(), name='category_match'),
    path('tags/<int:pk>/', views.TagView.as_view(), name='tag_match'),
]
