import React, { Component } from "react";
import Input from "./form-components/input";


class Form extends Component {
    constructor(props) {
        super(props);
        this.state = {
            newUser: {
                age: ""
            }
        };
        this.handleUserInput = this.handleUserInput.bind(this)
    }
    handleUserInput(e) {
        let value = e.target.value;
        let name = e.target.name;
        this.setState(prevState => {
            return {
                newUser: {
                    ...prevState.newUser,
                    [name]: value
                }
            };
        });
    }

render() {
    return (
        <div>
            {
                <Input
                    type={"text"}
                    title={"Age"}
                    name={"age"}
                    placeholder={"Enter your age"}
                    value={this.state.newUser.age}
                    handleChange={this.handleUserInput}
                />
            }
        </div>
    );
}

}

export default Form;