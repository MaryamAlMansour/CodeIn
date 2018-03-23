import React from 'react';

import LoginOptions from './LoginOptions';

const Landing = () => {
    return (
        <div style={{ textAlign: 'center' }}>
            <div>
                <h1>CoderIn!</h1>
                Find smartest coders!
            </div>
            <LoginOptions />
        </div>
    );
};

export default Landing;
