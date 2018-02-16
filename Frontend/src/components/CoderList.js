import React, { Component } from 'react';
import { connect } from 'react-redux';
import {
    Button,
    Header,
    Icon,
    Modal,
    Card,
    Form,
    Divider
} from 'semantic-ui-react';

import {
    fetchCoders,
    setCurrentCoderPortfolio,
    addContact
} from './../actions';

class CoderList extends Component {
    state = { modalOpen: false };

    handleOpen = () => this.setState({ modalOpen: true });

    handleClose = () => this.setState({ modalOpen: false });

    componentWillMount() {
        this.props.fetchCoders();
    }
    renderPortfolio = () => {
        const { name, email } = this.props.currentCoderPortfolio;
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
                    <Form.Input label="Email" defaultValue={email} readOnly />
                    <Form.Input label="Phone" defaultValue="Phone" readOnly />
                </Form.Group>
            </Form>
        );
    };
    renderProjectsHelper = () => {
        const { projects } = this.props.currentCoderPortfolio;
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
                    <Divider section />
                </Form>
            );
        });
    };

    renderProjects = () => {
        return <div>{this.renderProjectsHelper()}</div>;
    };

    renderScrollContent = () => {
        if (this.props.currentCoderPortfolio) {
            return (
                <div>
                    <Divider horizontal>Portfolio</Divider>
                    {this.renderPortfolio()}
                    <Divider horizontal>Projects</Divider>
                    {this.renderProjects()}
                </div>
            );
        } else {
            return null;
        }
    };

    renderModal = coder => {
        return (
            <Modal
                dimmer="blurring"
                open={this.state.modalOpen}
                onClose={this.handleClose}
                trigger={
                    <Button
                        basic
                        color="green"
                        onClick={() => {
                            this.props.setCurrentCoderPortfolio(coder);
                            this.handleOpen();
                        }}
                    >
                        View Portfolio
                    </Button>
                }
            >
                <Modal.Header>Profile Picture</Modal.Header>
                <Modal.Content scrolling>
                    <Modal.Description>
                        <Header>Modal Header</Header>
                        <p>
                            This is an example of expanded content that will
                            cause the modal's dimmer to scroll
                        </p>

                        <div>{this.renderScrollContent()}</div>
                    </Modal.Description>
                </Modal.Content>
                <Modal.Actions>
                    <Button
                        secondary
                        onClick={() => {
                            this.handleClose();
                        }}
                    >
                        Exit <Icon name="left chevron" />
                    </Button>
                    <Button
                        primary
                        onClick={() => {
                            this.props.addContact(coder);
                            this.handleClose();
                        }}
                    >
                        Add Contact <Icon name="right chevron" />
                    </Button>
                </Modal.Actions>
            </Modal>
        );
    };

    renderCard() {
        return this.props.coders.map(coder => {
            // TODO: use id instead of name
            const { name, role, exp } = coder;
            return (
                <Card key={name}>
                    <Card.Content>
                        <Card.Header>{name}</Card.Header>
                        <Card.Meta>{role}</Card.Meta>
                        <Card.Description>{exp}</Card.Description>
                    </Card.Content>
                    <Card.Content extra>
                        <div className="ui two buttons">
                            {this.renderModal(coder)}

                            <Button
                                basic
                                color="blue"
                                onClick={() => this.props.addContact(coder)}
                            >
                                Add Contact
                            </Button>
                        </div>
                    </Card.Content>
                </Card>
            );
        });
    }
    renderCards() {
        if (this.props.coders) {
            return <Card.Group>{this.renderCard()}</Card.Group>;
        } else {
            return <div />;
        }
    }
    render() {
        return <div>{this.renderCards()}</div>;
    }
}

const mapStateToProps = ({ coders, currentCoderPortfolio }) => {
    return { coders, currentCoderPortfolio };
};

export default connect(mapStateToProps, {
    fetchCoders,
    setCurrentCoderPortfolio,
    addContact
})(CoderList);
