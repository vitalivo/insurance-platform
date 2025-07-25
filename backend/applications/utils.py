from django.core.mail import send_mail
from django.conf import settings
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import ssl

def send_application_notification(application):
    """Отправляет email уведомления о новой заявке"""
    
    print(f"🔄 Начинаем отправку email для заявки #{application.application_number}")
    
    # Создаем SSL контекст без проверки сертификатов
    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE
    
    try:
        # Подключаемся к SMTP серверу
        server = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
        server.starttls(context=context)
        server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
        
        # 📧 Email клиенту
        print(f"📧 Отправляем email клиенту: {application.email}")
        
        customer_msg = MIMEMultipart()
        customer_msg['From'] = settings.DEFAULT_FROM_EMAIL
        customer_msg['To'] = application.email
        customer_msg['Subject'] = f'Ваша заявка #{application.application_number} получена'
        
        customer_body = f"""Здравствуйте, {application.full_name}!

Ваша заявка #{application.application_number} успешно получена и находится в обработке.

Детали заявки:
- Продукт: {application.product.name}
- Дата создания: {application.created_at.strftime('%d.%m.%Y %H:%M')}
- Статус: {application.status.name}

Вы можете отслеживать статус вашей заявки по ссылке:
http://localhost:3000/tracking?number={application.application_number}

С уважением,
Команда страховой компании"""
        
        customer_msg.attach(MIMEText(customer_body, 'plain'))
        server.send_message(customer_msg)
        print(f"✅ Email клиенту отправлен успешно")
        
        # 📧 Email администратору
        print(f"📧 Отправляем email администратору: {settings.ADMIN_EMAIL}")
        
        admin_msg = MIMEMultipart()
        admin_msg['From'] = settings.DEFAULT_FROM_EMAIL
        admin_msg['To'] = settings.ADMIN_EMAIL
        admin_msg['Subject'] = f'Новая заявка #{application.application_number}'
        
        admin_body = f"""Поступила новая заявка #{application.application_number}.

Детали заявки:
- Продукт: {application.product.name}
- Клиент: {application.full_name}
- Телефон: {application.phone}
- Email: {application.email}
- Дата создания: {application.created_at.strftime('%d.%m.%Y %H:%M')}

Для управления заявкой перейдите в панель администратора."""
        
        admin_msg.attach(MIMEText(admin_body, 'plain'))
        server.send_message(admin_msg)
        print(f"✅ Email администратору отправлен успешно")
        
        server.quit()
        
    except Exception as e:
        print(f"❌ Ошибка отправки email: {e}")
        raise e

def send_sms_notification(application):
    """Отправляет SMS уведомление клиенту"""
    
    message = f"Ваша заявка #{application.application_number} получена. Отслеживание: http://localhost:3000/tracking?number={application.application_number}"
    
    print(f"📱 SMS отправлено на {application.phone}: {message}")