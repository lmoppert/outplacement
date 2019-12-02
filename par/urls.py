from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.PARDetail.as_view(), name='par-detail'),
    path('skill/<int:pk>/', views.SkillDetail.as_view(), name='skill-detail'),
]
