/** @type {import('next').NextConfig} */
const nextConfig = {
  output: 'export',
  trailingSlash: true,
  images: {
    unoptimized: true
  },
  // Исключить динамические маршруты из экспорта
  exportPathMap: async function () {
    return {
      '/': { page: '/' },
      '/track': { page: '/track' },
    }
  }
}

module.exports = nextConfig

