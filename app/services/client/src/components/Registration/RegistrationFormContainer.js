import React, { Component } from 'react';
import RegistrationForm from './RegistrationForm';

class RegistrationFormContainer extends Component {
	constructor(props) {
        super(props);
        this.state = {
            name: "",
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
			<div>
				<RegistrationForm
					handleInputChange={this.handleInputChange}
					handleSubmit={this.handleSubmit}
					name={this.props.name}
					email={this.props.email}
					password={this.props.password}
				/>
			</div>
		);
	}
}

export default RegistrationFormContainer;