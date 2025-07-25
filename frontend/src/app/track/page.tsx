
'use client';

import { useState } from 'react';
import { applicationsAPI } from '@/lib/api';
import Breadcrumbs from '@/components/ui/Breadcrumbs';
import Loading from '@/components/ui/Loading';

interface ApplicationStatus {
  id: number;
  name: string;
  description: string;
  color: string;
}

interface ApplicationData {
  id: number;
  application_number: string;
  product: {
    id: number;
    name: string;
    display_name: string;
    description: string;
  };
  status: ApplicationStatus;
  full_name: string;
  phone: string;
  email: string;
  birth_date: string;
  comment: string;
  created_at: string;
}

export default function TrackPage() {
  const [applicationNumber, setApplicationNumber] = useState('');
  const [application, setApplication] = useState<ApplicationData | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleSearch = async (e: React.FormEvent) => {
    e.preventDefault();
    
    if (!applicationNumber.trim()) {
      setError('Введите номер заявки');
      return;
    }

    setLoading(true);
    setError(null);
    setApplication(null);

    try {
      const response = await applicationsAPI.getByNumber(applicationNumber.trim());
      setApplication(response.data);
    } catch (error: any) {
      if (error.response?.status === 404) {
        setError('Заявка с таким номером не найдена');
      } else {
        setError('Ошибка при поиске заявки. Попробуйте еще раз.');
      }
      console.error('Ошибка поиска заявки:', error);
    } finally {
      setLoading(false);
    }
  };

  const formatDate = (dateString: string) => {
    return new Date(dateString).toLocaleString('ru-RU', {
      year: 'numeric',
      month: 'long',
      day: 'numeric',
      hour: '2-digit',
      minute: '2-digit'
    });
  };

  return (
    <div className="min-h-screen bg-gray-50">
      <Breadcrumbs />
      
      <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div className="text-center mb-8">
          <h1 className="text-3xl font-bold text-gray-900 mb-4">
            Отслеживание заявки
          </h1>
          <p className="text-lg text-gray-600">
            Введите номер заявки для получения актуальной информации о статусе
          </p>
        </div>

        <div className="bg-white rounded-lg shadow-md p-6 mb-8">
          <form onSubmit={handleSearch} className="flex gap-4">
            <div className="flex-1">
              <label htmlFor="application_number" className="block text-sm font-medium text-gray-700 mb-2">
                Номер заявки
              </label>
              <input
                type="text"
                id="application_number"
                value={applicationNumber}
                onChange={(e) => setApplicationNumber(e.target.value)}
                className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                placeholder="APP-20250125123456"
                disabled={loading}
              />
            </div>
            <div className="flex items-end">
              <button
                type="submit"
                disabled={loading}
                className="bg-blue-600 text-white px-6 py-2 rounded-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
              >
                {loading ? 'Поиск...' : 'Найти'}
              </button>
            </div>
          </form>
        </div>

        {loading && (
          <div className="bg-white rounded-lg shadow-md p-8">
            <Loading text="Поиск заявки..." />
          </div>
        )}

        {error && (
          <div className="bg-white rounded-lg shadow-md p-6 mb-8">
            <div className="bg-red-50 border border-red-200 rounded-md p-4">
              <div className="flex">
                <div className="flex-shrink-0">
                  <svg className="h-5 w-5 text-red-400" viewBox="0 0 20 20" fill="currentColor">
                    <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" clipRule="evenodd" />
                  </svg>
                </div>
                <div className="ml-3">
                  <h3 className="text-sm font-medium text-red-800">
                    Заявка не найдена
                  </h3>
                  <div className="mt-2 text-sm text-red-700">
                    <p>{error}</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        )}

        {application && (
          <div className="bg-white rounded-lg shadow-md p-6">
            <div className="border-b border-gray-200 pb-6 mb-6">
              <div className="flex items-center justify-between">
                <h2 className="text-2xl font-bold text-gray-900">
                  Заявка {application.application_number}
                </h2>
                <div className="flex items-center">
                  <span 
                    className="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium"
                    style={{ 
                      backgroundColor: application.status.color + '20',
                      color: application.status.color 
                    }}
                  >
                    ● {application.status.name}
                  </span>
                </div>
              </div>
              <p className="text-gray-600 mt-2">{application.status.description}</p>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div>
                <h3 className="text-lg font-semibold text-gray-900 mb-4">Информация о продукте</h3>
                <div className="space-y-3">
                  <div>
                    <span className="text-sm font-medium text-gray-500">Продукт:</span>
                    <p className="text-gray-900">{application.product.display_name}</p>
                  </div>
                  <div>
                    <span className="text-sm font-medium text-gray-500">Описание:</span>
                    <p className="text-gray-900">{application.product.description}</p>
                  </div>
                  <div>
                    <span className="text-sm font-medium text-gray-500">Дата подачи:</span>
                    <p className="text-gray-900">{formatDate(application.created_at)}</p>
                  </div>
                </div>
              </div>

              <div>
                <h3 className="text-lg font-semibold text-gray-900 mb-4">Контактная информация</h3>
                <div className="space-y-3">
                  <div>
                    <span className="text-sm font-medium text-gray-500">ФИО:</span>
                    <p className="text-gray-900">{application.full_name}</p>
                  </div>
                  <div>
                    <span className="text-sm font-medium text-gray-500">Телефон:</span>
                    <p className="text-gray-900">{application.phone}</p>
                  </div>
                  <div>
                    <span className="text-sm font-medium text-gray-500">Email:</span>
                    <p className="text-gray-900">{application.email}</p>
                  </div>
                  {application.comment && (
                    <div>
                      <span className="text-sm font-medium text-gray-500">Комментарий:</span>
                      <p className="text-gray-900">{application.comment}</p>
                    </div>
                  )}
                </div>
              </div>
            </div>

            <div className="mt-8 pt-6 border-t border-gray-200">
              <div className="bg-blue-50 rounded-lg p-4">
                <h4 className="text-sm font-medium text-blue-900 mb-2">Что дальше?</h4>
                <p className="text-sm text-blue-800">
                  Наши специалисты рассматривают вашу заявку. 
                  При необходимости мы свяжемся с вами по указанному телефону или email.
                </p>
              </div>
            </div>
          </div>
        )}

        <div className="mt-8 bg-white rounded-lg shadow-md p-6">
          <h3 className="text-lg font-semibold text-gray-900 mb-4">Нужна помощь?</h3>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
            <div className="text-center p-4 border border-gray-200 rounded-lg">
              <div className="text-2xl mb-2">📞</div>
              <h4 className="font-medium text-gray-900 mb-1">Телефон</h4>
              <p className="text-sm text-gray-600">8 (800) 123-45-67</p>
            </div>
            <div className="text-center p-4 border border-gray-200 rounded-lg">
              <div className="text-2xl mb-2">✉️</div>
              <h4 className="font-medium text-gray-900 mb-1">Email</h4>
              <p className="text-sm text-gray-600">support@insurance.ru</p>
            </div>
            <div className="text-center p-4 border border-gray-200 rounded-lg">
              <div className="text-2xl mb-2">💬</div>
              <h4 className="font-medium text-gray-900 mb-1">Чат</h4>
              <p className="text-sm text-gray-600">Онлайн поддержка</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
