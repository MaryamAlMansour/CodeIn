import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import { connect } from 'react-redux';
import { Button, Icon, Form, Input, TextArea } from 'semantic-ui-react';

import { saveProject } from '../actions';

class AddProject extends Component {
    render() {
        return (
            <Form>
                <Form.Field
                    id="form-input-control-first-name"
                    control={Input}
                    label="Project Name"
                    placeholder="Project Name"
                />
                <Form.Field
                    id="form-textarea-control-opinion"
                    control={TextArea}
                    label="Project Description"
                    placeholder="Project Description"
                />
                <Form.Group grouped>
                    <label>HTML radios</label>
                    <Form.Field
                        label="This one"
                        control="input"
                        type="radio"
                        name="htmlRadios"
                    />
                    <Form.Field
                        label="That one"
                        control="input"
                        type="radio"
                        name="htmlRadios"
                    />
                </Form.Group>
                <Form.Group grouped>
                    <label>HTML checkboxes</label>
                    <Form.Field
                        label="This one"
                        control="input"
                        type="checkbox"
                    />
                    <Form.Field
                        label="That one"
                        control="input"
                        type="checkbox"
                    />
                </Form.Group>
                <div>
                    <Button
                        primary
                        animated
                        as={Link}
                        to="/myportfolio"
                        onClick={() => console.log('add clicked')}
                    >
                        <Button.Content visible>Add</Button.Content>
                        <Button.Content hidden>
                            <Icon name="check" />
                        </Button.Content>
                    </Button>
                    <Button secondary animated as={Link} to="/myportfolio">
                        <Button.Content visible>Cancel</Button.Content>
                        <Button.Content hidden>
                            <Icon name="cancel" />
                        </Button.Content>
                    </Button>
                </div>
            </Form>
            // TODO: add saveProject action callback
        );
    }
}

export default connect(null, { saveProject })(AddProject);
