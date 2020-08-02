from django.urls import path
from . import views
urlpatterns = [
    path('', views.HomePageView.as_view(), name="home"),
    path('search/', views.search, name="search"),
    path('signup/', views.SignUpView.as_view(), name="signup"),
    path('profile/',views.view_profile,name="view_profile"),
    # path('profile/edit/',views.edit_profile,name="edit_profile"),
    path('detail/<int:pk>/', views.FPDetailView.as_view(), name="detail"),
    # path('profile/change_password/',views.change_password,name="change_password"),
]