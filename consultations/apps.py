from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ConsultationsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'consultations'
    verbose_name = _("Consultations")
