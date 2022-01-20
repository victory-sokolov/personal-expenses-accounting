import MyContext from 'components/globalContext';
import { useContext } from 'react';
import AddNewReceiptContainer from './AddNewReceipt/AddNewReceiptContainer';
import dashboard from './dashboard.module.scss';

export default function Header(props: any) {
	const [open, setOpen] = useContext(MyContext);

	return (
		<div className={dashboard.heading}>
			<h1>Expenses</h1>
			<div className={dashboard.divider}></div>
			<div className={dashboard.filterandexpens}>
				<AddNewReceiptContainer
					showModal={open}
					// imagePreviewHandler={props.imagePreviewHandler}
					imagePreview={props.imagePreview}
				/>
			</div>
			<div className={dashboard.divider}></div>
		</div>
	);
}
