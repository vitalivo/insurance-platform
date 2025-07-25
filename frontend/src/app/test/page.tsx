
'use client';

import { useEffect, useState } from 'react';
import { productsAPI, Product } from '@/lib/api';

export default function TestPage() {
  const [products, setProducts] = useState<Product[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchProducts = async () => {
      try {
        console.log('Загружаем продукты...');
        const response = await productsAPI.getAll();
        console.log('Ответ API:', response.data);
        setProducts(response.data.results);
      } catch (error) {
        console.error('Ошибка загрузки продуктов:', error);
        setError('Ошибка подключения к API');
      } finally {
        setLoading(false);
      }
    };

    fetchProducts();
  }, []);

  if (loading) {
    return (
      <div className="p-8">
        <div className="text-center">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600 mx-auto"></div>
          <p className="mt-4">Загрузка продуктов...</p>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="p-8">
        <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded">
          <strong>Ошибка:</strong> {error}
          <p className="mt-2">Убедитесь что Django сервер запущен на http://127.0.0.1:8000</p>
        </div>
      </div>
    );
  }

  return (
    <div className="p-8 max-w-4xl mx-auto">
      <h1 className="text-3xl font-bold mb-6">Тест API подключения</h1>
      
      <div className="mb-6">
        <p className="text-green-600 font-semibold">✅ Подключение к API успешно!</p>
        <p className="text-gray-600">Загружено продуктов: {products.length}</p>
      </div>

      <div className="grid gap-6">
        {products.map((product) => (
          <div key={product.id} className="border border-gray-200 p-6 rounded-lg bg-white shadow-sm">
            <div className="flex justify-between items-start mb-3">
              <h3 className="text-xl font-semibold text-gray-900">{product.display_name}</h3>
              <span className="text-sm text-gray-500">ID: {product.id}</span>
            </div>
            <p className="text-gray-600 mb-3">{product.description}</p>
            <div className="flex gap-4 text-sm">
              <span className="text-blue-600">Код: {product.name}</span>
              <span className={product.is_active ? 'text-green-600' : 'text-red-600'}>
                {product.is_active ? '✅ Активен' : '❌ Неактивен'}
              </span>
            </div>
          </div>
        ))}
      </div>

      <div className="mt-8 p-4 bg-blue-50 rounded-lg">
        <h3 className="font-semibold text-blue-900 mb-2">Информация о подключении:</h3>
        <ul className="text-sm text-blue-800 space-y-1">
          <li>• API URL: http://127.0.0.1:8000/api</li>
          <li>• Endpoint: /products/</li>
          <li>• Метод: GET</li>
          <li>• Статус: Подключено</li>
        </ul>
      </div>
    </div>
  );
}
