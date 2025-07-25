
import './globals.css'

export const metadata = {
  title: 'Страховая платформа',
  description: 'Система подачи заявок на страхование',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="ru">
      <body className="bg-gray-50 text-gray-900 antialiased">{children}</body>
    </html>
  )
}
