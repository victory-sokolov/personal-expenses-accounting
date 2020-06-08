import React, { Component } from 'react';
import Toast from "../ui-components/Toast";
import AddNewReceipt from './AddNewReceipt';

class AddNewReceiptContainer extends Component {
	constructor(props) {
		super(props);
		this.state = {
			toastText: ''
		};
		this.inputFileRef = React.createRef();
		this.notificationRef = React.createRef();
	}

	// Trigger click input file when click is made on link
	uploadInputHandler = (e) => {
		e.preventDefault();
		this.inputFileRef.current.click();
	};

	onImageHandler = (e) => {
		e.preventDefault();
		let file = event.target.files[0];
		this.notificationRef.current.showToast();
		this.setState({ toastText: "Receipt is being recognized."});
		this.readFile(file).then(function(base64string) {
			const img = base64string.split(",")[1];
			fetch("http://localhost:5001/recognize", {
				method: "POST",
				body: JSON.stringify({ image: img, id: localStorage.getItem("id") }),
			}).then((response) => {
				if (response.status == 200) {
					console.log(response.status);
				}
			})
			.catch(function(error) {
				console.log(error);
			});
		});
	};


	readFile = (file) => {
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
			}).catch(function(error) {
				console.log(error);
			});
			let result = response.json();
			console.log(result);
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
				<Toast text={this.state.toastText} ref={this.notificationRef} />
			</div>
		);
	}
}

export default AddNewReceiptContainer;