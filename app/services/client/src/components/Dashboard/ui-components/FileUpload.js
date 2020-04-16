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
				id="icon-button-file"
				type="file"
			/>
			<label htmlFor="icon-button-file">
				<IconButton
					color="primary"
					aria-label="upload picture"
					component="span"
				>
				<PhotoCamera style={{ fontSize: 80 }} />
				</IconButton>
			</label>
		</div>
	);
}
