import React, { Component } from 'react';
import RegistrationForm from './RegistrationForm';

class RegistrationFormContainer extends Component {
	constructor() {
		super();
		this.state = {
			name: '',
			email: '',
			password: ''
		};
	}

	handleInputChange = (event) => {
		this.setState({
			[event.target.name]: event.target.value
		});
	};

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
			<div>
				<RegistrationForm
					handleInputChange={this.handleInputChange}
					handleSubmit={this.handleSubmit}
					name={this.state.name}
					email={this.state.email}
					password={this.state.password}
				/>
			</div>
		);
	}
}

export default RegistrationFormContainer;