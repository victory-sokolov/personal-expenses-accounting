import React, { Component } from 'react';

class LoginForm extends Component {

	constructor(props) {
		super(props);
	}

    render() {
		const {email, password} = this.props;

        return (
			<form method="POST" onSubmit={this.props.handleSubmit}>
				<div className="input-container">
					<label htmlFor="email">Email</label>
					<input
						type="email"
						id="email"
						name="email"
						required="required"
						placeholder="Email"
						autoComplete="off"
						value={email.value}
						onChange={this.props.handleInputChange}
					/>
					<div className="bar"></div>
				</div>
				<div className="input-container">
					<label htmlFor="password">Password</label>
					<input
						type="password"
						id="password"
						name="password"
						required="required"
						placeholder="Password"
						autoComplete="off"
						value={password.value}
						onChange={this.props.handleInputChange}
					/>

					<div className="bar"></div>
				</div>
				<div className="login-block">
					<input type="checkbox" id="remember" name="remember" />
					<label htmlFor="remember">Remember me</label>
					<a href="#">Forgot password?</a>
				</div>
				<div className="button-container">
					<input type="submit" value="Login" name="submit" />
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