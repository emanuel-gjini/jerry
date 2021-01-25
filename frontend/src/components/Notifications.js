import NotificationList from './NotificationList';
import React from 'react';
import { connect } from 'react-redux';


const mapStateToProps = state => ({
  ...state.notificationList,
});

class Notifications extends React.Component {
  render() {
    return (
      <div className="notifications-page">
        <div className="container">
          <div className="row">
            <div className="col-xs-12 col-md-10 offset-md-1">
              <NotificationList
                notifications={this.props.notifications}
                state={this.props.currentPage} />
            </div>

          </div>
        </div>

      </div>
    );
  }
}

export default connect(mapStateToProps)(Notifications);

