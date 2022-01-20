import Main from './App.module.scss';
import LoginFormContainer from './components/Login/LoginFormContainer';

function App() {
	return (
		<div className={Main.container}>
			<LoginFormContainer />
		</div>
	);
}

export default App;
