// Query 4
// Find the shortest friendship path between two users.

MATCH (start:User {id: "U1"}), (target:User {id: "U100"})

MATCH p = shortestPath((start)-[:FRIEND_OF*]-(target))

RETURN
    length(p) AS hop_count,
    [node IN nodes(p) | node.id] AS path_nodes,
    [rel IN relationships(p) | type(rel)] AS relationship_types;
