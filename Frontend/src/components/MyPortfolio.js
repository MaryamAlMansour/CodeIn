import React, { Component } from 'react';
import { connect } from 'react-redux';
import { Link } from 'react-router-dom';
import { Button, Icon, Form, Divider } from 'semantic-ui-react';

import { fetchPortfolio, setEdittingProject } from '../actions';
import Landing from './Landing';

class MyPortfolio extends Component {
    componentWillMount() {
        this.props.fetchPortfolio();
    }

    renderPortfolio() {
        if (this.props.currentUserPortfolio) {
            const { name, email } = this.props.currentUserPortfolio;

            return (
                <Form>
                    <Form.Group unstackable widths={2}>
                        <Form.Input
                            label="First name"
                            defaultValue={name}
                            readOnly
                        />
                        <Form.Input
                            label="Last name"
                            defaultValue="Last name"
                            readOnly
                        />
                    </Form.Group>
                    <Form.Group widths={2}>
                        <Form.Input
                            label="Email"
                            defaultValue={email}
                            readOnly
                        />
                        <Form.Input
                            label="Phone"
                            defaultValue="Phone"
                            readOnly
                        />
                    </Form.Group>
                    <Button
                        animated
                        as={Link}
                        to="/editportfolio"
                        onClick={() => console.log('Edit Portfolio clicked')}
                    >
                        <Button.Content visible>Edit Portfolio</Button.Content>
                        <Button.Content hidden>
                            <Icon name="write" />
                        </Button.Content>
                    </Button>
                </Form>
            );
        } else {
            return <div />;
        }
    }
    renderProjectsHelper() {
        if (this.props.currentUserPortfolio) {
            const { projects } = this.props.currentUserPortfolio;
            return projects.map(project => {
                const { projectName, projectDescription } = project;
                return (
                    // TODO: use id for key
                    <Form key={projectName}>
                        <Form.Input
                            label="Project Name"
                            defaultValue={projectName}
                            readOnly
                        />
                        <Form.TextArea
                            label="Project Description"
                            defaultValue={projectDescription}
                            readOnly
                        />
                        <Button
                            animated
                            as={Link}
                            to="/editproject"
                            onClick={() => {
                                this.props.setEdittingProject(project);
                                console.log('editting project', project);
                                console.log('edit project clicked');
                            }}
                        >
                            <Button.Content visible>Edit</Button.Content>
                            <Button.Content hidden>
                                <Icon name="edit" />
                            </Button.Content>
                        </Button>
                        <Divider section />
                    </Form>
                );
            });
        } else {
            return <div />;
        }
    }

    renderProjects() {
        return (
            <div>
                {this.renderProjectsHelper()}
                <Button
                    animated
                    as={Link}
                    to="/addproject"
                    onClick={() => console.log('Add Project clicked')}
                    floated="right"
                >
                    <Button.Content visible>Add Project</Button.Content>
                    <Button.Content hidden>
                        <Icon name="add" />
                    </Button.Content>
                </Button>
            </div>
        );
    }

    render() {
        const content = this.props.user ? (
            <div>
                <Divider horizontal>Portfolio</Divider>
                {this.renderPortfolio()}
                <Divider horizontal>Projects</Divider>
                {this.renderProjects()}
            </div>
        ) : (
            <Landing />
        );

        return content;
    }
}

const mapStateToProps = ({ currentUserPortfolio, user }) => {
    return { currentUserPortfolio, user };
};

export default connect(mapStateToProps, { fetchPortfolio, setEdittingProject })(
    MyPortfolio
);
