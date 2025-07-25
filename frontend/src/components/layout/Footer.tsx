
export default function Footer() {
  return (
    <footer className="bg-gray-100 border-t border-gray-200">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
        <div className="flex flex-col md:flex-row justify-between items-center">
          {/* Логотип и описание */}
          <div className="flex items-center mb-4 md:mb-0">
            <div className="w-6 h-6 bg-blue-600 rounded flex items-center justify-center mr-2">
              <span className="text-white font-bold text-xs">СП</span>
            </div>
            <div>
              <span className="text-gray-800 font-semibold">Страховая платформа</span>
              <p className="text-gray-500 text-xs mt-1">
                Быстрое оформление страховых полисов онлайн
              </p>
            </div>
          </div>
          
          {/* Контакты */}
          <div className="flex items-center space-x-6">
            <div className="text-sm text-gray-600">
              <div className="flex items-center">
                <span className="mr-2">📱</span>
                <span>8 (800) 123-45-67</span>
              </div>
            </div>
            <div className="text-sm text-gray-600">
              <div className="flex items-center">
                <span className="mr-2">✉️</span>
                <span>support@insurance.ru</span>
              </div>
            </div>
          </div>
        </div>
        
        {/* Нижняя строка */}
        <div className="flex flex-col md:flex-row justify-between items-center mt-4 pt-4 border-t border-gray-200 text-sm">
          <p className="text-gray-500 text-xs mb-2 md:mb-0">
            © 2025 Страховая платформа. Все права защищены.
          </p>
          <div className="flex space-x-4">
            <a href="#" className="text-gray-500 hover:text-blue-600 transition-colors text-xs">
              Политика конфиденциальности
            </a>
            <a href="#" className="text-gray-500 hover:text-blue-600 transition-colors text-xs">
              Условия использования
            </a>
          </div>
        </div>
      </div>
    </footer>
  );
}
