
import Link from 'next/link';

export default function Home() {
  return (
    <main className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100">
      <div className="container mx-auto px-4 py-16">
        <div className="text-center max-w-4xl mx-auto">
          <h1 className="text-5xl font-bold text-gray-900 mb-6">
            Страховая платформа
          </h1>
          <p className="text-xl text-gray-600 mb-8">
            Быстрое и удобное оформление страховых полисов онлайн
          </p>
          
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mt-12">
            <div className="bg-white p-6 rounded-lg shadow-md hover:shadow-lg transition-shadow">
              <div className="text-4xl mb-4">🚗</div>
              <h3 className="text-xl font-semibold text-gray-900 mb-3">ОСАГО</h3>
              <p className="text-gray-600 mb-4">Обязательное страхование автогражданской ответственности</p>
              <Link 
                href="/products/osago"
                className="block w-full bg-primary-600 text-white py-2 px-4 rounded-md hover:bg-primary-700 transition-colors text-center"
              >
                Оформить
              </Link>
            </div>
            
            <div className="bg-white p-6 rounded-lg shadow-md hover:shadow-lg transition-shadow">
              <div className="text-4xl mb-4">🛡️</div>
              <h3 className="text-xl font-semibold text-gray-900 mb-3">КАСКО</h3>
              <p className="text-gray-600 mb-4">Добровольное страхование автотранспорта от угона и ущерба</p>
              <Link 
                href="/products/kasko"
                className="block w-full bg-primary-600 text-white py-2 px-4 rounded-md hover:bg-primary-700 transition-colors text-center"
              >
                Оформить
              </Link>
            </div>
            
            <div className="bg-white p-6 rounded-lg shadow-md hover:shadow-lg transition-shadow">
              <div className="text-4xl mb-4">🏠</div>
              <h3 className="text-xl font-semibold text-gray-900 mb-3">Недвижимость</h3>
              <p className="text-gray-600 mb-4">Страхование квартир, домов и личного имущества</p>
              <Link 
                href="/products/ifl"
                className="block w-full bg-primary-600 text-white py-2 px-4 rounded-md hover:bg-primary-700 transition-colors text-center"
              >
                Оформить
              </Link>
            </div>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mt-6">
            <div className="bg-white p-6 rounded-lg shadow-md hover:shadow-lg transition-shadow">
              <div className="text-4xl mb-4">🏥</div>
              <h3 className="text-xl font-semibold text-gray-900 mb-3">Несчастный случай</h3>
              <p className="text-gray-600 mb-4">Страхование от несчастных случаев и болезней</p>
              <Link 
                href="/products/ns"
                className="block w-full bg-primary-600 text-white py-2 px-4 rounded-md hover:bg-primary-700 transition-colors text-center"
              >
                Оформить
              </Link>
            </div>
            
            <div className="bg-white p-6 rounded-lg shadow-md hover:shadow-lg transition-shadow">
              <div className="text-4xl mb-4">🏡</div>
              <h3 className="text-xl font-semibold text-gray-900 mb-3">Ипотека</h3>
              <p className="text-gray-600 mb-4">Страхование ипотечного имущества и титула собственности</p>
              <Link 
                href="/products/mortgage"
                className="block w-full bg-primary-600 text-white py-2 px-4 rounded-md hover:bg-primary-700 transition-colors text-center"
              >
                Оформить
              </Link>
            </div>
            
            <div className="bg-white p-6 rounded-lg shadow-md hover:shadow-lg transition-shadow">
              <div className="text-4xl mb-4">🦠</div>
              <h3 className="text-xl font-semibold text-gray-900 mb-3">Клещ</h3>
              <p className="text-gray-600 mb-4">Страхование от укуса клеща и клещевого энцефалита</p>
              <Link 
                href="/products/klezh"
                className="block w-full bg-primary-600 text-white py-2 px-4 rounded-md hover:bg-primary-700 transition-colors text-center"
              >
                Оформить
              </Link>
            </div>
          </div>

          <div className="mt-12 p-6 bg-white rounded-lg shadow-md">
            <h2 className="text-2xl font-semibold text-gray-900 mb-4">Почему выбирают нас?</h2>
            <div className="grid grid-cols-1 md:grid-cols-3 gap-6 text-left">
              <div>
                <div className="text-2xl mb-2">⚡</div>
                <h4 className="font-semibold mb-2">Быстро</h4>
                <p className="text-gray-600 text-sm">Оформление заявки за 5 минут</p>
              </div>
              <div>
                <div className="text-2xl mb-2">🔒</div>
                <h4 className="font-semibold mb-2">Безопасно</h4>
                <p className="text-gray-600 text-sm">Защита персональных данных</p>
              </div>
              <div>
                <div className="text-2xl mb-2">📞</div>
                <h4 className="font-semibold mb-2">Поддержка</h4>
                <p className="text-gray-600 text-sm">Консультации 24/7</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </main>
  )
}
