import React, { Component } from 'react';
import Main from "./Main";
import NavContainer from "./Nav/NavContainer";
import nav from './Nav/side-nav.scss';

class Dashboard extends Component {
    render() {
        return (
			<div className={nav.container}>
				<NavContainer />
				<Main />
			</div>
		);
    }
}

export default Dashboard;