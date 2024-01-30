
from django.urls import path
from . import views


urlpatterns = [
     path('', views.index, name= 'index'),
     path('contact/', views.contact_form, name='contact_form'),
     path('about/', views.about, name='about'),
     path('', views.portfolio, name='portfolio'),
     path('admin/skills/', views.skill_list, name='skill_list'),
    path('admin/skills/add/', views.skill_create, name='skill_create'),
    path('admin/skills/<int:skill_id>/', views.skill_update, name='skill_update'),
    path('admin/skills/<int:skill_id>/delete/', views.skill_delete, name='skill_delete'),
]
