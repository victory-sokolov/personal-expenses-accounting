import React, { Component } from 'react';
import pcIcon from "../../../public/images/Business_SVG.svg";
import Main from "../App.scss";
import Alert from '../Dashboard/ui-components/Alert';
import RegistrationForm from './RegistrationForm';
class RegistrationFormContainer extends Component {
	constructor(props) {
		super(props);
		this.state = {
			name: "",
			email: "",
			password: "",
			repeatPassword: "",
			errors: ""
		};
	}

	handleInputChange = (event) => {
		this.setState({
			[event.target.name]: event.target.value,
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
		}).then((response) =>
			response
				.json()
				.then((data) => ({ status: response.status, body: data.status }))
				.then((res) => {
					if (res.status == 200) {
						this.props.history.push("/dashboard");
						return;
					}
					this.setState({ errors: res.body });
				})
		);
	};

	render() {
		return (
			<div className={Main.flexWrapper}>
				<div className={Main.imageBlock}>
					<img src={pcIcon} alt="Login Page" />
				</div>
				<div className={Main.formCard}>
					<h1>
						<span className={Main.underline}>Create new account</span>
					</h1>
					<RegistrationForm
						handleInputChange={this.handleInputChange}
						handleSubmit={this.handleSubmit}
						name={this.state.name}
						email={this.state.email}
						password={this.state.password}
						repeatPassword={this.state.repeatPassword}
					/>
					{(this.state.errors !== "") ? (
						<Alert variant="danger" message={this.state.errors} show={true} />
					) : ''}
				</div>
			</div>
		);
	}
}

export default RegistrationFormContainer;