/** @type {import('next').NextConfig} */
const nextConfig = {
  output: 'export',
  trailingSlash: true,
  basePath: '/insurance-platform',
  assetPrefix: '/insurance-platform',
  images: {
    unoptimized: true
  }
}

module.exports = nextConfig

