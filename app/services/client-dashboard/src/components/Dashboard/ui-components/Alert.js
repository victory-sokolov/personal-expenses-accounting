import React, { Component } from "react";
import Alert from 'react-bootstrap/Alert';
class CustomAlert extends Component {
    constructor(props) {
        super(props);
        this.state = {
            show: false,
            setShow: false,
            variant: "",
            message: "",
        };
    }


    render() {
        return (
					<Alert
						variant={this.props.variant}
						show={this.props.show}
						onClose={() => (this.state.setShow = false)}
                        dismissible
					>
						<strong>{this.props.message}</strong>
					</Alert>
				);
    }
}

export default CustomAlert;