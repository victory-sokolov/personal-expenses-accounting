import Button from "@material-ui/core/Button";
import IconButton from "@material-ui/core/IconButton";
import { makeStyles } from "@material-ui/core/styles";
import PhotoCamera from "@material-ui/icons/PhotoCamera";
import React from "react";

const useStyles = makeStyles(theme => ({
	root: {
		"& > *": {
			margin: theme.spacing(1)
		}
	},
	input: {
		display: "none"
	}
}));


export default function FileUpload() {
	const classes = useStyles();

	return (
		<div className={classes.root}>
			<input
				accept="image/*"
				className={classes.input}
				id="contained-button-file"
				multiple
				type="file"
			/>
			<label htmlFor="contained-button-file">
				<Button variant="contained" color="primary" component="span">
					Upload
				</Button>
			</label>
			<input
				accept="image/*"
				className={classes.input}
				id="icon-button-file"
				type="file"
			/>
			<label htmlFor="icon-button-file">
				<IconButton
					color="primary"
					aria-label="upload picture"
					component="span"
				>
					<PhotoCamera />
				</IconButton>
			</label>
		</div>
	);
}
