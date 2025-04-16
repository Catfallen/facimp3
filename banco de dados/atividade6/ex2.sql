select f.title, c.name as categoria 
from film f
join film_category fc on fc.film_id = f.film_id
join category c on c.category_id = fc.category_id;


