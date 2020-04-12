import React, { Component } from 'react';
import cards from './cards.scss';
import recieptIcon from './icons/receipt-solid.svg';
import graphIcon from './icons/today_graph.svg';

class SmallCard extends Component {
	render() {
		return (
			<div className={cards.container}>
				<div className={cards.smallCards}>
					<div className={cards.title}>
						<p>Monthly Spendings</p>
						<p>900 $</p>
					</div>
					<img src={graphIcon} alt="" />
				</div>
				<div className={cards.smallCards}>
					<div className={cards.title}>
						<p>Yearly Spendings</p>
						<p>23000 $</p>
					</div>
					<img src={graphIcon} className={cards.graphIcon} alt="" />
				</div>
				<div className={cards.smallCards}>
					<p>Frequently Used Category</p>
					<p>Grocerry</p>
				</div>
				<div className={cards.smallCards}>
					<p>
						Amount Of <br /> Receipts / Month
					</p>
					<p>32</p>
					<img src={recieptIcon} className={cards.receiptIcon} alt="" />
				</div>
			</div>
		);
	}
}

export default SmallCard;