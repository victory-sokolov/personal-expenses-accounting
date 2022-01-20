import Main from '../../App.module.scss';
import pcIcon from '../../assets/images/Business_SVG.svg';
import Alert from '../Dashboard/ui-components/Alert';
import RegistrationForm from './RegistrationForm';

export default function RegistrationFormContainer()  {

	return (
		<div className={Main.flexWrapper}>
			<div className={Main.imageBlock}>
				<img src={pcIcon} alt="Login Page" />
			</div>
			<div className={Main.formCard}>
				<h1>
					<span className={Main.underline}>Create new account</span>
				</h1>
				<RegistrationForm />
				{/* {this.state.errors !== '' ? (
					<Alert variant="danger" message={this.state.errors} show={true} />
				) : (
					''
				)} */}
			</div>
		</div>
	);
}
