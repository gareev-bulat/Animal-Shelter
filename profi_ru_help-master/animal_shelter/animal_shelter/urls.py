from django.contrib import admin
from django.urls import path
from page import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index),
    path('news', views.news, name='news'),
    path('pets', views.pet_list, name='pets'),
    path('volunteering', views.volunteering, name='volunteering'),
    # path('contacts', views.contacts, name='contacts'),
    path(r'admin', admin.site.urls),
    path('pets/<int:pk>/', views.pet_detail, name='pet_detail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
