// Query 3
// Recommend products based on purchases made by direct friends.
// Excludes products already purchased by the target user.

MATCH (u:User {id: "U1"})-[:FRIEND_OF]->(friend:User)
MATCH (friend)-[:PURCHASED]->(product:Product)
WHERE NOT (u)-[:PURCHASED]->(product)

RETURN
    product.id AS product_id,
    product.name AS product_name,
    COUNT(friend) AS recommendation_score

ORDER BY recommendation_score DESC, product_name ASC
LIMIT 10;
