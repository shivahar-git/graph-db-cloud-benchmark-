// Query 5
// Find the top companies by employee count.

MATCH (employee:User)-[:WORKS_AT]->(company:Company)

RETURN
    company.id AS company_id,
    company.name AS company_name,
    COUNT(employee) AS employee_count

ORDER BY employee_count DESC, company_name ASC
LIMIT 10;
