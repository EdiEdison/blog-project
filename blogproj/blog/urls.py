from django.urls import path
from . import views

urlpatterns = [
    # this was the path for the function-based views
    # path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),

    # this is the class based view
    path('', views.PostListView.as_view(), name='blog-home'),
    path('post<int:pk>/', views.PostDetailView.as_view(), name='blog-detail'),
]
