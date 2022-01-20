import { configure, shallow } from "enzyme";
import Adapter from "enzyme-adapter-react-16";
import React from 'react';
import LoginForm from '../LoginForm';

configure({ adapter: new Adapter() });

describe("Form", () => {
    it("Fill Login form data", () => {
        const wrapper = shallow(<LoginForm />)
        let email = wrapper.find('input').first();
        email.simulate("change", {
					target: { value: "viktor" },
				});
        email = wrapper.find("input").first();
        expect(nameInput.props().value).toEqual('viktor')
    })
});