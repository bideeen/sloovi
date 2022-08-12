"# Sloovi Python Test" 
<hr>

[API](https://slapis.herokuapp.com/) is a powerful fully managed free template API provider that provides extensive APIs that range from subjects of templates and body of templates including the template name.



### How to Use the [API](https://slapis.herokuapp.com/) Endpoints
<hr>
These are the endpoints in the Template API:
<table>
 <tr><th>Endpoints</th>  <th>MethodS</th> </tr>
  <tr><td>/register</td>	<td>POST</td>	.</tr>
  <tr><td>/login</td>	<td>POST</td></tr>
  <tr><td>/templates</td>	<td>POST, GET</td></tr>
  <tr><td>/templates/<template_id></td>	<td>GET, PUT, DELETE</td></tr>
</table>


### [API](https://slapis.herokuapp.com/) Endpoints Status Codes
<table>
 <tr><th>Code</th>  <th>Meaning</th> <th>Description</th></tr>
  <tr><td>200</td>	<td>OK</td>	<td>The requested action was successful</td></tr>
  <tr><td>201</td>	<td>Created</td>	<td>A new resource was created</td></tr>
  <tr><td>202</td>	<td>Accepted</td>	<td>The request was received, but no modification has been made yet</td></tr>
  <tr><td>204</td>	<td>No Content</td>	<td>The request was successful, but the response has no content</td></tr>
  <tr><td>400</td>	<td>Bad Request</td>	<td>The request was malformed</td></tr>
  <tr><td>401</td>	<td>Unauthorized</td>	<td>The client is not authorized to perform the requested action</td></tr>
  <tr><td>404</td>	<td>Not Found</td>	<td>The requested resource was not found</td>.</tr>
  <tr><td>415</td>	<td>Unsupported Media Type</td>	<td>The request data format is not supported by the server</td></tr>
  <tr><td>422</td>	<td>Unprocessable Entity</td>	<td>The request data was properly formatted but contained invalid or missing data</td></tr>
  <tr><td>500</td>	<td>Internal Server Error</td>	<td>The server threw an error when processing the request</td></tr>
</table>
  
  
  
  
  
  
  
 
