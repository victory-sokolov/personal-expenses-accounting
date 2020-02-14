const path = require('path');
const htmlWebPackPlugin = require('html-webpack-plugin');

const settings = {
  distPath: path.join(__dirname, "/dist"),
  srcPath: path.join(__dirname, "/")
};

function srcPathExtend(subpath) {
  return path.join(settings.srcPath, subpath)
}

module.exports = {
  output: {
    path: path.join(__dirname, '/dist'),
    filename: 'bundle.js'
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader',
          options: {
            presets: [
              '@babel/preset-env',
              '@babel/react', {
                'plugins': ['@babel/plugin-proposal-class-properties']
              }]
          }
        }
      },
      {
        test: /\.css$/,
        loader: 'style-loader!css-loader'
      },
      {
        test: /\.(png|jpg|gif)$/i,
        use: [
          {
            loader: 'url-loader',
            options: {
              // limit: 8192,
            },
          },
        ],
      }
    ]
  },
  plugins: [
    // new htmlWebPackPlugin({
    //   template: srcPathExtend("index.html")
    // })
  ],
  watch: true
}
