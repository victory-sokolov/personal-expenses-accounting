import React from 'react';
import styled from "styled-components";

// Extract our Sass variables into a JS object
const color = require('sass-extract-loader?{"plugins": ["sass-extract-js"]}!../../ui-elements/colors.scss');

const InputOutline = (props) => {

    const {
        type,
        id,
        value,
        name,
        onChange,
		placeholder,
		required = true,
        label = ""
	} = props;

    return (
			<InputContainer>
				<Input
					type={type}
					id={id}
					value={value}
					name={name == undefined ? id : name}
					placeholder={placeholder}
					required={required}
					onChange={onChange}
				/>
				<label htmlFor={id}>{label}</label>
				<Bar></Bar>
			</InputContainer>
		);
}


const Input = styled.input`
	outline: none;
	z-index: 10;
	position: relative;
	background: none;
	width: 100%;
	height: 60px;
	border: 0;
	color: #212121;
	font-size: 16px;
	font-weight: 400;

	&:focus {
		~ label {
			color: #9d9d9d;
			transform: translate(-12%, -50%) scale(0.75);
		}

		~ .bar {
			&:before,
			&:after {
				width: 50%;
			}
		}
	}

	&:valid {
		~ label {
			color: #9d9d9d;
			transform: translate(-12%, -50%) scale(0.75);
		}
	}

	+ label {
		position: absolute;
		top: 0;
		left: 0;
		color: ${color.primaryColor};
		font-size: 16px;
		font-weight: 300;
		line-height: 60px;
		z-index: 1;
	}

	&:focus ~ ${Bar}:before, &:focus ~ ${Bar}:after {
		width: 50%;
	}
`;

const Bar = styled.div`
	position: absolute;
	left: 0;
	bottom: 0;
	background: ${color.primaryLight};
	width: 100%;
	height: 1px;

	&:before,
	&:after {
		content: "";
		position: absolute;
		background: ${color.primaryColor};
		width: 0;
		height: 2px;
		transition: 0.2s ease;
	}

	&:before {
		left: 50%;
	}
	&:after {
		right: 50%;
	}
`;

const InputContainer = styled.div`
	position: relative;
	margin: 0 10px 50px;
`;

export default InputOutline;