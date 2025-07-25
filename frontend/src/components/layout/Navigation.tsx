
'use client';

import Link from 'next/link';
import { usePathname } from 'next/navigation';

export default function Navigation() {
  const pathname = usePathname();

  const isActive = (path: string) => {
    return pathname === path ? 'text-blue-600 font-semibold' : 'text-gray-700 hover:text-blue-600';
  };

  return (
    <nav className="bg-white shadow-sm border-b sticky top-0 z-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between h-16">
          <div className="flex items-center">
            <Link href="/" className="flex items-center space-x-2">
              <div className="w-8 h-8 bg-blue-600 rounded-lg flex items-center justify-center">
                <span className="text-white font-bold text-sm">СП</span>
              </div>
              <span className="text-xl font-bold text-gray-900">
                Страховая платформа
              </span>
            </Link>
          </div>
          
          <div className="flex items-center space-x-6">
            <Link 
              href="/" 
              className={`transition-colors \${isActive('/')}`}
            >
              Главная
            </Link>
            <Link 
              href="/track" 
              className={`transition-colors \${isActive('/track')}`}
            >
              Отследить заявку
            </Link>
            <div className="h-6 w-px bg-gray-300"></div>
            <Link 
              href="http://127.0.0.1:8000/admin/" 
              target="_blank"
              className="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700 transition-colors text-sm"
            >
              Админ панель
            </Link>
          </div>
        </div>
      </div>
    </nav>
  );
}
