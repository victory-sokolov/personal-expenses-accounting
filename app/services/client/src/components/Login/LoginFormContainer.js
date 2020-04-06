import React, { Component } from 'react';
import LoginForm from './LoginForm';
import Welcome from './Welcome';

class LoginFormContainer extends Component {
	constructor(props) {
		super(props);
		this.state = {
			email: "",
			password: "",
		};
	}

	handleInputChange(event) {
		this.setState({
			[event.target.name]: event.target.value,
		});
	}

	handleSubmit = async (event) => {
		event.preventDefault();
		await fetch("/register", {
			method: "POST",
			redirect: "follow",
			cache: "no-cache",
			headers: {
				"Content-Type": "application/json",
			},
			body: JSON.stringify(this.state),
		}).then((response) => {
			if (response.status == 200) {
				// redirect to dashboard
				//this.props.history.push("/dashboard");
			}
		});
	};

	render() {
		return (
			<div className="form-card">
				<Welcome />
				<LoginForm email={this.state.email} password={this.state.password}/>
			</div>
		);
	}
}

export default LoginFormContainer;