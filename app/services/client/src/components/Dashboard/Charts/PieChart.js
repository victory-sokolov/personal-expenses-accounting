import cx from "classnames";
import React, { Component } from "react";
import ReactApexChart from "react-apexcharts";
import { countBy } from "../../../utils/helpers";
import cards from "../Cards/cards.scss";
class PieChart extends Component {
	constructor(props) {
		super(props);

		this.state = {
			categories: [],
			series: [],
			options: {
				chart: {
					width: 380,
					height: 250,
					type: "pie",
				},
				labels: [
						"Clothes",
						"Medicine",
						"Press subscription",
						"Books, bookstores",
						"Web stores",
						"Stomatology",
				],
				responsive: [
					{
						breakpoint: 480,
						options: {
							chart: {
								width: 200,
							},
							legend: {
								position: "bottom",
							},
						},
					},
				],
			},
		};
	}

	componentDidMount() {
		const id = localStorage.getItem("id");
		this.getCategories(id);
	}

	categoriesStat = () => {
		const cat = countBy(this.state.categories);
		const series = Object.entries(cat).map(([key, value]) => value * 10);
		this.setState({ series: series });
		const opt = this.state.options;
		opt.labels = [...Object.keys(cat)];
		this.setState({ opt });
	};

	getCategories = async (id) => {
		await fetch(`/receipt/${id}`, {
			method: "GET",
			cache: "no-cache",
			headers: {
				"Content-Type": "application/json",
			},
		})
			.then((response) => response.json())
			.then((data) => {
				this.setState({ categories: data["categories"] }, () =>
					this.categoriesStat()
				);
			})
			.catch((error) => {
				console.error("Error:", error);
			});
	};

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
