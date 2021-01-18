from django.urls import path

from blog import views

urlpatterns = [
    path('', views.allblogs, name='allblogs'),

    # '<int:blog_id>/' means: look for an 'int', after the '/blog', and this will be saved as 'blog_id' :
    path('<int:blog_id>/', views.detail, name='detail'),
]
