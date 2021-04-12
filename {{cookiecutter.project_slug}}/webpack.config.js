const path = require('path');
const glob = require('glob');
const webpack = require('webpack'); 
const ReactRefreshWebpackPlugin = require('@pmmmwh/react-refresh-webpack-plugin');

const entryArray = glob.sync('./front/src/**.js');

const entryObject = entryArray.reduce((acc, item) => {
    const name = item.replace('.js', '').replace('./front/src/', '');
    acc[name] = item;
    return acc;
  }, {}); 

module.exports = {
    mode: 'development',
    entry: entryObject,

    output: {
        path: path.resolve(__dirname, 'static/js'),
        filename: '[name].bundle.js',
        publicPath: "/static/js/",
    },

    resolve: {
        extensions: ['.js', '.jsx']
    },

    module: {
        rules: [
            { test: /\.js[x]?$/, use: 'babel-loader'}
        ]
    },

    devServer: {
        contentBase: path.resolve(__dirname, 'static/js'),
        publicPath: "/static/js/",
        port: 8090,
        hotOnly: true,
        writeToDisk: true,
        headers: {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, PATCH, OPTIONS",
            "Access-Control-Allow-Headers":
                "X-Requested-With, content-type, Authorization",
        },
    },

    plugins: [
        new webpack.HotModuleReplacementPlugin(),
        new ReactRefreshWebpackPlugin({
            overlay: {
                sockPort: 8090,
            },
        }),
    ]
}