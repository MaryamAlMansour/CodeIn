import { LOGIN, LOGOUT } from '../actions/types';

export default function(state = null, action) {
    switch (action.type) {
        case LOGIN:
            return { ...state, ...action.payload };
        case LOGOUT:
            console.log('logout reducer invoked');
            return null;
        default:
            return state;
    }
}
