import ProductClient from './product-client';

// Серверная функция для статического экспорта
export async function generateStaticParams() {
  return [
    { name: 'osago' },
    { name: 'kasko' },
    { name: 'ifl' },
    { name: 'ns' },
    { name: 'mortgage' },
    { name: 'klezh' },
  ]
}

// Серверный компонент
export default function ProductPage({ params }: { params: { name: string } }) {
  return <ProductClient productName={params.name} />;
}