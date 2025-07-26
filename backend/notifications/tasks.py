from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
import ssl
import logging

logger = logging.getLogger(__name__)

@shared_task(bind=True, autoretry_for=(Exception,), retry_kwargs={'max_retries': 3, 'countdown': 60})
def send_email_notification(self, subject, message, recipient_email):
    """
    Отправка email уведомлений через Celery с отключенной проверкой SSL
    """
    try:
        # Временно сохраняем оригинальные настройки
        import smtplib
        from django.core.mail.backends.smtp import EmailBackend
        
        # Создаем кастомный backend с отключенной проверкой SSL
        class CustomEmailBackend(EmailBackend):
            def open(self):
                if self.connection:
                    return False
                try:
                    self.connection = smtplib.SMTP(self.host, self.port, timeout=self.timeout)
                    if self.use_tls:
                        # Создаем SSL контекст с отключенной проверкой
                        import ssl
                        context = ssl.create_default_context()
                        context.check_hostname = False
                        context.verify_mode = ssl.CERT_NONE
                        self.connection.starttls(context=context)
                    if self.username and self.password:
                        self.connection.login(self.username, self.password)
                    return True
                except Exception as e:
                    logger.error(f"Email connection error: {e}")
                    if not self.fail_silently:
                        raise
        
        # Используем кастомный backend
        backend = CustomEmailBackend(
            host=settings.EMAIL_HOST,
            port=settings.EMAIL_PORT,
            username=settings.EMAIL_HOST_USER,
            password=settings.EMAIL_HOST_PASSWORD,
            use_tls=settings.EMAIL_USE_TLS,
            use_ssl=settings.EMAIL_USE_SSL,
            fail_silently=False,
        )
        
        from django.core.mail import EmailMessage
        email = EmailMessage(
            subject=subject,
            body=message,
            from_email=settings.EMAIL_HOST_USER,
            to=[recipient_email],
            connection=backend
        )
        
        result = email.send()
        
        if result:
            logger.info(f"✅ Email успешно отправлен на {recipient_email}")
            return f"Email отправлен на {recipient_email}"
        else:
            logger.error(f"❌ Не удалось отправить email на {recipient_email}")
            raise Exception("Email не был отправлен")
            
    except Exception as e:
        logger.error(f"❌ Ошибка отправки email: {e}")
        raise

@shared_task(bind=True, max_retries=3)
def send_telegram_notification(self, message, chat_id=None):
    """Асинхронная отправка Telegram уведомлений"""
    try:
        bot_token = settings.TELEGRAM_BOT_TOKEN
        target_chat_id = chat_id or settings.TELEGRAM_CHAT_ID
        
        if not bot_token or not target_chat_id:
            raise ValueError("Telegram bot token или chat_id не настроены")
        
        import requests
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        data = {
            'chat_id': target_chat_id,
            'text': message,
            'parse_mode': 'HTML'
        }
        
        response = requests.post(url, data=data, timeout=10)
        response.raise_for_status()
        
        logger.info(f"✅ Telegram сообщение отправлено: {target_chat_id}")
        return f"Telegram сообщение отправлено в чат {target_chat_id}"
        
    except Exception as exc:
        logger.error(f"❌ Ошибка отправки Telegram: {exc}")
        raise self.retry(exc=exc, countdown=60)

@shared_task
def send_application_notification(application_data):
    """Комплексное уведомление о новой заявке"""
    try:
        # Формируем сообщения
        subject = f"Новая заявка #{application_data['id']}"
        email_message = f"""
        Получена новая заявка на страхование:
        
        Продукт: {application_data['product_name']}
        Клиент: {application_data['client_name']}
        Email: {application_data['client_email']}
        Телефон: {application_data['client_phone']}
        Дата: {application_data['created_at']}
        """
        
        telegram_message = f"""
        🆕 <b>Новая заявка #{application_data['id']}</b>
        📋 Продукт: {application_data['product_name']}
        👤 Клиент: {application_data['client_name']}
        �� Email: {application_data['client_email']}
        📱 Телефон: {application_data['client_phone']}
        """
        
        # Отправляем уведомления асинхронно
        send_email_notification.delay(
            subject=subject,
            message=email_message,
            recipient_email=settings.ADMIN_EMAIL
        )
        
        send_telegram_notification.delay(
            message=telegram_message
        )
        
        return "Уведомления отправлены в очередь"
        
    except Exception as exc:
        logger.error(f"❌ Ошибка отправки уведомлений: {exc}")
        raise
