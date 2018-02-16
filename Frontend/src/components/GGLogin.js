/**
 * Note: 'Block third-party cookies' must be disabled to make this component work
 * chrome://settings/content/cookies
 */
import React from 'react';
import { connect } from 'react-redux';
import { withRouter } from 'react-router-dom';
import { GoogleLogin } from 'react-google-login';

import { login } from '../actions';

class GGLogin extends React.Component {
    responseOnSuccess = response => {
        const { profileObj } = response;
        console.log(profileObj);
        this.props.login(profileObj);
        this.props.history.push('/dashboard');
    };
    responseOnFailure = response => {
        alert(
            `Please go to 'chrome://settings/content/cookies' and disable 'Block third-party cookies' to enable login with Google`
        );
    };
    render() {
        return (
            <GoogleLogin
                clientId="806914580079-9msqlpl8f51fd3diiflsthebog8l7p2u.apps.googleusercontent.com"
                buttonText="LOGIN WITH GOOGLE"
                onSuccess={this.responseOnSuccess}
                onFailure={this.responseOnFailure}
                style={{}}
                className="ui red fluid button"
            />
        );
    }
}

export default connect(null, { login })(withRouter(GGLogin));
