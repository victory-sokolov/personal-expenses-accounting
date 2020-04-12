import React, { Component } from 'react';
import nav from './side-nav.scss';


class Nav extends Component {
    render() {
        return (
			<nav className={nav.menu} tabIndex="0">
				<div className="smartphone-menu-trigger"></div>
				<header className={nav.avatar}>
					<img src="https://s3.amazonaws.com/uifaces/faces/twitter/kolage/128.jpg" />
					<h2>John D.</h2>
				</header>
				<ul>
					<li tabIndex="0" className={nav.receiptIcon}>
						<a href="#">Expenses</a>
					</li>
					<li tabIndex="0" className={nav.exportIcon}>
						<a href="#">Reports</a>
					</li>
					<li tabIndex="0" className={nav.cogIcon}>
						<a href="#">Settings</a>
					</li>
					<li tabIndex="0" className={nav.logoutIcon}>
						<a href="#">Log out</a>
					</li>
				</ul>
			</nav>
		);
    }
}

export default Nav;