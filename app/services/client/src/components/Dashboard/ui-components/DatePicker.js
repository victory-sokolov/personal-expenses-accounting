import Utils from "@date-io/date-fns";
import { createMuiTheme } from "@material-ui/core";
import { makeStyles } from "@material-ui/core/styles";
import { KeyboardDatePicker, MuiPickersUtilsProvider } from "@material-ui/pickers";
import { ThemeProvider } from "@material-ui/styles";
import React, { useEffect, useState } from "react";
import dashboard from "../dashboard.scss";

const materialTheme = createMuiTheme({
	spacing: 25,
	minWidth: 265
});

const useStyles = makeStyles((theme) => ({
	root: {
		"& > *": {
			width: 305,
		},
	},
}));

export default function DatePickerComponent(props) {
	const date = new Date(props.date);
	const formatedDate = `${date.getMonth()+1}/${date.getDate()}/${date.getFullYear()}`;
	const [currentDate, setDate] = useState(formatedDate);

	const handleDateChange = (date) => {
		setDate(date);
	}

	useEffect(() => {
		setDate(formatedDate);
	}, [formatedDate]);

	return (
		<MuiPickersUtilsProvider utils={Utils}>
			<ThemeProvider theme={materialTheme}>
				<KeyboardDatePicker
					clearable
					value={currentDate}
					onChange={handleDateChange}
					format="MM/dd/yyyy"
					className={dashboard.MuiInput}
				/>
			</ThemeProvider>
		</MuiPickersUtilsProvider>
	);
}
