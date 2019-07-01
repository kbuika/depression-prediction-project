import React from "react";

const Input = props => {
    return (
        <div>
            <label>
                <input
                    id={props.name}
                    name={props.name}
                    type={props.type}
                    value={props.value}
                    onChange={props.handleChange}
                    placeholder={props.placeholder}
                    className={props.style}
                    required
                
                />
            </label>

        </div>
    );
};

export default Input;