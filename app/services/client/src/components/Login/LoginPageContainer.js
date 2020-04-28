import React, { Component } from 'react';
import pcIcon from '../../../public/images/app_development_SVG.svg';
import Main from '../App.scss';
import Alert from "../Dashboard/ui-components/Alert";
import LoginForm from './LoginForm';
class LoginFormContainer extends Component {
	constructor(props) {
		super(props);
		this.state = {
			email: "",
			password: "",
			errors: "",
		};
	}

	handleInputChange = (event) => {
		this.setState({
			[event.target.name]: event.target.value,
		});
	}

	handleSubmit = async (event) => {
		event.preventDefault();
		await fetch("/login", {
			method: "POST",
			headers: {
				"Content-Type": "application/json",
			},
			body: JSON.stringify(this.state),
		}).then((response) =>
			response
				.json()
				.then((data) => ({ status: response.status, body: data }))
				.then((res) => {
					if (res.status == 200) {
						//set users id to localstorage
						localStorage.setItem("id", res.body.id);
						this.props.history.push("/dashboard");
					}
					this.setState({ errors: res.body.status});
				})
		);
	}

	render() {
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
					<LoginForm
						handleInputChange={this.handleInputChange}
						handleSubmit={this.handleSubmit}
						email={this.state.email}
						password={this.state.password}
					/>
					{this.state.errors !== "" ? (
						<Alert variant="danger" message={this.state.errors} show={true} />
					) : (
						null
					)}
				</div>
			</div>
		);
	}
}

export default LoginFormContainer;