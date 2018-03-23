import { FETCH_CODERS } from '../actions/types';

export default function(state = null, action) {
    switch (action.type) {
        case FETCH_CODERS:
            return action.payload;
        default:
            return state;
    }
}
