module.exports = {
    publicPath: './',
    devServer: {
        proxy: {
            '^/api': {
                target: 'https://localhost:8080',
                changeOrigin: true,
                logLevel: 'debug',
                pathRewrite: { '^/api': '/' },
            },
        },
    },
}