import cx from "classnames";
import React, { Component } from "react";
import ReactApexChart from "react-apexcharts";
import cards from "../Cards/cards.scss";

class PieChart extends Component {
	constructor(props) {
		super(props);

		this.state = {
			series: [44, 55, 13, 43, 22],
			options: {
				chart: {
                    width: 380,
                    height: 250,
					type: "pie"
				},
				labels: ["Team A", "Team B", "Team C", "Team D", "Team E"],
				responsive: [
					{
						breakpoint: 480,
						options: {
							chart: {
								width: 200,
							},
							legend: {
								position: "bottom"
							}
						}
					}
				]
			}
		};
	}

	render() {
        let className = cx(cards.spendingsCharCart, cards.piecChart);
		return (
			<div id="wrapper">
				<div id="chart-area" className={className}>
                    <h3>Categories</h3>
					<ReactApexChart
						options={this.state.options}
						series={this.state.series}
						type="pie"
						width={450}
						height={222}
					/>
				</div>
			</div>
		);
	}
}

export default PieChart;
