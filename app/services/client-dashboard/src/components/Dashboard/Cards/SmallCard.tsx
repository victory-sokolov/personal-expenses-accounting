import { useEffect, useState } from 'react';
import cards from './cards.module.scss';
import recieptIcon from './icons/receipt-solid.svg';
import tagIcon from './icons/tags-solid.svg';
import graphIcon from './icons/today_graph.svg';

export default function SmallCard({props}: any) {
	const [monthlySum, setMonthlySum] = useState('');
	const [yearlySum, setYearlySum] = useState('');
	const [receiptData, setReceiptData] = useState([]);

	useEffect(() => {
		const id = localStorage.getItem('id')?.toString();
		receiptAggregatedData(id);
	}, []);

	const sumSpendings = (receiptData: any) => {
		const monthName = new Date().toLocaleString('default', { month: 'long' });
		const monthlySum = receiptData.yearly[monthName].reduce(
			(curr: number, prev: number) => curr + prev,
			0
		);
		setMonthlySum(monthlySum.toFixed(2));
	};

	const yearlySpendings = (receiptData: any) => {
		let sum = 0;
		for (let key in receiptData.yearly) {
			let currentSum = receiptData.yearly[key].reduce(
				(curr: number, prev: number) => curr + prev,
				0
			);
			sum += currentSum;
		}
		setYearlySum(sum.toFixed(2));
	};

	const receiptAggregatedData = async (id: string | undefined) => {
		await fetch(`${process.env.REACT_APP_SERVER}/receipt/${id}`, {
			method: 'GET',
			cache: 'no-cache',
			headers: {
				'Content-Type': 'application/json',
			},
		})
			.then((response) => response.json())
			.then((data) => {
				setReceiptData(data);
				sumSpendings(data);
				yearlySpendings(data);
			})
			.catch((error) => {
				console.error('Error:', error);
			});
	};

	const totalReceipts = Object.keys(receiptData).length;

	return (
		<div className={cards.container}>
			<div className={cards.smallCards}>
				<div className={cards.title}>
					<p>Monthly Spendings</p>
					<p>{monthlySum} &euro;</p>
				</div>
				<img src={graphIcon} alt="" />
			</div>
			<div className={cards.smallCards}>
				<div className={cards.title}>
					<p>Yearly Spendings</p>
					<p>{yearlySum} &euro;</p>
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
