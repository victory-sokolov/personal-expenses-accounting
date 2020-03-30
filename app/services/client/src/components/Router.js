import React from "react";
import { BrowserRouter, Route, Switch } from "react-router-dom";
import App from "./App";


const Router = () => (
	<BrowserRouter>
		<Switch>
			<Route exact path="/" component={App} />
			{/* <Route path="/login" component={LoginFormContainer} />
			<Route path="/register" component={RegistrationFormContainer} />
			<Route path="/dashboard" component={DashboardContainer} />
			<Route component={PageNotFound} /> */}
		</Switch>
	</BrowserRouter>
);

export default Router;
