import React, { Component } from "react";
import Button from "react-bootstrap/Button";
import Col from "react-bootstrap/Col";
import Container from "react-bootstrap/Container";
import Modal from "react-bootstrap/Modal";
import Row from "react-bootstrap/Row";
import dashboard from "./dashboard.scss";
import DatePickerComponent from "./ui-components/DatePicker";
import FileUpload from "./ui-components/FileUpload";
import { InputContainer, InputOutline } from './ui-components/InputOutline';
import NativeSelects from './ui-components/Select';

class ModalWindow extends Component {
	constructor(props) {
		super(props);
		this.state = {
			image: null,
			imagePath: null,
			renderImageUpload: true,
			vendor: "",
			date: "",
			amount: "",
			category: "",
			warranty: "",
		};
	}

	setInputFields = () => {
		this.setState({
			vendor: this.props.inputData.vendor,
			date: this.props.inputData.date,
			amount: this.props.inputData.amount,
			category: this.props.inputData.category,
			warranty: this.props.inputData.warranty,
		});
	}

	resetInputFields = () => {
		this.setState({
			vendor: "",
			date: "",
			amount: "",
			category: "",
			warranty: "",
		});
	}

	onImagePreview = (e) => {
		e.preventDefault();
		let file = event.target.files[0];
		this.setState({ image: file });
		if (file != null) {
			let image = URL.createObjectURL(file);
			this.imagePreviewHandler(image);
		}
	};

	// Discard image preview when modal is closed
	imagePreviewHandler(image) {
		this.setState((prevState) => ({
			renderImageUpload: !prevState.renderImageUpload,
			imagePath: image,
		}));
	}

	onChangeHandler = () => {
		this.setState({
			[event.target.name]: event.target.value,
		});
	};

	render() {
		return (
			<div>
				<Modal
					show={this.props.show}
					onHide={this.props.handleClose}
					size="lg"
					centered
				>
					<Modal.Header closeButton>
						<Modal.Title>Add Expense</Modal.Title>
					</Modal.Header>
					<Modal.Body>
						<Container>
							<form method="POST" onSubmit={this.props.handleFormUpload}>
								<Row>
									<Col xs={12} md={6}>
										<InputOutline
											label="Vendor"
											type="text"
											id="vendor"
											onChange={this.onChangeHandler}
											value={this.state.vendor}
										/>
										<InputContainer>
											<DatePickerComponent />
										</InputContainer>
										<InputOutline
											label="Amount"
											type="text"
											id="amount"
											onChange={this.onChangeHandler}
											value={this.amount}
										/>
										<InputContainer>
											<NativeSelects />
										</InputContainer>
										<InputOutline
											label="Warranty"
											type="text"
											id="warranty"
											onChange={this.onChangeHandler}
											value={this.warranty}
										/>
									</Col>
									<Col xs={12} md={6} className={dashboard.verticalCenterd}>
										{this.state.renderImageUpload ? (
											<FileUpload onChange={this.onImagePreview} />
										) : (
											<img src={this.state.imagePath} alt="Cash receipt" />
										)}
									</Col>
								</Row>
							</form>
						</Container>
					</Modal.Body>
					<Modal.Footer>
						<Button variant="secondary" onClick={this.props.handleClose}>
							Close
						</Button>
						<Button variant="primary" onClick={this.props.handleClose}>
							Save
						</Button>
						{this.props.children}
					</Modal.Footer>
				</Modal>
			</div>
		);
	}
}

export default ModalWindow;
