import MyContext from 'components/globalContext';
import { useContext } from 'react';
import Dropdown from 'react-bootstrap/Dropdown';
import DropdownButton from 'react-bootstrap/DropdownButton';
import button from '../../ui-elements/button.module.scss';
import dashboard from '../dashboard.module.scss';

export default function AddNewReceipt(props: any) {
	console.log('AddNewReceipt', props);

	const [open, setOpen] = useContext(MyContext);

	return (
		<div className={dashboard.buttonContainer}>
			{/* <Toast /> */}
			<DropdownButton id="dropdown-basic-button" title="New Expense">
				<Dropdown.Item onClick={() => setOpen(true)}>
					Create Manually
				</Dropdown.Item>
				<input
					type="file"
					name="upload"
					className={button.uploadButton}
					ref={(input) => (props.inputFileRef.current = input)}
					onChange={props.onImageHandler}
				/>
				<Dropdown.Item
					onClick={props.uploadInputHandler}
					title="Recognize Receipt"
				>
					Recognize Receipt
				</Dropdown.Item>
			</DropdownButton>
		</div>
	);
}
