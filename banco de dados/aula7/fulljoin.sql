select a.first_name, a.last_name, f.title from actor a
full join film_actor fa on fa.actor_id = a.actor_id
full join film f on f.film_id = fa.film_id
order by a.actor_id desc;