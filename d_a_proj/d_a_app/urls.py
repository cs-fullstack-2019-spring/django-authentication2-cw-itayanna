from django.urls import path, include
from . import views





# defining pathways

urlpatterns = [
    path('', views.index, name='index'),
    path('allEntries/', views.allBlogEntries, name='allEntries'),
    path('alEntries/yourEntries/', views.yourEntries, name='yourEntries')
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')), ]
