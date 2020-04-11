import React from "react";
import { BrowserRouter, Route, Switch } from "react-router-dom";
import App from "./App";
import Dashboard from "./Dashboard/Dashboard";
import LoginPageContainer from "./Login/LoginPageContainer";
import PageNotFound from './PageNotFound';
import RegistrationPageContainer from "./Registration/RegistrationPageContainer";

const Router = () => (
	<BrowserRouter>
		<Switch>
			<Route exact path="/" component={App} />
			<Route path="/login" component={LoginPageContainer} />
			<Route path="/register" component={RegistrationPageContainer} />
			<Route path="/dashboard" component={Dashboard} />
			<Route component={PageNotFound} />
		</Switch>
	</BrowserRouter>
);

export default Router;
