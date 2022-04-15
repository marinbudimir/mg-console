import axios from "axios";

/**
 * Execute POST method on http://localhost:5004/query
 * @param {*} data POST request data
 * @returns 
 */
export default async function apiQuery(data) {
  var response = await axios.post('http://localhost:5004/query', data);
  return response;
}