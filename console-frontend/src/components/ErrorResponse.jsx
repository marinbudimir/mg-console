import React from 'react';
import Alert from 'react-bootstrap/Alert';

export default class ErrorResponse extends React.Component {
  
  render() {
    return (
      <Alert variant="danger">
        <Alert.Heading>Query failed</Alert.Heading>
        <p>
          {this.props.data["error"]}
        </p>
      </Alert>
    );
  }
}