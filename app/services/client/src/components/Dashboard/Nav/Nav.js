import React, { Component } from 'react';
import { Link } from "react-router-dom";
import nav from "./side-nav.scss";
class Nav extends Component {

	constructor(props) {
		super(props);
	}

    render() {
		let dataName = this.props.userData.name;
		const name = dataName.charAt(0).toUpperCase() + dataName.slice(1);
        return (
					<nav className={nav.menu} tabIndex="0">
						<div className="smartphone-menu-trigger"></div>
						<header className={nav.avatar}>
							<img src={this.props.userData.avatar} />
							<h3>{name}</h3>
						</header>
						<ul>
							<li tabIndex="0" className={nav.receiptIcon}>
								<Link to="#">Expenses</Link>
							</li>
							<li tabIndex="0" className={nav.exportIcon}>
								<Link to="#">Reports</Link>
							</li>
							<li tabIndex="0" className={nav.cogIcon}>
								<Link to="#">Settings</Link>
							</li>
							<li tabIndex="0" className={nav.logoutIcon}>
								<Link to="/logout">Log out</Link>
							</li>
						</ul>
					</nav>
				);
    }
}

export default Nav;