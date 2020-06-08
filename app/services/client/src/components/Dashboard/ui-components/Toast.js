import classNames from "classnames";
import React, { Component } from 'react';
import toast from "./toast.scss";

export default class Toast extends Component {

    constructor(props) {
        super(props);
        this.state = {
			toastActive:false,
		};
    }

	closeToast = () => {
        console.log("show toast");
		this.setState({ toastActive: !this.state.toastActive });
	};

	showToast = () => {
        this.setState({ toastActive: !this.state.toastActive });
	};

    render() {
        let toastStyle = classNames(toast.toast, toast.jam, {
                [toast.on]: this.state.toastActive,
        });
        return (
            <div className={toastStyle} aria-hidden="true">
                <span
                    className={toast.close}
                    tabIndex="0"
                    onClick={(e) => this.closeToast(e)}
                >
                    &times;
                </span>
                {this.props.text}
            </div>
        );
    }

}


