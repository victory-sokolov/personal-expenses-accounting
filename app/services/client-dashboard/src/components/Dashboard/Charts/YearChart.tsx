import React, { Component } from 'react';
import ReactApexChart from 'react-apexcharts';
import cards from '../Cards/cards.module.scss';

interface Chart {
	receiptData: any;
	months: any;
	series: any;
	options: any;
}

export default class YearChart extends Component<{}, Chart> {
	constructor(props: any) {
		super(props);

		this.state = {
			receiptData: {},
			months: [
				'January',
				'February',
				'March',
				'April',
				'May',
				'June',
				'July',
				'August',
				'September',
				'October',
				'November',
				'December',
			],
			series: [
				{
					name: 'Expenses &euro;',
					data: [],
				},
			],
			options: {
				chart: {
					type: 'line',
					height: 250,
				},
				markers: {
					size: 6,
					colors: ['#FFA41B'],
					strokeColors: '#fff',
					strokeWidth: 2,
					hover: {
						size: 7,
					},
				},
				stroke: {
					width: 4,
					curve: 'smooth',
				},
				yaxis: {
					labels: {
						minWidth: 40,
					},
				},
				xaxis: {
					type: 'text',
					categories: [
						'Jan',
						'Feb',
						'Mar',
						'Apr',
						'May',
						'Jun',
						'Jul',
						'Aug',
						'Sep',
						'Oct',
						'Nov',
						'Dec',
					],
				},
				title: {
					text: 'Spendings',
					align: 'left',
					style: {
						fontSize: '16px',
						color: '#666',
					},
				},
			},
		};
	}

	componentDidMount = () => {
		const id = Number(localStorage.getItem('id'));
		this.receiptAggregatedData(id);
	};

	receiptAggregatedData = async (id: number) => {
		await fetch(`${process.env.REACT_APP_SERVER}/receipt/${id}`, {
			method: 'GET',
			cache: 'no-cache',
			headers: {
				'Content-Type': 'application/json',
			},
		})
			.then((response) => response.json())
			.then((data) => {
				this.setState({ receiptData: data }, () => this.yearlySpendings(data));
			})
			.catch((error) => {
				console.error('Error:', error);
			});
	};

	yearlySpendings = (receiptData: any) => {
		let totalSumForMonth: any = [];
		let receipts = receiptData.yearly;
		this.state.months.map((value: any) => {
			let sum = receipts[value].reduce(
				(curr: number, prev: number) => curr + prev,
				0
			);
			totalSumForMonth.push(sum.toFixed(2));
		});
		let monthData = { ...this.state.series }[0];
		monthData.data = [...totalSumForMonth];
		// this.setState({ monthData });
	};

	render() {
		const dat = [
			{
				name: 'Expenses &euro;',
				data: this.state.series[0].data,
			},
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
