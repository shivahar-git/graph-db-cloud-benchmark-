// Query 2
// Find friends-of-friends (2-hop traversal) while excluding direct friends
// and the starting user.

MATCH (u:User {id: "U1"})-[:FRIEND_OF]->(:User)-[:FRIEND_OF]->(fof:User)
WHERE fof.id <> "U1"
  AND NOT (u)-[:FRIEND_OF]->(fof)
RETURN DISTINCT
    fof.id AS friend_of_friend_id,
    fof.name AS friend_of_friend_name
ORDER BY friend_of_friend_name;
