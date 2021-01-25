import React from 'react';
import agent from '../agent';
import { connect } from 'react-redux';
import { NOTIFICATIONS } from '../constants/actionTypes';


const mapDispatchToProps = dispatch => ({
  loadNotifications: (payload) =>
    dispatch({ type: NOTIFICATIONS, payload }),
});

const NotificationPreview = props => {
  const notification = props.notification;
  const handleClick = async ev => {
    ev.preventDefault();
    await agent.Notifications.read(notification.id);
    props.loadNotifications(agent.Notifications.get());
  };

  return (
    <div className="notification-preview" onClick={handleClick}>
      <div className="message">
        {notification.message}
      </div>
      <span className="date">
        {new Date(notification.createdAt).toDateString()}
      </span>
    </div>
  );
}

export default connect(() => ({}), mapDispatchToProps)(NotificationPreview);
