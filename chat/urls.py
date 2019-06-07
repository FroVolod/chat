from django.conf.urls import include, url                                                                                                                                                     
from django.contrib import admin                                                                                                                                                              
                                                                                                                                                                                              
urlpatterns = [                                                                                                                                                                               
    url(r'^admin/', admin.site.urls),                                                                                                                                                         
    url(r'^auth/', include('djoser.urls')),                                                                                                                                                   
    url(r'^auth/', include('djoser.urls.authtoken')),                                                                                                                                         
    url(r'^auth/', include('djoser.urls.jwt')),                                                                      
]