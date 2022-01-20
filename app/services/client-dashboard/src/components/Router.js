import { BrowserRouter, Route, Switch } from "react-router-dom";
import Dashboard from "./Dashboard/Dashboard";
import LoginFormContainer from "./Login/LoginFormContainer";
import PageNotFound from './PageNotFound';
import RegistrationPageContainer from "./Registration/RegistrationPageContainer";

const Router = () => (
	<BrowserRouter>
		<Switch>
			<Route exact path="/" component={LoginFormContainer} />
			<Route path="/login" component={LoginFormContainer} />
			<Route path="/register" component={RegistrationPageContainer} />
			<Route path="/dashboard" component={Dashboard} />
			<Route path="/logout" component={LoginFormContainer} />
			<Route component={PageNotFound} />
		</Switch>
	</BrowserRouter>
);

export default Router;
