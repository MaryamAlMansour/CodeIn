import React from 'react';
import { connect } from 'react-redux';
import { Link } from 'react-router-dom';
import { Header, Segment } from 'semantic-ui-react';
import { logout } from '../actions';

class AppHeader extends React.Component {
    renderHeaderLeft() {
        // TODO: add greeting next to Logo
        if (this.props.user) {
            return (
                <Header
                    as={Link}
                    floated="left"
                    to="/dashboard"
                    onClick={() => console.log('logo clicked while logged in')}
                >
                    CodeIn
                </Header>
            );
        } else {
            return (
                <Header
                    as={Link}
                    floated="left"
                    to="/"
                    onClick={() => console.log('logo clicked while logged out')}
                >
                    CodeIn
                </Header>
            );
        }
    }
    renderHeaderRight() {
        if (this.props.user) {
            return (
                <div>
                    <Header as={Link} to="/myportfolio" floated="right">
                        myportfolio
                    </Header>
                    <Header
                        as={Link}
                        to="/logout"
                        floated="right"
                        onClick={() => {
                            this.props.logout();
                            console.log('logout clicked');
                        }}
                    >
                        logout
                    </Header>
                </div>
            );
        }
    }
    render() {
        return (
            <Segment clearing color="blue">
                {this.renderHeaderLeft()}
                {this.renderHeaderRight()}
            </Segment>
        );
    }
}

function mapStateToProps({ user }) {
    return { user };
}

export default connect(mapStateToProps, { logout })(AppHeader);
