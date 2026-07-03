from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from django.contrib.auth.views import LogoutView
#from . import views

"""urlpatterns = [
    path('', views.Home, name='home'),
    path('post/<int:post_id>/', views.Detail, name='detail'),
    path('create/', views.create_post, name='create_post'),
    path('edit/<int:post_id>/',views.edit_post,name='edit_post'),
    path('delete/<int:post_id>/',views.delete_post,name='delete_post'),
]"""

urlpatterns=[
    path('', PostListView.as_view(),name='home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('create/', PostCreateView.as_view(), name='create_post'),
    path('edit/<int:pk>/', PostUpdateView.as_view(), name='edit_post'),
    path('delete/<int:pk>/', PostDeleteView.as_view(), name='delete_post'),
    path('logout/', LogoutView.as_view(), name='logout'),  # ✅ ADD THIS


]