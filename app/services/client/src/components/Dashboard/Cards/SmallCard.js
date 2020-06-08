import React, { Component } from 'react';
import cards from "./cards.scss";
import recieptIcon from './icons/receipt-solid.svg';
import tagIcon from './icons/tags-solid.svg';
import graphIcon from './icons/today_graph.svg';

class SmallCard extends Component {
	constructor(props) {
		super(props);
		this.state = {
			receiptData: {},
			isLoading: true,
			monthlySum: 0,
			yearlySum: 0,
		};
	}

	componentDidMount = () => {
		const id = localStorage.getItem("id");
		this.receiptAggregatedData(id);
	};

	sumSpendings = (receiptData) => {
		const monthName = new Date().toLocaleString("default", { month: "long" });
		const monthlySum = receiptData.yearly[monthName].reduce(
			(curr, prev) => curr + prev, 0
		);
		this.setState({ monthlySum: monthlySum.toFixed(2) });
	};

	yearlySpendings = (receiptData) => {
		let sum = 0;
		for (let key in receiptData.yearly) {
			let currentSum = receiptData.yearly[key].reduce(
				(curr, prev) => curr + prev, 0
			);
			sum += currentSum;
		}
		this.setState({ yearlySum: sum.toFixed(2) });
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
				this.setState({ receiptData: data, isLoading: false });
				this.sumSpendings(data);
				this.yearlySpendings(data);
			})
			.catch((error) => {
				console.error("Error:", error);
			});
	};

	render() {
		const totalReceipts = Object.keys(this.props.receiptData).length;

		return (
			<div className={cards.container}>
				<div className={cards.smallCards}>
					<div className={cards.title}>
						<p>Monthly Spendings</p>
						<p>{this.state.monthlySum} &euro;</p>
					</div>
					<img src={graphIcon} alt="" />
				</div>
				<div className={cards.smallCards}>
					<div className={cards.title}>
						<p>Yearly Spendings</p>
						<p>{this.state.yearlySum} &euro;</p>
					</div>
					<img src={graphIcon} className={cards.graphIcon} alt="" />
				</div>
				<div className={cards.smallCards}>
					<div className={cards.title}>
						<p>Frequently Used Category</p>
						<p>Grocerry</p>
					</div>
					<img src={tagIcon} className={cards.tagIcon} alt="" />
				</div>
				<div className={cards.smallCards}>
					<div className={cards.title}>
						<p>
							Amount Of <br /> Receipts / Month
						</p>
						<p>{totalReceipts}</p>
					</div>
					<img src={recieptIcon} className={cards.receiptIcon} alt="" />
				</div>
			</div>
		);
	}
}

export default SmallCard;