import { combineReducers } from 'redux';
import authReducer from './authReducers';
import coderReducer from './coderReducer';
import portfolioReducer from './portfolioReducer';
import projectReducer from './projectReducer';
import setCurrentCoderPortfolioReducer from './setCurrentCoderPortfolioReducer';

const rootReducer = combineReducers({
    user: authReducer,
    coders: coderReducer,
    currentUserPortfolio: portfolioReducer,
    currentEdittingProject: projectReducer,
    currentCoderPortfolio: setCurrentCoderPortfolioReducer
});

export default rootReducer;

// TODO: make sure the init auth is false
