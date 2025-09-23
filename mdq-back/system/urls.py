from django.contrib import admin
from django.urls import include, path
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from turnstile.fields import TurnstileField


class XugarPasswordResetForm(PasswordResetForm):
    turnstile = TurnstileField()


class XugarPasswordResetView(PasswordResetView):
    form_class = XugarPasswordResetForm


urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path('accounts/password_reset/', XugarPasswordResetView.as_view(template_name="registration/password-reset.html")),
    path('accounts/password_reset/done/', PasswordResetDoneView.as_view(template_name="registration/password-reset-done.html")),
    path('accounts/reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name="registration/password-reset-change.html")),
    path('accounts/reset/done/', PasswordResetCompleteView.as_view(template_name="registration/password-reset-complete.html")),
    path('', include('mdq.urls')),
] + staticfiles_urlpatterns() + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

