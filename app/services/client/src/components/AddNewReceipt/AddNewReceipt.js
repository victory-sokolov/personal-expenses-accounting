import React, { Component } from 'react';

class AddNewReceipt extends Component {

    constructor(props) {
		super(props);
	}

	render() {
		return (
			<form onSubmit={this.props.handleImageUpload}>
				<div className="form-group">
					<input
						type="text"
						className="form-control"
						name="vendorm"
						placeholder="Vendor"
					/>
				</div>
				<div className="input-group mb-3">
					<select
						defaultValue={"Category"}
						className="custom-select"
						id="inputGroupSelect01"
					>
						<option value="Category">Category</option>
						<option value="1">One</option>
						<option value="2">Two</option>
						<option value="3">Three</option>
					</select>
				</div>
				<div className="form-group">
					<input
						ref={ref => {
							this.uploadInput = ref;
						}}
						type="file"
						className="form-control btn btn-primary"
					/>
				</div>
				<div className="form-group">
					<input
						type="submit"
						className="btn btn-success"
						name="save"
						value="Save"
					/>
				</div>
			</form>
		);
	}
}

export default AddNewReceipt;