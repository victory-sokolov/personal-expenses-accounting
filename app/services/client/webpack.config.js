const path = require("path");
const htmlWebPackPlugin = require("html-webpack-plugin");
const UglifyJsPlugin = require("uglifyjs-webpack-plugin");
const BundleAnalyzerPlugin = require("webpack-bundle-analyzer")
	.BundleAnalyzerPlugin;

const settings = {
	distPath: path.join(__dirname, "/dist"),
	srcPath: path.join(__dirname, "/"),
};

function srcPathExtend(subpath) {
	return path.join(settings.srcPath, subpath);
}

module.exports = {
	// mode: "production",
	output: {
		path: path.join(__dirname, "/dist"),
		filename: "bundle.js",
	},
	optimization: {
		minimizer: [new UglifyJsPlugin()],
	},
	module: {
		rules: [
			{
				test: /\.js$/,
				exclude: /node_modules/,
				use: {
					loader: "babel-loader",
					options: {
						presets: [
							[
								"@babel/preset-env",
								{
									targets: {
										esmodules: true,
									},
								},
							],
							"@babel/react",
							{
								plugins: ["@babel/plugin-proposal-class-properties"],
							},
						],
					},
				},
			},
			{
				test: /\.(css|scss)/,
				use: [
					"style-loader",
					{
						loader: "css-loader",
						options: {
							sourceMap: true,
							modules: {
								localIdentName: "[path][name]__[local]--[hash:base64:5]",
							},
						},
					},
					{
						loader: "sass-loader",
						options: {
							sourceMap: true,
						},
					},
				],
			},
			{
				test: /\.(png|jpg|gif|svg)$/i,
				use: ["url-loader", "image-webpack-loader"],
			},
		],
	},
	plugins: [
		new BundleAnalyzerPlugin({
			analyzerMode: "disabled",
			generateStatsFile: true,
			statsOptions: { source: false },
		}),
		// new htmlWebPackPlugin({
		//   template: srcPathExtend("index.html")
		// })
	],
	watch: true,
	devtool: "source-map",
};
