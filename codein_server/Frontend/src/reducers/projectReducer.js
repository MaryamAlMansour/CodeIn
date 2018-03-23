import { SET_EDITTING_PROJECT } from '../actions/types';

export default function(state = null, action) {
    switch (action.type) {
        case SET_EDITTING_PROJECT:
            return action.payload;
        default:
            return state;
    }
}
