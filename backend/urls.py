from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.urls import include, path

from core.views import PasswordResetConfirmView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('api/products/', include('core.urls')),
    #path('auth/users/reset_password/<uid>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
     # Confirm reset password
    #path('auth/', include('djoser.urls.jwt')),
]

# Servir les fichiers médias en mode développement
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()


