# API Endpoints Documentation

## Базовый URL
http://127.0.0.1:8000/api/

## Продукты (Products)

### GET /api/products/
Получить список всех активных страховых продуктов

### GET /api/products/{name}/
Получить детали конкретного продукта
Доступные продукты: osago, kasko, ns, klezh, mortgage, ifl

## Заявки (Applications)

### POST /api/applications/create/
Создать новую заявку

### GET /api/applications/{application_number}/
Получить детали заявки по номеру

## Примеры:
- GET /api/products/osago/
- POST /api/applications/create/
- GET /api/applications/APP-20250724180248/
