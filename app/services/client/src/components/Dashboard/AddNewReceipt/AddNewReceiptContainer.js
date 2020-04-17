import React, { Component } from 'react';
import ModalWindow from '../ModalWindow';

class AddNewReceiptContainer extends Component {
	constructor(props, context) {
		super(props, context);
		this.state = {
			vendor: "",
			date: "",
			amount: "",
			category: "",
			warranty: "",
			image: null,
			imagePath: null,
			renderImageUpload: true,
		};
		this.handleFormUpload = this.handleFormUpload.bind(this);
		this.onChangeHandler = this.onChangeHandler.bind(this);
		this.onImageHandler = this.onImageHandler.bind(this);
		this.componentMount = this.componentMount.bind(this);
	}

	onImageHandler(event) {
		let file = event.target.files[0];
		this.setState({ image: file });
		if (file != null) {
			let image = URL.createObjectURL(file);
			this.componentMount(image););
		}
	}

	componentMount(image) {
		this.setState((prevState) => ({
			renderImageUpload: !prevState.renderImageUpload,
			imagePath: image,
		}));
	}

	onChangeHandler() {
		this.setState({
			[event.target.name]: event.target.value,
		});
	}

	readFile(file) {
		return new Promise(function(resolve, reject) {
			let myReader = new FileReader();
			myReader.onloadend = function(e) {
				resolve(myReader.result);
			};
			myReader.readAsDataURL(file);
		});
	}

	handleFormUpload(e) {
		e.preventDefault();

		this.readFile(image).then(function(base64string) {
			const img = base64string.split(",")[1];
			this.setState({ image: img });
			fetch("http://localhost:5000/addreceipt", {
				method: "POST",
				body: JSON.stringify(this.state),
			});
		});
	}

	render() {
		return (
			<ModalWindow
				handleFormUpload={this.handleFormUpload}
				onChangeHandler={this.onChangeHandler}
				onImageHandler={this.onImageHandler}
				componentMount={this.componentMount}
				receiptData={this.state}
			/>
		);
	}
}

export default AddNewReceiptContainer;