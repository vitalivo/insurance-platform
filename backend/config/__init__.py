import ssl
from django.core.mail.backends.smtp import EmailBackend

class CustomSMTPBackend(EmailBackend):
    def open(self):
        if self.connection:
            return False
        try:
            self.connection = self.connection_class(
                host=self.host, port=self.port, timeout=self.timeout
            )
            if self.use_tls:
                context = ssl.create_default_context()
                context.check_hostname = False
                context.verify_mode = ssl.CERT_NONE
                self.connection.starttls(context=context)
            if self.username and self.password:
                self.connection.login(self.username, self.password)
            return True
        except Exception:
            if not self.fail_silently:
                raise
            
            
# EMAIL настройки
EMAIL_BACKEND = 'config.settings.CustomSMTPBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_HOST_USER = 'vitalivo@gmail.com'
EMAIL_HOST_PASSWORD = 'avsx tsjl brds cmlf'
DEFAULT_FROM_EMAIL = 'vitalivo@gmail.com'
ADMIN_EMAIL = 'vitalivo@gmail.com'     

# Принудительно установим наш backend
import sys
sys.modules[__name__].CustomSMTPBackend = CustomSMTPBackend      

# Это обеспечит загрузку Celery при старте Django
from .celery import app as celery_app

__all__ = ('celery_app',) 