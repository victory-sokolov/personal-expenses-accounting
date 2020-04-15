import React, { Component } from 'react';
import cards from './cards.scss';
import recieptIcon from './icons/receipt-solid.svg';
import tagIcon from './icons/tags-solid.svg';
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
						<p>32</p>
					</div>
					<img src={recieptIcon} className={cards.receiptIcon} alt="" />
				</div>
			</div>
		);
	}
}

export default SmallCard;