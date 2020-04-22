import FormControl from "@material-ui/core/FormControl";
import InputLabel from "@material-ui/core/InputLabel";
import Select from "@material-ui/core/Select";
import { makeStyles } from "@material-ui/core/styles";
import React from "react";


const useStyles = makeStyles(theme => ({
	formControl: {
		margin: theme.spacing(1),
		minWidth: 335
	},
	selectEmpty: {
		marginTop: theme.spacing(2)
	}
}));

export default function NativeSelects() {
	const classes = useStyles();
	const [state, setState] = React.useState({
		age: "",
		name: "category"
	});

	const handleChange = event => {
		const name = event.target.name;
		setState({
			...state,
			[name]: event.target.value
		});
	};

	return (
		<div>
			<FormControl className={classes.formControl}>
				<InputLabel htmlFor="cate-native">Category</InputLabel>
				<Select
					native
					value={state.age}
					onChange={handleChange}
					inputProps={{
						name: "Category",
						id: "cate-native",
					}}
				>
					<option aria-label="None" value="" />
					<option value={10}>Cat 1</option>
					<option value={20}>Cat 2</option>
					<option value={30}>Cat 3</option>
				</Select>
			</FormControl>
		</div>
	);
}
