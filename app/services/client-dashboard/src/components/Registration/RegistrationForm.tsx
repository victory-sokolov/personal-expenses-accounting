import React, { useState } from 'react';
import { useHistory } from 'react-router';
import useInput from '../../hooks/useInput';
import buttonStyle from '../ui-elements/button.module.scss';
import inputStyle from '../ui-elements/input.module.scss';

function RegistrationForm() {
	const history = useHistory();

	const [name, setName] = useInput('');
	const [email, setEmail] = useInput('');
	const [password, setPassword] = useInput('');
	const [repeatPassword, setRepeatPassword] = useInput('');
	const [error, setError] = useState('');

	const submitForm = async (e: React.ChangeEvent<HTMLFormElement>) => {
		e.preventDefault();

		const data = { name, email, password, repeatPassword };
		console.log(data);

		await fetch(`${process.env.REACT_APP_SERVER}/register`, {
			method: 'POST',
			cache: 'no-cache',
			headers: {
				'Content-Type': 'application/json',
			},
			mode: 'cors',
			body: JSON.stringify(data),
		}).then((response) =>
			response
				.json()
				.then((data) => ({ status: response.status, body: data.status }))
				.then((res) => {
					if (res.status == 200) {
						history.push('/dashboard');
						return;
					}
					setError(res.body);
				})
		);
	};

	return (
		<form method="POST" onSubmit={submitForm}>
			<div className={inputStyle.inputContainer}>
				<input
					type="text"
					id="name"
					name="name"
					required
					className={inputStyle.input}
					value={name}
					onChange={setName}
				/>
				<label htmlFor="name"> Name</label>
				<div className={inputStyle.bar} />
			</div>
			<div className={inputStyle.inputContainer}>
				<input
					type="text"
					id="email"
					name="email"
					required
					className={inputStyle.input}
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
					name="password"
					required
					className={inputStyle.input}
					value={password}
					onChange={setPassword}
				/>
				<label htmlFor="password">Password</label>
				<div className={inputStyle.bar} />
			</div>
			<div className={inputStyle.inputContainer}>
				<input
					type="password"
					id="repeat-password"
					name="repeatPassword"
					required
					className={inputStyle.input}
					value={repeatPassword}
					onChange={setRepeatPassword}
				/>
				<label htmlFor="repeat-password">Repeat Password</label>
				<div className={inputStyle.bar} />
			</div>
			<button className={buttonStyle.button}>Create Account</button>
		</form>
	);
}

export default RegistrationForm;
