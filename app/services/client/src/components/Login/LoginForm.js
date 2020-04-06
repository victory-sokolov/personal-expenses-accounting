import React, { Component } from 'react';

class LoginForm extends Component {

	constructor(props) {
		super(props);
	}

    render() {
		const {email, password} = this.props;

        return (
			<form method="POST">
				<div className="input-container">
					<input
						type="email"
						id="#{label}"
						required="required"
						placeholder="Email"
						value={email}
					/>
					<label htmlFor="#{label}">Email</label>
					<div className="bar"></div>
				</div>
				<div className="input-container">
					<input
						type="password"
						id="#{label}"
						required="required"
						placeholder="Password"
						value={password}
					/>
					<label htmlFor="#{label}">Password</label>
					<div className="bar"></div>
				</div>
				<div className="login-block">
					<input type="checkbox" id="remember" />
					<label htmlFor="remember">Remember me</label>
					<a href="#">Forgot password?</a>
				</div>
				<div className="button-container">
					<button>Login</button>
				</div>
				<div className="footer">
					<p>
						Don’t have an account?
						<a href="#">Click here</a>
					</p>
				</div>
			</form>
		);
    }
}

export default LoginForm;