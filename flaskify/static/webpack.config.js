module.exports = {
  entry: [
    './js/app.js'
  ],
  output: {
    path: __dirname + '/dist',
    filename: "index.js"
  },
  module: {
    loaders: [
      {test: /\.js$/, exclude: /node_modules/, loader: "babel-loader"}
    ]
  },
};
