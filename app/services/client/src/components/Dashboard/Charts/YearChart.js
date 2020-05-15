import React, { Component } from "react";
import ReactApexChart from "react-apexcharts";
import cards from "../Cards/cards.scss";

class YearChart extends Component {
	constructor(props) {
		super(props);

		this.state = {
			receiptData: {},
			months: [
				"January",
				"February",
				"March",
				"April",
				"May",
				"June",
				"July",
				"August",
				"September",
				"October",
				"November",
				"December",
			],
			series: [
				{
					name: "Expenses &euro;",
					data: [],
				},
			],
			options: {
				chart: {
					type: "line",
					height: 250,
				},
				markers: {
					size: 6,
					colors: ["#FFA41B"],
					strokeColors: "#fff",
					strokeWidth: 2,
					hover: {
						size: 7,
					},
				},
				stroke: {
					width: 4,
					curve: "smooth",
				},
				yaxis: {
					labels: {
						minWidth: 40,
					},
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
						"Dec",
					],
				},
				title: {
					text: "Spendings",
					align: "left",
					style: {
						fontSize: "16px",
						color: "#666",
					},
				},
			},
		};
	}

	componentDidMount = () => {
		const id = localStorage.getItem("id");
		this.receiptAggregatedData(id);
	};

	receiptAggregatedData = async (id) => {
		await fetch(`/receipt/${id}`, {
			method: "GET",
			cache: "no-cache",
			headers: {
				"Content-Type": "application/json",
			},
		})
			.then((response) => response.json())
			.then((data) => {
				this.setState({ receiptData: data, isLoading: false }, () => this.yearlySpendings(data));
			})
			.catch((error) => {
				console.error("Error:", error);
			});
	};

	yearlySpendings = (receiptData) => {
		let totalSumForMonth = [];
		let receipts = receiptData.yearly;
		this.state.months.map((value) => {
			let sum = receipts[value].reduce((curr, prev) => curr + prev, 0);
			totalSumForMonth.push(sum);
		});
		let monthData = {...this.state.series}[0];
		monthData.data = [...totalSumForMonth];
		this.setState({monthData});
	};

	render() {
		const dat = [
			{
				name: "Expenses &euro;",
				data: this.state.series[0].data,
			}
		];
		return (
			<div id="wrapper">
				<div id="chart-area" className={cards.spendingsCharCart}>
					<ReactApexChart
						options={this.state.options}
						series={dat}
						type="line"
						height={250}
					/>
				</div>
			</div>
		);
	}
}

export default YearChart;
