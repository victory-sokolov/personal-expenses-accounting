import React, { Component } from "react";
import ReactApexChart from "react-apexcharts";
import cards from "../Cards/cards.scss";

class YearChart extends Component {
	constructor(props) {
		super(props);

		this.state = {
			series: [
				{
					name: "Expenses",
					data: [23, 34, 12, 64, 32, 43, 23, 34, 12, 54, 32, 43]
				}
			],
			options: {
				chart: {
					type: "line",
					height: 250
				},
				markers: {
					size: 6,
					colors: ["#FFA41B"],
					strokeColors: "#fff",
					strokeWidth: 2,
					hover: {
						size: 7
					}
                },
				stroke: {
					width: 4,
					curve: "smooth"
				},
				yaxis: {
					labels: {
						minWidth: 40
					}
				},
				xaxis: {
					type: "text",
					categories: [
						"Jan",
						"Feb",
						"Mar",
						"Apr",
						"May",
						"Jun",
						"Jul",
						"Aug",
						"Sep",
						"Oct",
						"Nov",
						"Dec"
					]
				},
				title: {
					text: "Spendings",
					align: "left",
					style: {
						fontSize: "16px",
						color: "#666"
					}
                },
			}
		};
	}

	render() {
		return (
			<div id="wrapper">
				<div id="chart-area" className={cards.spendingsCharCart}>
					<ReactApexChart
						options={this.state.options}
						series={this.state.series}
						type="line"
						height={250}
					/>
				</div>
			</div>
		);
	}
}

export default YearChart;
