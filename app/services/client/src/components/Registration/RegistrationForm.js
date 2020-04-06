import React, { Component } from 'react';

class RegistrationForm extends Component {

    constructor(props) {
        super(props);
    }

    render() {
        const { name, email, password} = this.props;

        return (
            <form method="POST" onSubmit={this.props.handleSubmit}>
                <div className="input-container">
                    <input
                        type="text"
                        id="#{label}"
                        required="required"
                        placeholder="Name"
                        value={name}
                        onChange={this.props.handleInputChange}
                    />
                    <label htmlFor="#{label}">Name</label>
                    <div className="bar"></div>
                </div>
                <div className="input-container">
                    <input
                        type="email"
                        id="#{label}"
                        required="required"
                        placeholder="Email"
                        value={email}
                        onChange={this.props.handleInputChange}
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
                        onChange={this.props.handleInputChange}
                    />
                    <label htmlFor="#{label}">Password</label>
                    <div className="bar"></div>
                </div>
                <div className="input-container">
                    <input
                        type="password"
                        id="#{label}"
                        required="required"
                        placeholder="Password"
                        value={password}
                        onChange={this.props.handleInputChange}
                    />
                    <label htmlFor="#{label}">Repeat Password</label>
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