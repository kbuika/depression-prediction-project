import React from "react";

const Selection = props => {
    return (
        <div>
            <label>
                <select
                    name={props.name}
                    value={props.value}
                    onChange={props.handleChange}
                >
                    <option value="" disabled>
                        {props.placeholder}

                    </option>
                    {props.options.map(option => {
                        return (
                            <option key={option} value={option} label={option}>
                                {option}

                            </option>
                        );
                    })}

                </select>
            </label>
        </div>
    );
};

export default Selection;