import React, { Component } from 'react';
import { Link } from "react-router-dom";
import buttonStyle from "../ui-elements/button.scss";
import inputStyle from '../ui-elements/input.scss';
import login from '../ui-elements/login.scss';
class LoginForm extends Component {

	constructor(props) {
		super(props);
	}

    render() {
		const {email, password} = this.props;

        return (
			<form method="POST" onSubmit={this.props.handleSubmit}>
				<div className={inputStyle.inputContainer}>
					<input
						type="text"
						id="email"
						className={inputStyle.input}
						name="email"
						required="required"
						autoComplete="off"
						value={email.value}
						onChange={this.props.handleInputChange}
					/>
					<label htmlFor="email">Email</label>
					<div className={inputStyle.bar}></div>
				</div>
				<div className={inputStyle.inputContainer}>
					<input
						type="password"
						id="password"
						className={inputStyle.input}
						name="password"
						required="required"
						autoComplete="off"
						value={password.value}
						onChange={this.props.handleInputChange}
					/>
					<label htmlFor="password">Password</label>
					<div className={inputStyle.bar}></div>
				</div>
				<div className={login.loginBlock}>
					<div className={login.rememberMeBlock}>
						<input type="checkbox" id="remember" name="remember" />
						<label htmlFor="remember">Remember me</label>
					</div>
					<a href="#">Forgot password?</a>
				</div>
				<button className={buttonStyle.button}>Login</button>
				<div className={login.loginFooter}>
					<p>
						Don’t have an account?
						<Link to="/register" className="nav-link">
							Click here
						</Link>
					</p>
				</div>
			</form>
		);
    }
}

export default LoginForm;