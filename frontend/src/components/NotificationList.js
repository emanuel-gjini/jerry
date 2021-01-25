import React from 'react';
import NotificationPreview from './NotificationPreview';

const NotificationList = props => {
  if (!props.notifications) {
    return (
      <div className="article-preview">Loading...</div>
    );
  }

  if (props.notifications.length === 0) {
    return (
      <div className="article-preview">
        No unread notifications are here... yet.
      </div>
    );
  }

  return (
    <div className="article-preview">
      {
        props.notifications.map(notification => {
          return (
            <NotificationPreview notification={notification} key={notification.id} />
          );
        })
      }
    </div>
  );
};

export default NotificationList;
