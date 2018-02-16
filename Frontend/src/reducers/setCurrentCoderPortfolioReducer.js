import { SET_CURRENT_CODER_PORTFOLIO } from '../actions/types';

export default function(state = null, action) {
    switch (action.type) {
        case SET_CURRENT_CODER_PORTFOLIO:
            return action.payload;
        default:
            return state;
    }
}
