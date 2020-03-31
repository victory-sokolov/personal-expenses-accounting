import React, { Component } from 'react';

class AddNewReceipt extends Component {
	constructor(props) {
		super(props);
	}

	render() {
		return (
			<form method="POST" onSubmit={this.props.handleImageUpload}>
				<div className="form-group">
					<input
						type="text"
						ref={ref => {
							this.fileName = ref;
						}}
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

export default AddNewReceipt;