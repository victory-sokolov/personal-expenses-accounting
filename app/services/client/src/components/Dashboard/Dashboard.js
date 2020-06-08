
import React, { Component } from 'react';
import Button from "react-bootstrap/Button";
import Spinner from "react-bootstrap/Spinner";
import cards from "./Cards/cards.scss";
import SmallCard from "./Cards/SmallCard";
import PieChart from "./Charts/PieChart";
import YearChart from "./Charts/YearChart";
import dashboard from "./dashboard.scss";
import Header from "./Header";
import ModalWindow from "./ModalWindow";
import Nav from "./Nav/Nav";
import nav from "./Nav/side-nav.scss";
import ReceiptSection from "./Receipt/ReceiptSection";


const Delete = (props) => {
	return (
		<Button variant="danger" onClick={props.delete}>
			Delete
		</Button>
	);
}

class Dashboard extends Component {
	constructor(props) {
		super(props);
		this.state = {
			isLoading: true,
			show: false,
			data: {},
			preview: false,
			inputData: {},
			usersReceipts: {}
		};
		this.modalRef = React.createRef();
		this.receiptSectRef = React.createRef();
	}


	handleClose = () => {
		this.setState({ show: false });
		this.setState({ inputData: {} });
		this.modalRef.current.resetInputFields();
		this.receiptSectRef.current.setCurrentReceiptState();
		this.modalRef.current.imagePreviewHandler();
	};

	handleShow = () => {
		this.setState({ show: true });
		let receipt = this.receiptSectRef.current.getCurrentReceiptState();
		if (Object.keys(receipt).length > 0) {
			this.setState({ inputData: receipt }, () => {
				this.modalRef.current.setInputFields();
			});
		}
	};

	componentDidMount() {
		const id = localStorage.getItem("id");
		this.fetchData(`/user/${id}`, "GET"); 
	}

	postData = async(url, method, data) => {
		await fetch(url, {
			method: method,
			headers: {
				"Content-Type": "application/json",
			},
			body: JSON.stringify(data),
		})
			.then((response) => response.json())
			.catch((error) => {
				console.error("Error:", error);
			});
			// force to update component
			this.forceUpdate();
	}

	fetchData = async (url, method) => {
		await fetch(url, {
			method: method,
			cache: 'no-cache',
			headers: {
				"Content-Type": "application/json",
			},
		})
			.then((response) => response.json())
			.then((data) => {
				this.setState({ data: data, isLoading: false });
			})
			.catch((error) => {
				console.error("Error:", error);
			});
	};

	deleteReceipt = async () => {
		const receiptId = this.state.inputData.id;
		await fetch(`/receipt/${receiptId}`, {
			method: "DELETE",
		}).then(response => response.json())
		.catch((error) => {
			console.error("Error:", error);
		});
		this.handleClose();
		this.forceUpdate();
	};

	render() {
		return (
			<div className={nav.container}>
				{this.state.isLoading ? (
					<Spinner
						animation="border"
						variant="primary"
						size="lg"
						role="status"
						aria-hidden="true"
						className={dashboard.spinner}
					/>
				) : (
					<main>
						<Nav userData={this.state.data} />
						<ModalWindow
							handleFormUpload={this.handleFormUpload}
							onChangeHandler={this.onChangeHandler}
							show={this.state.show}
							handleClose={this.handleClose}
							inputData={this.state.inputData}
							ref={this.modalRef}
							postData={this.postData}
						>
							{Object.keys(this.state.inputData).length > 0 ? (
								<Delete delete={this.deleteReceipt} />
							) : null}
						</ModalWindow>
						<Header
							showModal={this.handleShow}
							imagePreviewHandler={this.imagePreviewHandler}
							imagePreview={this.state.preview}
						/>
						<SmallCard receiptData={this.state.data.receipts} />
						<div className={cards.chartsWrapper}>
							<YearChart />
							<PieChart />
						</div>

						<ReceiptSection
							showModal={this.handleShow}
							receipts={this.state.data}
							ref={this.receiptSectRef}
						/>
					</main>
				)}
			</div>
		);
	}
}

export default Dashboard;