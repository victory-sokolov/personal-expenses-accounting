import React from 'react';
import pcIcon from '../../assets/images/app_development_SVG.svg';
import Main from '../../App.module.scss';
import LoginForm from './LoginForm';

export default function LoginFormContainer() {
	return (
		<div className={Main.flexWrapper}>
			<div className={Main.imageBlock}>
				<img src={pcIcon} alt="" />
			</div>
			<div className={Main.formCard}>
				<div className={Main.welcome}>
					<h1>
						<span className={Main.underline}>
							Keep all expenses <br />
							in one place
						</span>
					</h1>
					<h2>Welcome back</h2>
				</div>
				<LoginForm />
				{/* {this.state.errors !== "" ? (
						<Alert variant="danger" message={this.state.errors} show={true} />
					) : (
						null
					)} */}
			</div>
		</div>
	);
}

