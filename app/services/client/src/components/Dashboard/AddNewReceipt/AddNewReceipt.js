import React, { Component } from 'react';
import Dropdown from "react-bootstrap/Dropdown";
import DropdownButton from "react-bootstrap/DropdownButton";
import button from "../../ui-elements/button.scss";
import dashboard from "../dashboard.scss";
// import Toast from "../ui-components/Toast";

class AddNewReceipt extends Component {
	constructor(props) {
		super(props);
	}


	render() {
		return (
			<div className={dashboard.buttonContainer}>
				{/* <Toast /> */}
				<DropdownButton id="dropdown-basic-button" title="New Expense">
					<Dropdown.Item onClick={this.props.showModal}>
						Create Manually
					</Dropdown.Item>
					<input
						type="file"
						name="upload"
						className={button.uploadButton}
						ref={(input) => (this.props.inputFileRef.current = input)}
						onChange={this.props.onImageHandler}
					/>
					<Dropdown.Item
						onClick={this.props.uploadInputHandler}
						title="Recognize Receipt"
					>
						Recognize Receipt
					</Dropdown.Item>
				</DropdownButton>
			</div>
		);
	}
}

export default AddNewReceipt;