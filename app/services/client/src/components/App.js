import React, { Component } from "react";
import Main from './App.scss';
import LoginPageContainer from "./Login/LoginPageContainer";

class App extends Component {
	render() {
		return (
			<div className={Main.container}>
				<LoginPageContainer />
			</div>
		);
	}
}

export default App;
