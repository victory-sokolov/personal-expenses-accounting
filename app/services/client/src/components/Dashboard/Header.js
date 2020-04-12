import React, { Component } from 'react';
import dashboard from "./dashboard.scss";
import ModalWindow from './ModalWindow';

class Header extends Component {
    render() {
        return (
					<div className={dashboard.heading}>
						<h1>Expenses</h1>
						<div className={dashboard.divider}></div>
						<div className={dashboard.filterandexpens}>
							<div className={dashboard.filterIcon}></div>
							<a href="#">Show filters</a>
							<ModalWindow />
						</div>

						<div className={dashboard.divider}></div>
					</div>
				);
    }
}

export default Header;