// Query 1
// Find direct friends of a user.

MATCH (u:User {id: "U1"})-[:FRIEND_OF]->(friend:User)
RETURN
    friend.id AS friend_id,
    friend.name AS friend_name
ORDER BY friend_name;
