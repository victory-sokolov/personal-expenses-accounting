import { useState } from 'react';

const useInput = (initialValue: string): any => {
	const [value, setValue] = useState(initialValue);

	const handleChange = (e: React.ChangeEvent<HTMLInputElement>): void => {
		setValue(e.target.value);
	};

	return [value, handleChange];
};

export default useInput;
