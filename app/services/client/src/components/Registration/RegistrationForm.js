import React, { Component } from 'react';
import buttonStyle from "../ui-elements/button.scss";
import inputStyle from "../ui-elements/input.scss";
class RegistrationForm extends Component {

    constructor(props) {
        super(props);
    }

    render() {

        const { name, email, password, repeatPassword } = this.props;

        return (
			<form method="POST" onSubmit={this.props.handleSubmit}>
				<div className={inputStyle.inputContainer}>
					<input
						type="text"
						id="name"
						name="name"
						required="required"
						className={inputStyle.input}
						value={name.value}
						onChange={this.props.handleInputChange}
					/>
					<label htmlFor="name"> Name</label>
					<div className={inputStyle.bar}></div>
				</div>
				<div className={inputStyle.inputContainer}>
					<input
						type="text"
						id="email"
						name="email"
						required="required"
						className={inputStyle.input}
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
						name="password"
						required="required"
						className={inputStyle.input}
						value={password.value}
						onChange={this.props.handleInputChange}
					/>
					<label htmlFor="password">Password</label>
					<div className={inputStyle.bar}></div>
				</div>
				<div className={inputStyle.inputContainer}>
					<input
						type="password"
						id="repeat-password"
						name="repeatPassword"
						required="required"
						className={inputStyle.input}
						value={repeatPassword.value}
						onChange={this.props.handleInputChange}
					/>
					<label htmlFor="repeat-password">Repeat Password</label>
					<div className={inputStyle.bar}></div>
				</div>
				<button className={buttonStyle.button}>Create Account</button>
			</form>
		);
    }
}

export default RegistrationForm;