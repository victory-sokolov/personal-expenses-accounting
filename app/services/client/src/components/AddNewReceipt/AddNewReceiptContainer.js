import React, { Component } from 'react';

class AddNewReceiptContainer extends Component {
	constructor(props) {
		super(props);
		this.handleImageUpload = this.handleImageUpload.bind(this);
	}

	handleImageUpload(e) {
        e.preventDefault();

        const data = new FormData();
		data.append("file", this.uploadInput.files[0]);
		fetch("http://localhost:5000/addreceipt", {
			method: "POST",
			body: data
		});
	}

	render() {
		return (
			<div className="container">
				<AddNewReceiptContainer handleImageUpload={this.handleImageUpload} />
			</div>
		);
	}
}

export default AddNewReceiptContainer;