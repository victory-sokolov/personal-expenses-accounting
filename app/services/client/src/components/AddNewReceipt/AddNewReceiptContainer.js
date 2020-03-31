import React, { Component } from 'react';
import AddNewReceipt from './AddNewReceipt';

class AddNewReceiptContainer extends Component {
	constructor(props) {
		super(props);
		this.state = {
			fileInput: ''
		};
		this.handleImageUpload = this.handleImageUpload.bind(this);
		this.onChangeHandler = this.onChangeHandler.bind(this);
	}

	onChangeHandler() {
		let file = event.target.files[0];
		this.setState({
			fileInput: file
		});
	}

	handleImageUpload(e) {
		e.preventDefault();

		const data = new FormData();
		data.append("file", this.state.fileInput);
		fetch("http://localhost:5000/addreceipt", {
			method: "POST",
			body: data
		});
	}

	render() {
		return (
			<div className="container">
				<AddNewReceipt
					handleImageUpload={this.handleImageUpload}
					onChangeHandler={this.onChangeHandler}
				/>
			</div>
		);
	}
}

export default AddNewReceiptContainer;