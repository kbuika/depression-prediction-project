import React, { Component } from "react";
import Form from "./components/form";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      form: {
        age: ""
      }
    };
    this.hadleUserInput = this.handleUserInput.bind(this);
  
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
        <Form />
      </div>
    )
  }
}

export default App;
