from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url


# SET THE NAMESPACE!
app_name = 'breyta'

# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'^main/$',views.inicio, name='main'),
    url(r'^billetera/$',views.billetera, name='billetera'),
    url(r'^store/$',views.store, name='store'),
    url(r'^aboutus/$',views.aboutus, name='aboutus'),
    url(r'', views.index, name='home')
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    ) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)