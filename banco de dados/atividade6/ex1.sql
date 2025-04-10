select title,film.length 
from film 
where length > 120 
order by length desc limit 10;
