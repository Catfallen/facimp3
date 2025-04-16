SELECT 
    cat.name AS categoria,
    SUM(p.amount) AS receita_total
FROM 
    category cat
JOIN 
    film_category fc ON cat.category_id = fc.category_id
JOIN 
    inventory i ON fc.film_id = i.film_id
JOIN 
    rental r ON i.inventory_id = r.inventory_id
JOIN 
    payment p ON r.rental_id = p.rental_id
GROUP BY 
    cat.name
ORDER BY 
    receita_total DESC;
