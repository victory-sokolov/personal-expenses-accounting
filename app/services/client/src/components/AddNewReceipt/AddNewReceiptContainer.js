import React, { Component } from 'react';
import AddNewReceipt from './AddNewReceipt';

class AddNewReceiptContainer extends Component {
	constructor(props) {
		super(props);
		this.state = {
			fileInput: ""
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

	readFile(file) {
		return new Promise(function(resolve, reject) {
			let myReader = new FileReader();
			myReader.onloadend = function (e) {
				resolve(myReader.result);
			};
			myReader.readAsDataURL(file);
		});
	};


	handleImageUpload(e) {
		e.preventDefault();

		const image = this.state.fileInput;
		this.readFile(image).then(function(base64string) {
			const img = base64string.split(',')[1];
			fetch("http://localhost:5000/addreceipt", {
				method: "POST",
				body: JSON.stringify({'image' : img})
			});
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