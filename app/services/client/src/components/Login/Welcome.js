import React, { Component } from 'react';
import Main from '../App.scss';

class Welcome extends Component {
    render() {
        return (
					<div className={Main.welcome}>
						<h1>
							<span className={Main.underline}>
								Keep all expenses <br />
								in one place
							</span>
						</h1>
						<h2>Welcome back</h2>
					</div>
				);
    }
}

export default Welcome;