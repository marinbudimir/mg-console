import React from 'react';

import { Container, Row } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';

import QueryForm from './QueryForm';
import ResponseTable from './ResponseTable';
import ErrorResponse from './ErrorResponse';

export default class Console extends React.Component {
 
  constructor(props) {
    super(props);
    this.setConsoleState = this.setConsoleState.bind(this);
    this.state = {response : {"result": "undefined"}};
  }

  setConsoleState(res) {
    this.setState({response: res})
  }
    
  render() {
    return (
      <Container>
        <Row className="justify-content-md-center">
          <QueryForm setConsoleState={this.setConsoleState}/>
        </Row>
        <Row className="justify-content-md-center">
          <Results response={this.state.response}/>
        </Row>
      </Container>
    );
  }
}

const Results = (props) =>{
  switch (props.response["result"]) {
    case "undefined":
      return <></>;
    case "success":
      return <ResponseTable data={props.response}/>;
    case "fail":
      return <ErrorResponse data={props.response}/>;
    default:
      return <></>;
  }
}