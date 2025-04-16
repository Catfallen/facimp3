select c.first_name || ' ' || c.last_name as nome_completo, sum(p.amount) as total_gasto
from customer c
inner join payment p on c.customer_id = p.customer_id
group by nome_completo
order by total_gasto desc;