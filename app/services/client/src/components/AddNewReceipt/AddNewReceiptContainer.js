import React, { Component } from 'react';

class AddNewReceiptContainer extends Component {
	constructor(props) {
		super(props);

		this.state = {
			imageURL: ""
		};

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
			<form method="POST" onSubmit={this.handleImageUpload}>
				<div className="form-group">
					<input
						type="text"
						ref={(ref) => { this.fileName = ref; }}
						className="form-control"
						name="vendor"
						placeholder="Vendor"
					/>
				</div>
				<div className="form-group">
					<input
						ref={ref => {
							this.uploadInput = ref;
						}}
						type="file"
						className="form-control btn btn-primary"
					></input>
				</div>
				<div className="form-group">
					<button className="btn btn-success">Submit</button>
				</div>
			</form>
		);
	}
}

export default AddNewReceiptContainer;