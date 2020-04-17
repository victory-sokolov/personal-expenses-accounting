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
			show: false,
			setShow: false,
		};
	}


	handleClose = () => {
		this.setState({ show: false});
		this.props.componentMount();
	}
	handleShow = () => this.setState({ show: true });
	render() {
		const { imagePath, renderImageUpload } = this.props.receiptData;
		return (
			<>
				<div className={dashboard.buttonContainer} onClick={this.handleShow}>
					<button>New Expense</button>
				</div>

				<Modal
					show={this.state.show}
					onHide={this.handleClose}
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
											onChange={this.props.onChangeHandler}
										/>
										<InputContainer>
											<DatePickerComponent />
										</InputContainer>
										<InputOutline
											label="Amount"
											type="text"
											id="amount"
											onChange={this.props.onChangeHandler}
										/>
										<InputContainer>
											<NativeSelects />
										</InputContainer>
										<InputOutline
											label="Warranty"
											type="text"
											id="warranty"
											onChange={this.props.onChangeHandler}
										/>
									</Col>
									<Col xs={12} md={6} className={dashboard.verticalCenterd}>
										{renderImageUpload ? (
											<FileUpload onChange={this.props.onImageHandler} />
										) : (
											<img src={imagePath} alt="" />
										)}
									</Col>
								</Row>
							</form>
						</Container>
					</Modal.Body>
					<Modal.Footer>
						<Button variant="secondary" onClick={this.handleClose}>
							Close
						</Button>
						<Button variant="primary" onClick={this.handleClose}>
							Save
						</Button>
					</Modal.Footer>
				</Modal>
			</>
		);
	}
}

export default ModalWindow;
