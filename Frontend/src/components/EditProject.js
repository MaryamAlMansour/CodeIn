import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import { connect } from 'react-redux';
import { withRouter } from 'react-router-dom';
import { Button, Icon, Form } from 'semantic-ui-react';

import { saveProject } from '../actions';
import Landing from './Landing';

class EditProject extends Component {
    render() {
        if (this.props.user) {
            const {
                projectName,
                projectDescription
            } = this.props.currentEdittingProject;
            return (
                <Form>
                    <Form.Input
                        label="Project Name"
                        defaultValue={projectName}
                    />
                    <Form.TextArea
                        label="Project Description"
                        defaultValue={projectDescription}
                    />
                    <div>
                        <Button
                            primary
                            animated
                            as={Link}
                            to="/myportfolio"
                            onClick={() => console.log('add clicked')}
                        >
                            <Button.Content visible>Save</Button.Content>
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
        } else {
            this.props.history.push('/');
            return <Landing />;
        }
    }
}

const mapStateToProps = ({ currentEdittingProject, user }) => {
    return { currentEdittingProject, user };
};

export default connect(mapStateToProps, { saveProject })(
    withRouter(EditProject)
);
