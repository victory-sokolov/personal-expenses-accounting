import React, { useEffect, useState } from 'react';
import Button from 'react-bootstrap/Button';
import Spinner from 'react-bootstrap/Spinner';
import useFetch from '../../hooks/useFetch';
import MyContext from '../globalContext';
import dashboard from './dashboard.module.scss';
import Header from './Header';
import ModalWindow from './ModalWindow';
import Nav from './Nav/Nav';
import nav from './Nav/side-nav.module.scss';
import TransactionCard from './Transaction/TransactionCard';

export default function Dashboard() {
	const [userReceipts, setUserRceipts] = useState([]);
	const [isLoading, setIsLoading] = useState(false);
	const [inputData, setInputData] = useState({});
	const [preview, setPreview] = useState(false);
	const [open, setOpen] = useState(false);
	const [userId, setUserId] = useState(localStorage.getItem('id'));

	const [userData] = useFetch(`${process.env.REACT_APP_SERVER}/user/${userId}`);
	const [receipts] = useFetch(`${process.env.REACT_APP_SERVER}/receipt/${userId}`);

	const Delete = (props: any) => {
		return (
			<Button variant="danger" onClick={props.delete}>
				Delete
			</Button>
		);
	};

	useEffect(() => {
		setUserId(localStorage.getItem('id') || '');
	}, []);

	const deleteReceipt = async () => {
		// const receiptId = inputData.id;
		const receiptId = 1;
		await fetch(`${process.env.REACT_APP_SERVER}/receipt/${receiptId}`, {
			method: 'DELETE',
			mode: 'cors',
		})
			.then((response) => response.json())
			.catch((error) => {
				console.error('Error:', error);
			});
	};

	return (
		<MyContext.Provider value={[open, setOpen]}>
			<div className={nav.container}>
				{isLoading ? (
					<Spinner
						animation="border"
						variant="primary"
						size="sm"
						role="status"
						aria-hidden="true"
						className={dashboard.spinner}
					/>
				) : (
					<main>
						<Nav userData={userData} />
						<ModalWindow
							// handleFormUpload={handleFormUpload}
							// onChangeHandler={onChangeHandler}
							// show={open}
							inputData={inputData}
							// ref={this.modalRef}
							// postData={postData}
						>
							{Object.keys(inputData).length > 0 ? (
								<Delete delete={deleteReceipt} />
							) : null}
						</ModalWindow>
						<Header
							showModal={open}
							// imagePreviewHandler={imagePreviewHandler}
							imagePreview={preview}
						/>
						<TransactionCard receipts={receipts} />
						{/* <Transactions
							showModal={open}

							// ref={receiptSectRef}
						/> */}
					</main>
				)}
			</div>
		</MyContext.Provider>
	);
}
