create procedure inserir_actor(first_name text, last_name text)
Language plpgsql
AS $$
begin
    insert into actor(first_name,last_name)
    values (first_name,last_name);
end;
$$