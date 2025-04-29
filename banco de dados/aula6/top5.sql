select f.title,count(*) as total_alugados from rental r
join inventory i on i.inventory_id = r.inventory_id
join film f on f.film_id = i.film_id
group by f.title
order by total_alugados desc
limit 5;