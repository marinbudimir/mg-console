import mgclient

def load_initial_dataset():
    """ Load initial sample dataset to Memgraph DB if it is empty."""

    conn = mgclient.connect(host="host.docker.internal", port=7687)
    cursor = conn.cursor()

    # cursor.execute("MATCH (n)\nDETACH DELETE n;");
    # conn.commit()
    # conn.close()
    # return

    # proceed with loading dataset only if database is empty
    cursor.execute("MATCH (n) RETURN count(n);");
    res = cursor.fetchone()
    if res[0] != 0:
        return

    # load people_nodes.csv
    query = """
        LOAD CSV FROM "/usr/src/app/sample-data/people_nodes.csv" WITH HEADER AS row
        CREATE (n:Person {id: row.id, name: row.name, age: ToInteger(row.age), city: row.city});
        """
    cursor.execute(query)

    # load people_relationships.csv
    query = """
        LOAD CSV FROM "/usr/src/app/sample-data/people_relationships.csv" WITH HEADER AS row
        MATCH (p1:Person {id: row.first_person})
        MATCH (p2:Person {id: row.second_person})
        CREATE (p1)-[f:IS_FRIENDS_WITH]->(p2)
        SET f.met_in = row.met_in;
        """
    cursor.execute(query)

    # load restaurants_nodes.csv
    query = """
        LOAD CSV FROM "/usr/src/app/sample-data/restaurants_nodes.csv" WITH HEADER AS row
        CREATE (n:Restaurant {id: row.id, name: row.name, menu: row.menu});
        """
    cursor.execute(query)

    # load restaurants_relationships.csv
    query = """
        LOAD CSV FROM "/usr/src/app/sample-data/restaurants_relationships.csv" WITH HEADER AS row
        MATCH (p1:Person {id: row.PERSON_ID})
        MATCH (re:Restaurant {id: row.REST_ID})
        CREATE (p1)-[ate:ATE_AT]->(re)
        SET ate.liked = ToBoolean(row.liked);
        """
    cursor.execute(query)
    conn.commit()
    conn.close()