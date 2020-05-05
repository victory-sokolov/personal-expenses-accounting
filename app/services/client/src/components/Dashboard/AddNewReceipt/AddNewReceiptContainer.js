import React, { Component } from 'react';
import AddNewReceipt from './AddNewReceipt';
class AddNewReceiptContainer extends Component {
	constructor(props) {
		super(props);
		this.inputFileRef = React.createRef();
	}

	// Trigger click input file when click is made on link
	uploadInputHandler = (e) => {
		e.preventDefault();
		this.inputFileRef.current.click();
	};

	onImageHandler = (e) => {
		e.preventDefault();
		let file = event.target.files[0];
		this.readFile(file).then(function(base64string) {
			const img = base64string.split(",")[1];
			fetch("http://localhost:5001/recognize", {
				method: "POST",
				body: JSON.stringify({ image: img, id: localStorage.getItem("id") }),
			}).catch(function(error) {
				console.log(error);
			});
		});
	};


	readFile(file) {
		return new Promise(function(resolve, reject) {
			let myReader = new FileReader();
			myReader.onloadend = function(e) {
				resolve(myReader.result);
			};
			myReader.readAsDataURL(file);
		});
	}

	handleFormUpload = (e) => {
		e.preventDefault();
		this.readFile(image).then(function(base64string) {
			const img = base64string.split(",")[1];
			this.setState({ image: img });
			fetch("http://localhost:5001/recognize", {
				method: "POST",
				body: JSON.stringify(this.state),
			});
		});
	};

	render() {
		return (
			<div>
				<AddNewReceipt
					inputFileRef={this.inputFileRef}
					uploadInputHandler={this.uploadInputHandler}
					onImageHandler={this.onImageHandler}
					showModal={this.props.showModal}
				/>
			</div>
		);
	}
}

export default AddNewReceiptContainer;