import Utils from "@date-io/date-fns";
import { createMuiTheme } from "@material-ui/core";
import { KeyboardDatePicker, MuiPickersUtilsProvider } from "@material-ui/pickers";
import { ThemeProvider } from "@material-ui/styles";
import React, { useState } from "react";

const materialTheme = createMuiTheme({
	spacing: 25,
	minWidth: 265
});

export default function DatePickerComponent() {

	const [selectedDate, handleDateChange] = useState(new Date());

	return (
		<MuiPickersUtilsProvider utils={Utils}>
			<ThemeProvider theme={materialTheme}>
				<KeyboardDatePicker
					clearable
					value={selectedDate}
					onChange={date => handleDateChange(date)}
					minDate={new Date()}
					format="MM/dd/yyyy"
				/>
			</ThemeProvider>
		</MuiPickersUtilsProvider>
	);
}
