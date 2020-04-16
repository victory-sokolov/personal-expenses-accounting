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
			setShow: false
		};
	}

	handleClose = () => this.setState({ show: false });
	handleShow = () => this.setState({ show: true });

	render() {
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
							<Row>
								<Col xs={12} md={5}>
									<InputOutline label="Vendor" type="text" id="vendor" />
									<InputContainer>
										<DatePickerComponent />
									</InputContainer>
									<InputOutline label="Amount" type="text" id="amount" />
									<InputOutline label="Category" type="text" id="category" />
									<InputOutline label="Warranty" type="text" id="warranty" />
									<NativeSelects/>
								</Col>
								<Col xs={12} md={7}>
									<FileUpload />
								</Col>
							</Row>
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
