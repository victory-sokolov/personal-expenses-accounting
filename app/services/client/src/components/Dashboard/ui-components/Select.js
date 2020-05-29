import FormControl from "@material-ui/core/FormControl";
import InputLabel from "@material-ui/core/InputLabel";
import Select from "@material-ui/core/Select";
import { makeStyles } from "@material-ui/core/styles";
import React from "react";
import { category } from './categories';

const useStyles = makeStyles(theme => ({
	formControl: {
		margin: theme.spacing(1),
		minWidth: 335
	},
	selectEmpty: {
		marginTop: theme.spacing(2)
	}
}));

const categories = Object.keys(category);

export default function NativeSelects(props) {
	const classes = useStyles();
	const [state, setState] = React.useState({
		age: "",
		name: "category"
	});


	const handleChange = event => {
		const name = event.target.value;
		setState({
			...state,
			[name]: event.target.value
		});
	};

	return (
		<div>
			<FormControl className={classes.formControl}>
				<InputLabel htmlFor="cate-native">Choose category</InputLabel>
				<Select
					native
					onChange={props.onChange}
					inputProps={{
						name: "Category",
						id: "cate-native",
					}}
				>
					<option defaultValue disabled hidden>
						Choose category
					</option>
					{categories.map((cat, id) => {
						return (
							<option key={id} value={cat}>
								{cat}
							</option>
						);
					})}
				</Select>
			</FormControl>
		</div>
	);
}
