import MyContext from 'components/globalContext';
import React, { useContext, useState } from 'react';
import Button from 'react-bootstrap/Button';
import Col from 'react-bootstrap/Col';
import Container from 'react-bootstrap/Container';
import Modal from 'react-bootstrap/Modal';
import Row from 'react-bootstrap/Row';
import dashboard from './dashboard.module.scss';
import FileUpload from './ui-components/FileUpload';
import { InputContainer, InputOutline } from './ui-components/InputOutline';
import NativeSelects from './ui-components/Select';

export default function ModalWindow(props: any) {

	const ReceiptFormState = {
		id: '',
		image: '',
		imagePath: '',
		renderImageUpload: true,
		vendor: '',
		date: '',
		amount: '',
		category: '',
		warranty: '',
	};

	const [
		{
			id,
			image,
			imagePath,
			renderImageUpload,
			vendor,
			date,
			amount,
			category,
			warranty,
		},
		setState,
	] = useState(ReceiptFormState);

	const [open, setOpen] = useContext(MyContext);

	const resetInputFields = () => {
		setState({ ...ReceiptFormState });
	};

	const onImagePreview = (e: any) => {
		e.preventDefault();
		const file: string = e.target.files[0];
		setState((prevState) => ({ ...prevState, [image]: file }));
		if (file != null) {
			const image = URL.createObjectURL(file);
			imagePreviewHandler(image);
		}
	};

	// Discard image preview when modal is closed
	const imagePreviewHandler = (image: string) => {
		setState((prevState) => ({
			...prevState,
			// [renderImageUpload]: !prevState.renderImageUpload,
			[imagePath]: image,
		}));
	};

	const onInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
		const { name, value } = e.target;
		setState((prevState) => ({ ...prevState, [name]: value }));
	};

	const submitForm = (e: React.ChangeEvent<HTMLFormElement>) => {
		e.preventDefault();
	};

	const saveHandler = async () => {
		const receipt = {
			id,
			vendor,
			amount,
			warranty,
			date,
			category,
		};

		props.postData(
			`${process.env.REACT_APP_RECOGNITION_API}/receipt/${id}`,
			'POST',
			receipt
		);
		closeModalWindow();
	};

	const closeModalWindow = () => {
		setOpen(false);
		resetInputFields();
	};

	return (
		<Modal show={open} onHide={closeModalWindow} size="lg" centered>
			<Modal.Header closeButton>
				<Modal.Title>Add Expense</Modal.Title>
			</Modal.Header>
			<Modal.Body>
				<Container>
					<form method="POST" onSubmit={submitForm}>
						<Row>
							<Col xs={12} md={6}>
								<InputOutline
									label="Vendor"
									type="text"
									id="vendor"
									onChange={onInputChange}
									value={vendor}
								/>
								<InputContainer>
									{/* <DatePickerComponent date={date} /> */}
								</InputContainer>
								<InputOutline
									label="Amount"
									type="text"
									id="amount"
									onChange={onInputChange}
									value={amount}
								/>
								<InputContainer>
									<NativeSelects onChange={onInputChange} />
								</InputContainer>
								<InputOutline
									label="Warranty"
									type="text"
									id="warranty"
									onChange={onInputChange}
									value={warranty}
								/>
							</Col>
							<Col xs={12} md={6} className={dashboard.verticalCenterd}>
								{renderImageUpload ? (
									<FileUpload onChange={onImagePreview} />
								) : (
									<img src={imagePath} alt="Cash receipt" />
								)}
							</Col>
						</Row>
					</form>
				</Container>
			</Modal.Body>
			<Modal.Footer>
				<Button variant="secondary" onClick={closeModalWindow}>
					Close
				</Button>
				<Button variant="primary" onClick={saveHandler}>
					Save
				</Button>
				{/* {this.props.children} */}
			</Modal.Footer>
		</Modal>
	);
}
