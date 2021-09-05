module.exports = {
  devServer: {
    proxy: 'http://localhost:8000'
  },
  publicPath: process.env.NODE_ENV === 'production'
    ? '/static/'
    : '/'
}