import React, { Component } from 'react';

class RegistrationForm extends Component {

    constructor(props) {
        super(props);
    }

    render() {

        const { name, email, password, repeatPassword } = this.props;

        return (
			<form method="POST" onSubmit={this.props.handleSubmit}>
				<div className="input-container">
					<label htmlFor="name"> Name</label>
					<input
						type="text"
						id="name"
						name="name"
						placeholder="Name"
						value={name.value}
						onChange={this.props.handleInputChange}
					/>
					<div className="bar"></div>
				</div>
				<div className="input-container">
					<label htmlFor="email">
						Email
						<input
							type="email"
							id="email"
							name="email"
							placeholder="Email"
							value={email.value}
							onChange={this.props.handleInputChange}
						/>
					</label>
					<div className="bar"></div>
				</div>
				<div className="input-container">
					<label htmlFor="password">
						Password
						<input
							type="password"
							id="password"
							name="password"
							placeholder="Password"
							value={password.value}
							onChange={this.props.handleInputChange}
						/>
					</label>
					<div className="bar"></div>
				</div>
				<div className="input-container">
					<label htmlFor="repeat-password">
						Repeat Password
						<input
							type="password"
							id="repeat-password"
							name="repeatPassword"
							placeholder="Password"
							value={repeatPassword.value}
							onChange={this.props.handleInputChange}
						/>
					</label>
					<div className="bar"></div>
				</div>
				<div className="button-container">
					<input type="submit" value="Create account" />
				</div>
			</form>
		);
    }
}

export default RegistrationForm;