import React, { Component } from 'react';
import { BrowserRouter, Route } from 'react-router-dom';
import { Container } from 'semantic-ui-react';

import AppHeader from './AppHeader';
import Landing from './Landing';
import Dashboard from './Dashboard';
import MyPortfolio from './MyPortfolio';
import AddProject from './AddProject';
import LoginEmailPassword from './LoginEmailPassword';
import Logout from './Logout';
import EditPortfolio from './EditPortfolio';
import EditProject from './EditProject';

class App extends Component {
    render() {
        return (
            <BrowserRouter>
                <Container style={{ marginTop: '3em' }}>
                    {/* Header will always display because it is not in Route. */}
                    <AppHeader />
                    <Route exact path="/" component={Landing} />
                    <Route exact path="/dashboard" component={Dashboard} />
                    <Route
                        exact
                        path="/loginemailpassword"
                        component={LoginEmailPassword}
                    />
                    <Route exact path="/logout" component={Logout} />
                    <Route
                        exact
                        path="/editportfolio"
                        component={EditPortfolio}
                    />
                    <Route exact path="/myportfolio" component={MyPortfolio} />
                    <Route exact path="/addproject" component={AddProject} />
                    <Route exact path="/editproject" component={EditProject} />
                </Container>
            </BrowserRouter>
        );
    }
}

export default App;
