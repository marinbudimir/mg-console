import React from 'react';
import Table from 'react-bootstrap/Table';
import 'bootstrap/dist/css/bootstrap.min.css';

export default class ResponseTable extends React.Component {
 
  constructor(props){
    super(props);
    this.getHeader = this.getHeader.bind(this);
    this.getRowsData = this.getRowsData.bind(this);
  }
    
  getHeader(){
    var keys = this.props.data.headers;
    return keys.map((key, index)=>{
      return <th key={key}>{key}</th>
    })
  }
    
  getRowsData() {
    var items = this.props.data.rows;
    return items.map((row, index)=>{
      return <tr key={index}><RenderRow key={index} data={row}/></tr>
    })
  }
    
  render() {
    return (
    <div>
      <Table striped bordered hover variant="dark">
        <thead>
          <tr>{this.getHeader()}</tr>
        </thead>
        <tbody>
          {this.getRowsData()}
        </tbody>
      </Table>
    </div>
    );
  }
}
  
const RenderRow = (props) =>{
  return props.data.map((item, index)=>{
    const parsedItem = parseData(item);
    return <td key={parsedItem.key}>{parsedItem.value}</td>;
  })
}

/**
 * Prepares all response items for represenation
 * depending on whether they are Memgraph nodes, relationships,
 * paths or simple object.
 * @param {*} item response item
 * @returns item ready for representation in <td></td>
 */
function parseData(item) {
  var result = {};
  switch (item.type) {
    case 'node':
      result["key"] = item.data.id;
      result["value"] = JSON.stringify(item.data.labels).concat(":", JSON.stringify(item.data.properties));
      break;
    case 'relationship':
      result["key"] = item.data.id;
      result["value"] = JSON.stringify(item.data.type).concat(":", JSON.stringify(item.data.properties));
      break;
    case 'path':
      result["key"] = "path";
      var value = [];
      item.data.forEach(element => {
        const temp = parseData(element);
        value.push(temp["value"]);
      });
      result["value"] = value.join()
      break;
    default:
      result["key"] = item;
      result["value"] = item;
  }

  return result;
}