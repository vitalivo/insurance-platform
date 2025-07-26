from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
import requests
import logging

logger = logging.getLogger(__name__)

@shared_task(bind=True, max_retries=3)
def send_email_notification(self, subject, message, recipient_email):
    """Асинхронная отправка email уведомлений"""
    try:
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[recipient_email],
            fail_silently=False,
        )
        logger.info(f"✅ Email отправлен: {recipient_email}")
        return f"Email успешно отправлен на {recipient_email}"
    
    except Exception as exc:
        logger.error(f"❌ Ошибка отправки email: {exc}")
        # Повторная попытка через 60 секунд
        raise self.retry(exc=exc, countdown=60)

@shared_task(bind=True, max_retries=3)
def send_telegram_notification(self, message, chat_id=None):
    """Асинхронная отправка Telegram уведомлений"""
    try:
        bot_token = settings.TELEGRAM_BOT_TOKEN
        target_chat_id = chat_id or settings.TELEGRAM_CHAT_ID
        
        if not bot_token or not target_chat_id:
            raise ValueError("Telegram bot token или chat_id не настроены")
        
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
        📧 Email: {application_data['client_email']}
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