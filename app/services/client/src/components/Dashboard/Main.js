import React, { Component } from 'react';
import SmallCard from './Cards/SmallCard';
import PieChart from "./Charts/PieChart";
import YearChart from './Charts/YearChart';
import Header from './Header';
import cards from './Cards/cards.scss';

class Main extends Component {
    render() {
        return (
			<main>
				<Header />
				<SmallCard />
				<div className={cards.chartsWrapper}>
					<YearChart />
					<PieChart />
				</div>
			</main>
		);
    }
}

export default Main;