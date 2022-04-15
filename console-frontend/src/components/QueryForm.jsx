import React from 'react';

import apiQuery from '../api/Query';

import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';
import 'bootstrap/dist/css/bootstrap.min.css';

export default class QueryForm extends React.Component {
 
  constructor(props) {
    super(props);
    this.handleChange = this.handleChange.bind(this);
    this.runQuery = this.runQuery.bind(this);
    this.state = {responseData : null};
  }

  async runQuery() {
    const data = { query: this.state.value}
    const response = await apiQuery(data);
    this.props.setConsoleState(response.data);
  }

  handleChange(event) {
    this.setState({value: event.target.value});
  }
    
  render() {
    return (
      <Form>
        <Form.Group className='my-3' controlId="exampleForm.ControlTextarea1">
          <Form.Control as="textarea" className={['text-light', "bg-dark"]} spellCheck="false" rows={8} value={this.state.value} onChange={this.handleChange} />
        </Form.Group>
        <Button className={["float-end", "mb-5"]} variant="primary" onClick={this.runQuery}>Run query</Button>
      </Form> 
    );
  }
}
