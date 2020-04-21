import Utils from "@date-io/date-fns";
import { createMuiTheme } from "@material-ui/core";
import { makeStyles } from "@material-ui/core/styles";
import { KeyboardDatePicker, MuiPickersUtilsProvider } from "@material-ui/pickers";
import { ThemeProvider } from "@material-ui/styles";
import React, { useState } from "react";
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

export default function DatePickerComponent() {
	const [selectedDate, handleDateChange] = useState(new Date());

	return (
		<MuiPickersUtilsProvider utils={Utils}>
			<ThemeProvider theme={materialTheme}>
				<KeyboardDatePicker
					clearable
					value={selectedDate}
					onChange={(date) => handleDateChange(date)}
					format="MM/dd/yyyy"
					className={dashboard.MuiInput}
				/>
			</ThemeProvider>
		</MuiPickersUtilsProvider>
	);
}
