import { Link } from 'react-router-dom';
import nav from './side-nav.module.scss';

export default function Nav({ userData }: any) {
	const dataName = userData?.name;
	const name = dataName
		? dataName.charAt(0).toUpperCase() + dataName.slice(1)
		: '';

	return (
		<nav className={nav.menu}>
			<div className="smartphone-menu-trigger"></div>
			<header className={nav.avatar}>
				<img src={userData?.avatar} />
				<h3>{name}</h3>
			</header>
			<ul>
				<li className={nav.receiptIcon}>
					<Link to="#">Expenses</Link>
				</li>
				<li className={nav.exportIcon}>
					<Link to="#">Reports</Link>
				</li>
				<li className={nav.cogIcon}>
					<Link to="#">Settings</Link>
				</li>
				<li className={nav.logoutIcon}>
					<Link to="/logout">Log out</Link>
				</li>
			</ul>
		</nav>
	);
}
