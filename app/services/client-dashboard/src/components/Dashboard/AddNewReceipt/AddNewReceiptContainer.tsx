import MyContext from 'components/globalContext';
import React, { useContext, useState } from 'react';
import AddNewReceipt from './AddNewReceipt';

export default function AddNewReceiptContainer(props: any) {
	console.log('AddNewReceiptContainer', props);

	const inputFileRef: any = React.createRef();

	// Trigger click input file when click is made on link
	const uploadInputHandler = (e: any) => {
		e.preventDefault();
		inputFileRef.current.click();
	};

	const [open, setOpen] = useContext(MyContext);
	const [image, setImage] = useState('');

	const onImageHandler = (e: any) => {
		e.preventDefault();
		let file = e.target.files[0];
		readFile(file).then((base64: any) => {
			const img = base64.split(',')[1];
			fetch(`${process.env.REACT_APP_RECOGNITION_API}/recognize`, {
				method: 'POST',
				body: JSON.stringify({ image: img, id: localStorage.getItem('id') }),
			})
				.then((response) => {
					if (response.status === 200) {
						console.log(response.status);
					}
				})
				.catch((error) => {
					console.log(error);
				});
		});
	};

	const readFile = (file: any) => {
		return new Promise(function (resolve) {
			let myReader = new FileReader();
			myReader.onloadend = function (e) {
				resolve(myReader.result);
			};
			myReader.readAsDataURL(file);
		});
	};

	const handleFormUpload = (e: any) => {
		e.preventDefault();
		// To Do: fix image
		const image = '';
		readFile(image).then((base64string: any) => {
			const img = base64string.split(',')[1];
			setImage(img);
			fetch(`${process.env.REACT_APP_RECOGNITION_API}/recognize`, {
				method: 'POST',
				body: JSON.stringify(image),
			})
				.then((response) => response.json())
				.catch((error) => {
					console.error(error);
				});
		});
	};

	return (
		<div>
			<AddNewReceipt
				inputFileRef={inputFileRef}
				uploadInputHandler={uploadInputHandler}
				onImageHandler={onImageHandler}
				showModal={open}
			/>
		</div>
	);
}
