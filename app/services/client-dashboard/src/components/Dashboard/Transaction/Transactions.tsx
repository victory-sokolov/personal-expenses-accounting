import React from 'react';
import dashboard from '../dashboard.module.scss';

export default function Transactions(props: any) {
	const modalClick = (e: any) => {
		const receiptID = Number(e.target.getAttribute('receipt-id'));
		const allReceipts = props.receipts.receipts;
		const receipt = allReceipts.find((x: any) => x.id === receiptID);

	};

	const { response } = props?.receipts;
	return (
		<div className={dashboard.receiptSection}>
			<div className={dashboard.titleSection}>
				<h5>Date</h5>
				<h5>Vendor</h5>
				<h5>Amount</h5>
				<h5>Category</h5>
			</div>
			{response
				.slice(0)
				.reverse()
				.map((receipt: any) => {
					const d = new Date(receipt.date);
					const date = `${d.getFullYear()}-${
						d.getUTCDay() + 1
					}-${d.getUTCDate()}`;
					const price = receipt.price == '' ? 0.0 : receipt.price;
					return (
						<div
							className={dashboard.receiptData}
							onClick={modalClick}
							receipt-id={receipt.id}
							key={receipt.id}
						>
							<h5>{date}</h5>
							<h5>{receipt.vendor}</h5>
							<h5>{price} &euro;</h5>
							<h5>{receipt.category}</h5>
							<img
								src={`assets/images/receipts/${receipt.image}`}
								alt="receipt"
								className={dashboard.receiptImage}
							/>
						</div>
					);
				})}
		</div>
	);
}
