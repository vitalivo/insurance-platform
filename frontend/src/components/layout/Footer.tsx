
export default function Footer() {
  return (
    <footer className="bg-gray-900 text-white">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-8">
          <div className="col-span-1 md:col-span-2">
            <div className="flex items-center space-x-2 mb-4">
              <div className="w-8 h-8 bg-blue-600 rounded-lg flex items-center justify-center">
                <span className="text-white font-bold text-sm">СП</span>
              </div>
              <span className="text-xl font-bold">Страховая платформа</span>
            </div>
            <p className="text-gray-400 mb-4">
              Быстрое и удобное оформление страховых полисов онлайн. 
              Надежная защита для вас и вашего имущества.
            </p>
            <div className="flex space-x-4">
              <span className="text-gray-400">📱 +7 (800) 123-45-67</span>
              <span className="text-gray-400">✉️ support@insurance.ru</span>
            </div>
          </div>
          
          <div>
            <h3 className="text-sm font-semibold uppercase tracking-wider mb-4">
              Продукты
            </h3>
            <ul className="space-y-2">
              <li><a href="/products/osago" className="text-gray-400 hover:text-white transition-colors">ОСАГО</a></li>
              <li><a href="/products/kasko" className="text-gray-400 hover:text-white transition-colors">КАСКО</a></li>
              <li><a href="/products/ifl" className="text-gray-400 hover:text-white transition-colors">Недвижимость</a></li>
              <li><a href="/products/ns" className="text-gray-400 hover:text-white transition-colors">Несчастный случай</a></li>
              <li><a href="/products/mortgage" className="text-gray-400 hover:text-white transition-colors">Ипотека</a></li>
              <li><a href="/products/klezh" className="text-gray-400 hover:text-white transition-colors">Клещ</a></li>
            </ul>
          </div>
          
          <div>
            <h3 className="text-sm font-semibold uppercase tracking-wider mb-4">
              Сервисы
            </h3>
            <ul className="space-y-2">
              <li><a href="/track" className="text-gray-400 hover:text-white transition-colors">Отследить заявку</a></li>
              <li><a href="http://127.0.0.1:8000/admin/" target="_blank" className="text-gray-400 hover:text-white transition-colors">Админ панель</a></li>
              <li><span className="text-gray-500">Поддержка 24/7</span></li>
            </ul>
          </div>
          
          <div>
            <h3 className="text-sm font-semibold uppercase tracking-wider mb-4">
              Контакты
            </h3>
            <ul className="space-y-2">
              <li><span className="text-gray-400">Телефон:</span></li>
              <li><span className="text-gray-300">8 (800) 123-45-67</span></li>
              <li><span className="text-gray-400">Email:</span></li>
              <li><span className="text-gray-300">support@insurance.ru</span></li>
            </ul>
          </div>
        </div>
        
        <div className="border-t border-gray-800 mt-8 pt-8 flex flex-col md:flex-row justify-between items-center">
          <p className="text-gray-400 text-sm">
            © 2025 Страховая платформа. Все права защищены.
          </p>
          <div className="flex space-x-6 mt-4 md:mt-0">
            <span className="text-gray-500 text-sm">Политика конфиденциальности</span>
            <span className="text-gray-500 text-sm">Условия использования</span>
          </div>
        </div>
      </div>
    </footer>
  );
}
