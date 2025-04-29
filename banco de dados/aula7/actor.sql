select a.first_name, a.last_name, f.title
from actor a
inner join film_actor fa on a.actor_id = fa.actor_id
inner join film f on fa.film_id = f.film_id;



select * from actor a