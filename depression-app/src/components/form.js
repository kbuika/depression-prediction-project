import React, { Component } from "react";
import Input from "./form-components/input";
import Selection from "./form-components/selection";


class Form extends Component {
    constructor(props) {
        super(props);
        this.state = {
            newUser: {
                age: "",
                gender: ""
            },
            gender: [
                "Male",
                "Female",
                "Other"
            ]
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
            <div>
            {
                <Input
                    type={"text"}
                    title={"Age"}
                    name={"age"}
                    label={"Age"}
                    placeholder={"Enter your age"}
                    value={this.state.newUser.age}
                    handleChange={this.handleUserInput}
                />
            }
            </div>
            <div>
                {
                    <Selection
                        type={"select"}
                        title={"Gender"}
                        name={"gender"}
                        label={"Gender"}
                        placeholder={"Select your Gender"}
                        value={this.state.newUser.gender}
                        options={this.state.gender}
                        handleChange={this.handleUserInput}
                    />
                }
            </div>
            <div>
                {
                    <Selection
                        
                    />
                }
            </div>
        </div>
    );
}

}

export default Form;