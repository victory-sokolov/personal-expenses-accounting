import React, { Component } from 'react';
import dashboard from "../dashboard.scss";

class ReceiptSection extends Component {
	constructor(props) {
		super(props);
		this.state = {
			currentReceipt: {},
		};
	}

	getCurrentReceiptState = () => {
		return this.state.currentReceipt;
	};

	setCurrentReceiptState = () => {
		this.setState({
			currentReceipt: {}
		});
	}

	modalClick = (e) => {
		const receiptID = Number(e.target.getAttribute("receipt-id"));
		const allReceipts = this.props.receipts.receipts;
		const receipt = allReceipts.find((x) => x.id === receiptID);

		this.setState({ currentReceipt: receipt }, () => {
			this.props.showModal();
		});
	};

	render() {
		const { receipts } = this.props.receipts;
		return (
			<div className={dashboard.receiptSection}>
				<div className={dashboard.titleSection}>
					<h5>Date</h5>
					<h5>Vendor</h5>
					<h5>Amount</h5>
					<h5>Category</h5>
				</div>
				{receipts.map((receipt) => {
					const d = new Date(receipt.date);
					const date = `${d.getFullYear()}-${d.getUTCDay()}-${d.getUTCDate()}`;
					const price = receipt.price == null ? 0.0 : receipt.price;
					return (
						<div
							className={dashboard.receiptData}
							onClick={this.modalClick}
							receipt-id={receipt.id}
							key={receipt.id}
						>
							<h5>{date}</h5>
							<h5>{receipt.vendor}</h5>
							<h5>{price} &euro;</h5>
							<h5>{receipt.category}</h5>
							<img
								src={`client/public/receipts/${receipt.image}`}
								alt="receipt"
								className={dashboard.receiptImage}
							/>
						</div>
					);
				})}
			</div>
		);
	}
}

export default ReceiptSection;