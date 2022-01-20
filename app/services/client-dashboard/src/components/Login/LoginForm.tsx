import React, { useState } from 'react';
import { Link, useHistory } from 'react-router-dom';
import useInput from '../../hooks/useInput';
import buttonStyle from '../ui-elements/button.module.scss';
import inputStyle from '../ui-elements/input.module.scss';
import login from '../ui-elements/login.module.scss';

export default function LoginForm() {
	const history = useHistory();
	const [email, setEmail] = useInput('');
	const [password, setPassword] = useInput('');
	const [data, setData] = useState({});

	const submitForm = async (e: any): Promise<void> => {
		e.preventDefault();

		try {
			const response = await fetch(`${process.env.REACT_APP_SERVER}/login`, {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json'
				},
				body: JSON.stringify({ email, password })
			});

			if (response.status === 200) {
				const data = await response.json();
				localStorage.setItem('id', data.id);
				setData(data);
				history.push('/dashboard');
			}

		} catch(err) {
			throw new Error(err);
		}
	};

	return (
		<form method="POST" onSubmit={submitForm}>
			<div className={inputStyle.inputContainer}>
				<input
					type="text"
					id="email"
					className={inputStyle.input}
					name="email"
					required
					autoComplete="off"
					value={email}
					onChange={setEmail}
				/>
				<label htmlFor="email">Email</label>
				<div className={inputStyle.bar} />
			</div>
			<div className={inputStyle.inputContainer}>
				<input
					type="password"
					id="password"
					className={inputStyle.input}
					name="password"
					required
					autoComplete="off"
					value={password}
					onChange={setPassword}
				/>
				<label htmlFor="password">Password</label>
				<div className={inputStyle.bar} />
			</div>
			<div className={login.loginBlock}>
				<div className={login.rememberMeBlock}>
					<input type="checkbox" id="remember" name="remember" />
					<label htmlFor="remember">Remember me</label>
				</div>
				<Link to="#">Forgot password?</Link>
			</div>
			<button className={buttonStyle.button}>Login</button>
			<div className={login.loginFooter}>
				<p>
					Don’t have an account?
					<Link to="/register" className="nav-link">
						Click here
					</Link>
				</p>
			</div>
		</form>
	);
}
