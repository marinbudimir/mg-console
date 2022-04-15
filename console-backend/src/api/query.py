import mgclient
import jsons
import os

from flask import Blueprint, request, json
from flask_restx import Resource, Api, fields, marshal

query_blueprint = Blueprint('query', __name__)
api = Api(query_blueprint)

def add_type(obj):
    """Appends type to instances of mgclient classes."""

    if isinstance(obj, mgclient.Node):
        return {"type": "node", "data": obj}
    elif isinstance(obj, mgclient.Relationship):
        return {"type": "relationship", "data": obj}
    elif isinstance(obj, list):
        temp = [add_type(item) for item in obj]
        return {"type": "path", "data": temp}
    else:
        return obj

class Query(Resource):
    def post(self):
        post_data = request.get_json()
        query = post_data.get('query')

        # connect to Memgraph DB
        conn = mgclient.connect(host="host.docker.internal", port=7687)
        cursor = conn.cursor()

        # check if query was executed correctly
        try:
            cursor.execute(query)
        except mgclient.DatabaseError as err:
            # append execution result and error message
            result = {"result": "fail", "error": ("Query failed: " + str(err))}
            return result, 201

        rows = cursor.fetchall()

        # itterate through all objects in results and add type to nodes, relationships and paths
        rows = [tuple(add_type(item) for item in row)for row in rows]

        # append execution result and headers 
        formated_results ={"result": "success", "headers":tuple(column.name for column in cursor.description), "rows":[tuple(item for item in row) for row in rows]}
        
        # serialization needed for mgclient classes objects
        formated_results = jsons.dumps(formated_results)
        formated_results = jsons.loads(formated_results)

        return formated_results, 201

api.add_resource(Query, '/query')
