/** @type {import('next').NextConfig} */
const nextConfig = {
  // Remove static export for development (can be re-enabled for production build)
  // output: 'export',
  images: {
    unoptimized: true,
  },
  trailingSlash: true,
  reactStrictMode: true,
}

module.exports = nextConfig

