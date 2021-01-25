import {
    NOTIFICATIONS,
    NEW_NOTIFICATION
} from '../constants/actionTypes';

export default (state = {}, action) => {
    switch (action.type) {
        case NOTIFICATIONS:
            return {
                ...state,
                notifications: action.payload.notifications,
            };
        case NEW_NOTIFICATION:
            return {
                ...state,
                notifications: [action.newNotification, ...state.notifications],
            };
        default:
            return state;
    }
};
